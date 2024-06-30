from cbr_website_beta.config.CBR_Config import CBR_Config
from osbot_utils.utils.Misc import list_set


class Health_Checks__CBR__Internal_Data:

    @staticmethod
    def cbr_config_data():
        cbr_config = CBR_Config().config()
        if list_set(cbr_config) == [ 'data', 'error', 'message', 'status']:
            return 'CBR_Config had the expected data'
        raise Exception('CBR_Config did NOT had the expected data')