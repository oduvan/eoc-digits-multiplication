from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "digits_multip"
    FUNCTION_NAMES = {
        "python_3": "digits_multip",
        "js_node": "digitsMultip"
    }
    ENV_COVERCODE = {
        
    }