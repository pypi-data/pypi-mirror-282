import numpy as np
import dartsflash.libflash
from dartsflash.libflash import Units


_Tc = {"H2O": 647.14, "CO2": 304.10, "N2": 126.20, "H2S": 373.53, "C1": 190.58, "C2": 305.32, "C3": 369.83, "iC4": 407.85, "nC4": 425.12, "iC5": 460.45, "nC5": 469.70, "nC6": 507.60, "nC7": 540.20, "nC8": 569.32, "nC9": 594.6, "nC10": 617.7, }
_Pc = {"H2O": 220.50, "CO2": 73.75, "N2": 34.00, "H2S": 89.63, "C1": 46.04, "C2": 48.721, "C3": 42.481, "iC4": 36.4, "nC4": 37.960, "iC5": 33.77, "nC5": 33.701, "nC6": 30.251, "nC7": 27.40, "nC8": 24.97, "nC9": 22.88, "nC10": 21.2, }
_ac = {"H2O": 0.328, "CO2": 0.239, "N2": 0.0377, "H2S": 0.0942, "C1": 0.012, "C2": 0.0995, "C3": 0.1523, "iC4": 0.1844, "nC4": 0.2002, "iC5": 0.227, "nC5": 0.2515, "nC6": 0.3013, "nC7": 0.3495, "nC8": 0.396, "nC9": 0.445, "nC10": 0.489, }
_Mw = {"H2O": 18.015, "CO2": 44.01, "N2": 28.013, "H2S": 34.10, "C1": 16.043, "C2": 30.07, "C3": 44.097, "iC4": 58.124, "nC4": 58.124, "iC5": 72.151, "nC5": 72.151, "nC6": 86.178, "nC7": 100.205, "nC8": 114.231, "nC9": 128.257, "nC10": 142.2848, }

