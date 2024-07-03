import numpy as np
import xarray as xr

import dartsflash.libflash
from dartsflash.libflash import FlashParams, EoS
from dartsflash.mixtures.mixtures import Mixture


class Analysis:
    a: dartsflash.libflash.Analysis = None
    # s: dartsflash.libflash.Stability = None
    f: dartsflash.libflash.Flash = None
    flash_params: FlashParams = None

    def __init__(self, mixture: Mixture):
        self.mixture = mixture
        self.flash_params = FlashParams(mixture.comp_data)

        self.components = mixture.comp_data.components
        self.ions = mixture.comp_data.ions
        self.nc = mixture.comp_data.nc
        self.ni = mixture.comp_data.ni
        self.ns = mixture.comp_data.ns
        self.nv = self.ns + 2  # NC + 2 state specifications
        self.np_max = mixture.np_max

        self.eos = {}

        self.H2O_idx = self.components.index("H2O") if "H2O" in self.components else None

    def add_eos(self, eos_name: str, eos: EoS, eos_range: dict = None, initial_guesses: list = None,
                stability_tol: float = None, switch_tol: float = None, line_tol: float = None, max_iter: int = None,
                line_iter: int = None, preferred_eos: int = None):
        """
        Method to add EoS object and set EoS-specific parameters
        """
        eos_range = eos_range if eos_range is not None else {}
        for i, zrange in eos_range.items():
            eos.set_eos_range(i, zrange)

        self.eos[eos_name] = eos
        self.flash_params.add_eos(eos_name, eos)

        params = self.flash_params.eos_params[eos_name]
        params.initial_guesses = initial_guesses if initial_guesses is not None else params.initial_guesses
        params.stability_tol = stability_tol if stability_tol is not None else params.stability_tol
        params.stability_switch_tol = switch_tol if switch_tol is not None else params.stability_tol
        params.stability_line_tol = line_tol if line_tol is not None else params.stability_line_tol
        params.stability_max_iter = max_iter if max_iter is not None else params.stability_max_iter
        params.stability_line_iter = line_iter if line_iter is not None else params.stability_line_iter

        if preferred_eos is not None:
            self.flash_params.preferred_eos[preferred_eos] = eos_name

    def init_flash(self, stabilityflash: bool = True, eos: list = None, initial_guess: list = None):
        self.a = dartsflash.libflash.Analysis(self.flash_params)

        if stabilityflash:
            self.f = dartsflash.libflash.StabilityFlash(self.flash_params, self.np_max)
        else:
            self.f = dartsflash.libflash.NegativeFlash(self.flash_params, eos, initial_guess)

    def get_state(self, state_variables, variable_idxs, idxs, mole_fractions, comp_in_dims, molality: list = None):
        # Get state
        j = 0
        state = np.empty(self.nv)
        for ith_var, ith_idx in enumerate(variable_idxs):
            if hasattr(state_variables[ith_var], "__len__"):
                state[ith_idx] = state_variables[ith_var][idxs[j]]
                j += 1
            else:
                state[ith_idx] = state_variables[ith_var]

        # If mole fractions, normalize mole numbers
        if mole_fractions:
            sum_zc = np.sum(state[comp_in_dims])
            if sum_zc >= 1.-1e-15:
                state = None
            else:
                for ith_comp in range(self.nc):
                    if (ith_comp + 2) not in comp_in_dims:
                        state[ith_comp + 2] = (1. - sum_zc)

        # If molality
        if self.ni > 0:
            molality = molality if molality is not None else [0.]
            zi = molality[0] * state[2 + self.H2O_idx] / 55.509
            for i in range(self.ni):
                state[2 + self.nc + i] = zi
            state[2:] = state[2:]/np.sum(state[2:])

        return state

    def evaluate_full_space(self, state_spec: list, dimensions: dict, constants: dict, mole_fractions: bool,
                            evaluate, output_arrays: dict, dims_order: list = None, molality: list = None):
        """
        This is a loop over all specified states to which each Analysis subroutine can be passed

        :param state_spec:
        :type state_spec: list
        :param dimensions:
        :type dimensions: dict
        :param constants:
        :type constants: dict
        :param mole_fractions:
        :type mole_fractions: bool
        :param evaluate:
        :type evaluate:
        :param output_arrays:
        :type output_arrays:
        :param dims_order: Option to change order of execution of for loops over dimensions
        :type dims_order: list
        :param molality: List of molalities
        :type molality: list
        """
        # assert self.a is not None, "dartsflash.libflash.Analysis object has not been initialized"
        assert self.eos is not {}, "No EoS object has been defined"
        dims_order = list(dimensions.keys()) if dims_order is None else dims_order
        assert len(dims_order) == len(dimensions), "Incompatible order of dimensions"

        # Create xarray DataArray to store results
        array_shape = [len(dimensions[var]) for var in dims_order]
        n_dims = [i for i, dim in enumerate(dims_order)]
        n_points = np.prod(array_shape)

        # Know where to find state variables/constants
        state_variables = [dimensions[var] for var in dims_order] + [constant for var, constant in constants.items()]
        comp_in_dims = [i + 2 for i, comp in enumerate(self.components) if comp in dimensions.keys()]
        variable_idxs = [(state_spec + self.components).index(var)
                         for i, var in enumerate(dims_order + list(constants.keys()))]

        # Create data dict and coords for xarray DataArray to store results
        data = {prop: (dims_order + [prop + '_array'] if array_len > 1 else dims_order,
                       np.full(tuple(array_shape + [array_len] if array_len > 1 else array_shape), np.nan))
                for prop, array_len in output_arrays.items()}
        coords = {dimension: xrange for dimension, xrange in dimensions.items()}

        # Loop over dimensions to create state and evaluate function
        idxs = np.array([0 for i in n_dims])
        for point in range(n_points):
            # Get state
            state = self.get_state(state_variables, variable_idxs, idxs, mole_fractions, comp_in_dims, molality)

            # Evaluate method_to_evaluate(state)
            if state is not None:
                output_data = evaluate(state)
                for prop, method in output_data.items():
                    method_output = method()
                    if isinstance(data[prop][1][tuple(idxs)], (list, np.ndarray)):
                        try:
                            data[prop][1][tuple(idxs)][:len(method_output)] = method_output
                        except ValueError:
                            data[prop][1][tuple(idxs)][:] = np.nan
                    else:
                        data[prop][1][tuple(idxs)] = method_output

            # Increment idxs
            idxs[0] += 1
            for i in n_dims[1:]:
                if idxs[i-1] == array_shape[i-1]:
                    idxs[i-1] = 0
                    idxs[i] += 1
                else:
                    break

        # Save data
        results = xr.Dataset(coords=coords)
        for var_name in data.keys():
            results[var_name] = data[var_name]

        return results

    def evaluate_flash(self, state_spec: list, dimensions: dict, constants: dict, mole_fractions: bool,
                       dims_order: list = None, molality: list = None):
        """
        Method to evaluate flash

        :param state_spec:
        :type state_spec: list
        :param dimensions:
        :type dimensions: dict
        :param constants:
        :type constants: dict
        :param mole_fractions:
        :type mole_fractions: bool
        :param dims_order: Option to change order of execution of for loops over dimensions
        :type dims_order: list
        """
        output_arrays = {'nu': self.np_max, 'np': 1, 'X': self.np_max * self.ns, 'eos': self.np_max}

        def evaluate(state):
            error = self.f.evaluate(state[0], state[1], state[2:])
            if error:
                print("ERROR in flash", error)
                print("state", state)
            flash_results = self.f.get_flash_results()
            output_data = {"nu": lambda results=flash_results: results.nu,
                           "np": lambda results=flash_results: len(results.nu),
                           "X": lambda results=flash_results: results.X,
                           # "eos": lambda results=flash_results: results.eos
                           }
            return output_data

        return self.evaluate_full_space(state_spec=state_spec, dimensions=dimensions, constants=constants,
                                        mole_fractions=mole_fractions, evaluate=evaluate,
                                        output_arrays=output_arrays, dims_order=dims_order, molality=molality)

    def evaluate_properties_1p(self, state_spec: list, dimensions: dict, constants: dict,
                               properties_to_evaluate: dict, mole_fractions: bool, dims_order: list = None):
        """
        Method to evaluate single phase properties

        :param state_spec:
        :type state_spec: list
        :param dimensions:
        :type dimensions: dict
        :param constants:
        :type constants: dict
        :param properties_to_evaluate:
        :type properties_to_evaluate: dict
        :param mole_fractions:
        :type mole_fractions: bool
        :param dims_order: Option to change order of execution of for loops over dimensions
        :type dims_order: list
        """
        output_arrays = {property_name: 1 for property_name in properties_to_evaluate.keys()}

        def evaluate(state):
            output_data = {}
            for property_name, method in properties_to_evaluate.items():
                result = method(state[0], state[1], state[2:])
                output_data[property_name] = lambda res=result: res
            return output_data

        return self.evaluate_full_space(state_spec, dimensions, constants, mole_fractions, evaluate,
                                        output_arrays, dims_order)

    def evaluate_properties_np(self, flash_results: dict, properties: dict):
        return

    def evaluate_properties_of_mixing(self, eos_name: str, state_spec: list, dimensions: dict, constants: dict,
                                      properties: dict, dims_order: list = None):
        return

    def evaluate_stationary_points(self, state_spec: list, dimensions: dict, constants: dict, mole_fractions: bool,
                                   dims_order: list = None):
        """
        Method to evaluate stationary points

        :param state_spec:
        :type state_spec: list
        :param dimensions:
        :type dimensions: dict
        :param constants:
        :type constants: dict
        :param mole_fractions:
        :type mole_fractions: bool
        :param dims_order: Option to change order of execution of for loops over dimensions
        :type dims_order: list
        :param fname:
        :type fname: str
        """
        output_arrays = {'Y': self.np_max * self.nc, 'tot_sp': 1, 'neg_sp': 1, 'eos': self.np_max}

        def evaluate(state):
            stationary_points = self.a.find_stationary_points(state[0], state[1], state[2])
            output_data = {"Y": lambda spts=stationary_points: np.array([sp.Y for sp in spts]).flatten(),
                           "tot_sp": lambda spts=stationary_points: len(spts),
                           "neg_sp": lambda spts=stationary_points: np.sum([sp.tpd < 0 for sp in spts]),
                           "eos": lambda spts=stationary_points: np.array([sp.eos for sp in spts]),
            }
            return output_data

        return self.evaluate_full_space(state_spec, dimensions, constants, mole_fractions, evaluate, output_arrays, dims_order)

    def evaluate_stability_path(self, state):
        self.a.calc_stability_path()
        return {}

    def evaluate_split_path(self, state):
        self.a.calc_split_path()
        return {}
