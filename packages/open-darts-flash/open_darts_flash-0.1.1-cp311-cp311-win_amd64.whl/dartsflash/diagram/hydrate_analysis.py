import numpy as np

from dartsflash.diagram.analysis import Analysis
from dartsflash.libflash import VdWP


class HydrateAnalysis(Analysis):
    hydrate_eos: dict = {}

    def add_hydrate_eos(self, name: str, eos: VdWP):
        """
        Method to add hydrate EoS to map
        """
        self.hydrate_eos[name] = eos

    def calc_df(self, pressure, temperature, composition, phase: str = "sI"):
        """
        Method to calculate fugacity difference between fluid mixture and hydrate phase

        :param pressure: Pressure [bar]
        :param temperature: Temperature [K]
        :param composition: Feed mole fractions [-]
        :param phase: Hydrate phase type
        """
        self.f.evaluate(pressure, temperature, composition)
        V = self.f.getnu()
        x = np.array(self.f.getx()).reshape(len(V), self.ns)
        f0 = self.flash_params.eos_map["AQ"].fugacity(pressure, temperature, x[0, :])

        fwH = self.hydrate_eos[phase].fw(pressure, temperature, f0)
        df = fwH - f0[self.H2O_idx]
        return df

    def calc_equilibrium_pressure(self, temperature: float, composition: list, p_init: float, phase: str = "sI",
                                  max_it: int = 100, dp: float = 10., min_p: float = 1., max_p: float = None):
        """
        Method to calculate equilibrium pressure between fluid phases and hydrate phase at given T, z

        :param temperature: Temperature [K]
        :param composition: Feed mole fractions [-]
        :param p_init: Initial guess for equilibrium pressure [bar]
        :param phase: Hydrate phase type
        :param max_it: Maximum number of iterations of bisection method
        :param dp: Step size to find pressure bounds
        :param min_p: Minimum pressure [bar]
        :param max_p: Maximum pressure [bar]
        """
        # Find bounds for pressure
        p_min, p_max = p_init, p_init
        if self.calc_df(p_init, temperature, composition, phase) > 0:
            while True:
                p_max += dp
                if self.calc_df(p_max, temperature, composition, phase) < 0:
                    break
                p_min += dp
        else:
            while True:
                p_min = max(min_p, p_min-dp)
                if self.calc_df(p_min, temperature, composition, phase) > 0:
                    break
                p_max = max(min_p, p_max-dp)

        for it in range(1, max_it+1):
            pressure = (p_min + p_max) / 2
            df = self.calc_df(pressure, temperature, composition, phase)

            if np.abs(df) < 1e-10:
                return pressure
            else:
                if df > 0:
                    p_min = pressure
                else:
                    p_max = pressure
        print("Not converged", temperature)
        return None

    def calc_equilibrium_temperature(self, pressure: float, composition: list, t_init: float, phase: str = "sI",
                                     max_it: int = 100, dT: float = 10., min_t: float = 273.15, max_t: float = 373.15):
        """
        Method to calculate equilibrium temperature between fluid phases and hydrate phase at given P, z

        :param pressure: Pressure [bar]
        :param composition: Feed mole fractions [-]
        :param t_init: Initial guess for equilibrium temperature [K]
        :param phase: Hydrate phase type
        :param max_it: Maximum number of iterations of bisection method
        :param dT: Step size to find pressure bounds
        :param min_t: Minimum temperature [K]
        :param max_t: Maximum temperature [K]
        """
        # Find bounds for temperature
        T_min, T_max = t_init, t_init
        if self.calc_df(pressure, t_init, composition, phase) > 0:
            while True:
                T_max += dT
                if self.calc_df(pressure, T_max, composition) < 0:
                    break
        else:
            while True:
                T_min -= dT
                if self.calc_df(pressure, T_min, composition, phase) > 0:
                    break

        for it in range(1, max_it+1):
            temperature = (T_min + T_max) / 2

            df = self.calc_df(pressure, temperature, composition, phase)

            if np.abs(df) < 1e-10:
                return temperature
            else:
                if df > 0:
                    T_min = temperature
                else:
                    T_max = temperature
        print("Not converged", pressure)
        return None

    def calc_equilibrium_curve(self, composition: list, ref_data: list, pressure: list = None, temperature: list = None,
                               phase: str = "sI", number_of_curves: int = 1, max_it: int = 100, dX: float = 10.):
        """
        Method to calculate equilibrium pressure/temperature between fluid phases and hydrate phase at given P/T, z

        :param composition: Feed mole fractions [-]
        :param ref_data: Reference data to be used as initial guess for equilibrium P/T
        :param pressure: Pressure [bar]
        :param temperature: Temperature [K]
        :param phase: Hydrate phase type
        :param number_of_curves: Number of equilibrium curves
        :param max_it: Maximum number of iterations of bisection method
        :param dX: Step size to find P/T bounds
        """
        assert not (pressure is None and temperature is None), "Specify either range of pressures or temperatures"
        ref_data = [ref_data] if not isinstance(ref_data[0], (list, np.ndarray)) else ref_data
        assert len(ref_data) == number_of_curves, ("Reference data length ({:}) should be equal to specified"
                                                   "number of curves ({:})").format(len(ref_data), number_of_curves)
        composition = [composition for i in range(number_of_curves)] \
            if not isinstance(composition[0], (list, np.ndarray)) else composition

        # Calculate pressure for each temperature
        if pressure is None:
            pressure = [[] for i in range(number_of_curves)]
            temperature = [temperature for i in range(number_of_curves)] \
                if not isinstance(temperature[0], (list, np.ndarray)) else temperature
            for ith_curve in range(number_of_curves):
                len_data = len(temperature[ith_curve])
                assert len_data == len(ref_data[ith_curve]), "Reference data and temperature should be of same length"
                pressure[ith_curve] = np.zeros(len_data)
                for ith_temp, t in enumerate(temperature[ith_curve]):
                    comp = composition[ith_curve] if not isinstance(composition[ith_curve][0], (list, np.ndarray)) \
                        else composition[ith_curve][ith_temp]
                    pressure[ith_curve][ith_temp] = self.calc_equilibrium_pressure(t, comp, ref_data[ith_curve][ith_temp],
                                                                                   phase, max_it, dp=dX)
        # Else, calculate temperature for each pressure
        elif temperature is None:
            temperature = [[] for i in range(number_of_curves)]
            pressure = [pressure for i in range(number_of_curves)] \
                if not isinstance(pressure[0], (list, np.ndarray)) else pressure
            for ith_curve in range(number_of_curves):
                len_data = len(pressure[ith_curve])
                assert len_data == len(ref_data[ith_curve]), "Reference data and temperature should be of same length"
                temperature[ith_curve] = np.zeros(len_data)
                for ith_pres, p in enumerate(pressure[ith_curve]):
                    comp = composition[ith_curve] if not isinstance(composition[ith_curve][0], (list, np.ndarray)) \
                        else composition[ith_curve][ith_pres]
                    temperature[ith_curve][ith_pres] = self.calc_equilibrium_temperature(p, comp, ref_data[ith_curve][ith_pres],
                                                                                         phase, max_it, dT=dX)
        return pressure, temperature

    def calc_properties(self, pressure: list, temperature: list, composition: list, guest_idx: list,
                        number_of_curves: int = 1, phase: str = "sI"):
        """
        Method to calculate hydrate phase properties at given P,T,z:
        - Hydration number nH [-]
        - Density rhoH [kg/m3]
        - Enthalpy of hydrate formation/dissociation dH [kJ/kmol]

        :param pressure: Pressure [bar]
        :param temperature: Temperature [K]
        :param composition: Feed mole fractions [-]
        :param guest_idx: Index of guest molecule(s)
        :param phase: Hydrate phase type
        :param number_of_curves: Number of equilibrium curves
        """
        from dartsflash.eos_properties import EnthalpyIdeal, EoSEnthalpy, VdWPDensity, VdWPEnthalpy
        densH = VdWPDensity(self.hydrate_eos[phase], self.mixture.comp_data.Mw)
        enthH = VdWPEnthalpy(self.hydrate_eos[phase], EnthalpyIdeal(self.components, self.ions))
        enthV = EoSEnthalpy(self.flash_params.eos_map["SRK"], EnthalpyIdeal(self.components, self.ions))
        enthA = EoSEnthalpy(self.flash_params.eos_map["AQ"], EnthalpyIdeal(self.components, self.ions))

        nH = [[] for i in range(number_of_curves)]
        rhoH = [[] for i in range(number_of_curves)]
        dH = [[] for i in range(number_of_curves)]

        for i in range(number_of_curves):
            len_data = len(pressure[i])
            assert len(temperature[i]) == len_data

            nH[i] = [None] * len_data
            rhoH[i] = [None] * len_data
            dH[i] = [None] * len_data

            for j in range(len_data):
                if not pressure[i][j] is None or not temperature[i][j] is None:
                    self.calc_df(pressure[i][j], temperature[i][j], composition[i])
                    V = self.f.getnu()
                    x = np.array(self.f.getx()).reshape(len(V), self.ns)
                    xH = self.hydrate_eos[phase].xH()

                    # Calculate hydration number nH
                    nH[i][j] = 1. / xH[guest_idx] - 1.

                    # Density rhoH
                    rhoH[i][j] = densH.evaluate(pressure[i][j], temperature[i][j], xH)

                    # Enthalpy of hydrate formation/dissociation
                    Hv = enthV.evaluate(pressure[i][j], temperature[i][j], x[1, :])
                    Ha = nH[i][j] * enthA.evaluate(pressure[i][j], temperature[i][j], x[0, :])
                    Hh = enthH.evaluate(pressure[i][j], temperature[i][j], xH) * (nH[i][j] + 1)
                    dH[i][j] = (Hv + Ha - Hh) * 1e-3  # H_hyd < H_fluids -> enthalpy release upon formation

        return nH, rhoH, dH