_kij = {"H2O": {"H2O": 0., "CO2": 0.19014, "N2": 0.32547, "H2S": 0.105, "C1": 0.47893, "C2": 0.5975, "C3": 0.5612, "iC4": 0.508, "nC4": 0.5569, "iC5": 0.5, "nC5": 0.5260, "nC6": 0.4969, "nC7": 0.4880, "nC8": 0.48, "nC9": 0.48, "nC10": 0.48, },
        "CO2": {"H2O": 0.19014, "CO2": 0., "N2": -0.0462, "H2S": 0.1093, "C1": 0.0936, "C2": 0.1320, "C3": 0.1300, "iC4": 0.13, "nC4": 0.1336, "iC5": 0.13, "nC5": 0.1454, "nC6": 0.1167, "nC7": 0.1209, "nC8": 0.1, "nC9": 0.1, "nC10": 0.1, },
        "N2": {"H2O": 0.32547, "CO2": -0.0462, "N2": 0., "H2S": 0.1475, "C1": 0.0291, "C2": 0.0082, "C3": 0.0862, "iC4": 0.1, "nC4": 0.0596, "iC5": 0.1, "nC5": 0.0917, "nC6": 0.1552, "nC7": 0.1206, "nC8": 0.1, "nC9": 0.1, "nC10": 0.1, },
        "H2S": {"H2O": 0.105, "CO2": 0.1093, "N2": 0.1475, "H2S": 0., "C1": 0.0912, "C2": 0.0846, "C3": 0.0874, "iC4": 0.06, "nC4": 0.0564, "iC5": 0.06, "nC5": 0.0655, "nC6": 0.0465, "nC7": 0.0191, "nC8": 0, "nC9": 0, "nC10": 0.1, },
        "C1": {"H2O": 0.47893, "CO2": 0.0936, "N2": 0.0291, "H2S": 0.0912, "C1": 0., "C2": 0.00518, "C3": 0.01008, "iC4": 0.026717, "nC4": 0.0152, "iC5": 0.0206, "nC5": 0.0193, "nC6": 0.0258, "nC7": 0.0148, "nC8": 0.037, "nC9": 0.03966, "nC10": 0.048388, },
        "C2": {"H2O": 0.5975, "CO2": 0.1320, "N2": 0.0082, "H2S": 0.0846, "C1": 0.00518, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "nC5": 0., "iC5": 0, "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "C3": {"H2O": 0.5612, "CO2": 0.1300, "N2": 0.0862, "H2S": 0.0874, "C1": 0.01008, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "nC5": 0., "iC5": 0, "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "iC4": {"H2O": 0.508, "CO2": 0.13, "N2": 0.1, "H2S": 0.06, "C1": 0.026717, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "iC5": 0, "nC5": 0., "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "nC4": {"H2O": 0.5569, "CO2": 0.1336, "N2": 0.0596, "H2S": 0.0564, "C1": 0.0152, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "iC5": 0, "nC5": 0., "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "iC5": {"H2O": 0.5, "CO2": 0.13, "N2": 0.1, "H2S": 0.06, "C1": 0.0206, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "iC5": 0, "nC5": 0., "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "nC5": {"H2O": 0.5260, "CO2": 0.1454, "N2": 0.0917, "H2S": 0.0655, "C1": 0.0193, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "iC5": 0, "nC5": 0., "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "nC6": {"H2O": 0.4969, "CO2": 0.1167, "N2": 0.1552, "H2S": 0.0465, "C1": 0.0258, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "iC5": 0, "nC5": 0., "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "nC7": {"H2O": 0.4880, "CO2": 0.1209, "N2": 0.1206, "H2S": 0.0191, "C1": 0.0148, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "iC5": 0, "nC5": 0., "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "nC8": {"H2O": 0.48, "CO2": 0.1, "N2": 0.1, "H2S": 0, "C1": 0.037, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "iC5": 0, "nC5": 0., "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "nC9": {"H2O": 0.48, "CO2": 0.1, "N2": 0.1, "H2S": 0, "C1": 0.03966, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "iC5": 0, "nC5": 0., "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        "nC10": {"H2O": 0.48, "CO2": 0.1, "N2": 0.1, "H2S": 0.1, "C1": 0.048388, "C2": 0., "C3": 0., "iC4": 0, "nC4": 0., "iC5": 0, "nC5": 0., "nC6": 0., "nC7": 0., "nC8": 0, "nC9": 0, "nC10": 0, },
        }

_H0 = {"H2O": 0., "CO2": 33., "N2": 0.64, "H2S": 100., "C1": 1.4, "C2": 1.9, "C3": 1.5, "iC4": 0.91, "nC4": 1.2, "iC5": 0.7, "nC5": 0.8, "nC6": 0.61, "nC7": 0.44, "nC8": 0.31, "nC9": 0.2, "nC10": 0.14, }
_dlnH0 = {"H2O": 0., "CO2": 2400., "N2": 1600., "H2S": 2100., "C1": 1900., "C2": 2400., "C3": 2700., "iC4": 2700., "nC4": 3100., "iC5": 3400., "nC5": 3400., "nC6": 3800., "nC7": 4100., "nC8": 4300., "nC9": 5000., "nC10": 5000., }

_charge = {"Na+": 1, "Cl-": -1}

_hi0 = {"H2O": -242000., "CO2": -393800., "N2": 0., "H2S": -20200.,
        "C1": -74900., "C2": -84720., "C3": -103900., "iC4": -134600., "nC4": -126200.,
        "iC5": -165976., "nC5": -146500., "nC6": -167300., "nC7": -187900., "NaCl": -411153.00
        }
R = 8.3145
_hia = {"H2O": [3.8747*R, 0.0231E-2*R, 0.1269E-5*R, -0.4321E-9*R],
        "CO2": [2.6751*R, 0.7188E-2*R, -0.4208E-5*R, 0.8977E-9*R],
        "N2": [3.4736*R, -0.0189E-2*R, 0.0971E-5*R, -0.3453E-9*R],
        "H2S": [3.5577*R, 0.1574E-2*R, 0.0686E-5*R, -0.3959E-9*R],
        "C1": [2.3902*R, 0.6039E-2*R, 0.1525E-5*R, -1.3234E-9*R],
        "C2": [0.8293*R, 2.0752E-2*R, -0.7699E-5*R, 0.8756E-9*R],
        "C3": [-0.4861*R, 3.6629E-2*R, -1.8895E-5*R, 3.8143E-9*R],
        "iC4": [-0.9511*R, 4.9999E-2*R, -2.7651E-5*R, 5.9982E-9*R],
        "nC4": [0.4755*R, 4.4650E-2*R, -2.2041E-5*R, 4.2068E-9*R],
        "iC5": [-1.9942*R, 6.6725E-2*R, -3.9738E-5*R, 9.1735E-9*R],
        "nC5": [0.8142*R, 5.4598E-2*R, -2.6997E-5*R, 5.0824E-9*R],
        "nC6": [0.8338*R, 6.6373E-2*R, -3.444E-5*R, 6.9342E-9*R],
        "nC7": [-0.6184*R, 8.1268E-2*R, -4.388E-5*R, 9.2037E-9*R],
        "NaCl": [5.526*R, 0.1963e-2*R, 0., 0.]
        }

def get_properties(property: dict, species: list):
    return np.array([property[i] if i in property.keys() else 0. for i in species])


class CompData(dartsflash.libflash.CompData):
    """
    This class contains component properties and data.

    :ivar nc: Number of components
    :type nc: int
    :ivar ni: Number of ions
    :type ni: int
    :ivar ns: Number of species (components + ions)
    :type ns: int
    :ivar Pc: List of component critical pressures [bar]
    :type Pc: list
    :ivar Tc: List of component critical temperatures [K]
    :type Tc: list
    :ivar ac: List of component acentric factors [-]
    :type ac: list
    :ivar Mw: List of species molar weight [g/mol]
    :type Mw: list
    :ivar kij: List of component binary interaction coefficients (flattened 2D array)
    :type kij: list
    :ivar H0: List of component H0 (Sander, 2006)
    :type H0: list
    :ivar dlnH0: List of component dlnH0 (Sander, 2006)
    :type dlnH0: list
    :ivar charge: List of ion charges
    :type charge: list
    """
    def __init__(self, components: list, ions: list = None, setprops: bool = False):
        """        
        :param components: List of components
        :type components: list
        :param ions: List of ions, default is None, sets empty list
        :type ions: list
        :param setprops: Switch to get properties from pre-defined data, default is False
        :type setprops: bool
        :param units: Object that contains units and methods for unit conversion
        :type units: :class:`dartsflash.libflash.Units`
        """
        super().__init__(components, ions if ions is not None else [])

        self.components = components
        self.ions = ions if ions is not None else []

        if setprops:
            self.set_properties()

    def set_properties(self, Pc: list = None, Tc: list = None, ac: list = None, Mw: list = None, kij: list = None, H0: list = None, dlnH0: list = None):
        """
        Function to populate properties with pre-defined properties from data at the top of this file
        """
        self.Pc = get_properties(_Pc, self.components) if Pc is None else Pc
        self.Tc = get_properties(_Tc, self.components) if Tc is None else Tc
        self.ac = get_properties(_ac, self.components) if ac is None else ac
        self.Mw = get_properties(_Mw, self.components) if Mw is None else Mw
        self.kij = np.array([get_properties(_kij[i], self.components) for i in self.components]).flatten() if kij is None else kij
        self.H0 = get_properties(_H0, self.components) if H0 is None else H0
        self.dlnH0 = get_properties(_dlnH0, self.components) if dlnH0 is None else dlnH0

        self.charge = get_properties(_charge, self.ions) if self.ions else []

        return

    def twu_dij(self, components: list, comp_data: dict):
        """
        Function to calculate Twu binary interaction coefficients

        :returns: Array of Twu () binary interaction coefficients
        :rtype: :class:`np.ndarray`
        """
        n = 1.2
        nc = len(components)

        Vc = np.zeros(nc)
        for i in range(nc):
            SG = comp_data["SG"][i]
            Tb = comp_data["Tb"][i]
            Tc0 = Tb * (0.533272 + 0.191017e-3 * Tb + 0.779681e-7 * Tb**2 - 0.284376e-10 * Tb**3 + 0.959468e28 * Tb**(-13))**(-1)
            a = 1 - Tb / Tc0
            Vc0 = (1 - (0.419869 - 0.505839*a - 1.56436*a**3 - 9481.7*a**14))**(-8)
            SG0 = 0.843593 - 0.128624*a - 3.36159*a**3 - 13749.5*a**12
            dSGV = np.exp(4*(SG0**2-SG**2))-1
            fV = dSGV * (0.46659/np.sqrt(Tb) + (-0.182421 + 3.01721/np.sqrt(Tb))*dSGV)
            Vc[i] = Vc0 * ((1+2*fV)/(1-2*fV))**2

        dij = np.zeros(nc * nc)
        for i, compi in enumerate(components):
            for j, compj in enumerate(components):
                if i != j:
                    dij[i * nc + j] = 1 - (2 * Vc[i]**(1/6) * Vc[j]**(1/6) / (Vc[i]**(1/3) + Vc[j]**(1/3))) ** n
        return dij


class EnthalpyIdeal:
    """
    This class can evaluate ideal gas enthalpy
    
    From: Jager et al. (2003) - The next generation of hydrate prediction II. Dedicated aqueous phase fugacity model for hydrate prediction

    :ivar T_0: Reference temperature for Jager (2003) correlation (T_0 = 298.15 K)
    :type T_0: float
    """
    T_0 = 298.15

    def __init__(self, components: list, ions: list = None):
        """        
        :param components: List of components
        :type components: list
        :param ions: List of ions, default is None, sets empty list
        :type ions: list
        """
        self.nc = len(components)
        self.hi_0 = get_properties(_hi0, components)
        self.hi_a = get_properties(_hia, components)

    def evaluate(self, temperature, x):
        """
        Evaluates the ideal gas enthalpy at given temperature and composition x.
        
        :param temperature: Temperature in Kelvin
        :type temperature: float
        :param x: Phase composition in mole fractions/mole numbers
        :type x: list

        :returns: Ideal gas enthalpy in J/mol
        :rtype: float
        """
        Hi = 0.
        for i in range(self.nc):
            ai = self.hi_a[i]
            Hi_i = self.hi_0[i] + ai[0] * (temperature - self.T_0) + ai[1] / 2. * (temperature ** 2 - self.T_0 ** 2)\
                                + ai[2] / 3. * (temperature ** 3 - self.T_0 ** 3) + ai[3] / 4. * (temperature ** 4 - self.T_0 ** 4)
            Hi += x[i] * Hi_i

        return Hi
