# coding: utf8
"""

Python CAMB interface (https://github.com/mishakb/ISiTGR)

"""
#< ISiTGR MOD START
__url__ = "https://isitgr.readthedocs.io"
__version__ = "1.0.5"
__camb_version__ = "1.5.5"

from . import baseconfig

baseconfig.check_fortran_version(__camb_version__)
from .baseconfig import CAMBFortranError, CAMBError, CAMBValueError, CAMBUnknownArgumentError, CAMBParamRangeError
from .isitgr import get_results, get_transfer_functions, get_background, \
    get_age, get_zre_from_tau, set_feedback_level, set_params, get_matter_power_interpolator, \
    set_params_cosmomc, read_ini, run_ini, get_valid_numerical_params
#< ISiTGR MOD END
from . import model
from . import initialpower
from . import reionization
from . import dark_energy
from . import nonlinear
from .model import CAMBparams, TransferParams
from .results import CAMBdata, MatterTransferData, ClTransferData
from .reionization import TanhReionization, ExpReionization
from .nonlinear import Halofit
from .dark_energy import DarkEnergyFluid, DarkEnergyPPF
from .initialpower import InitialPowerLaw, SplinedInitialPower
from .mathutils import threej
from ._config import config
