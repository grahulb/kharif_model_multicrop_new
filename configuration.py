PLUGIN_MODE = 'DEBUG'	#	Possible values: 'DEBUG', 'TEST-SUITE', 'REAL'

#	Set the following for debugging or testing mode
DEBUG_BASE_FOLDER_PATH = 'C:\Users\Rahul\Desktop\Gondala1'
TEST_SUITE_BASE_FOLDER_PATH = 'NO PATH YET'
DEBUG_OR_TEST_CROPS = ['soyabean', 'bajra']	#	Possible values: subset of dict_crop.keys()
DEBUG_OR_TEST_GRADUATED_RENDERING_INTERVAL_POINTS = [0, 50]

#	Input-Output protocol constants
RAINFALL_CSV_FILENAME = 'Rainfall.csv'
ET0_CSV_FILENAME = 'ET0_file.csv'
POINTWISE_OUTPUT_CSV_FILENAME = 'kharif_model_pointwise_output.csv'
ZONEWISE_BUDGET_CSV_FILENAME = 'kharif_model_zonewise_budget.csv'
CADESTRAL_VULNERABILITY_CSV_FILENAME = 'kharif_model_cadestral_vulnerability.csv'
#	Optional inputs for debugging/testing
OVERRIDE_FILECROPS_BY_DEBUG_OR_TEST_CROPS = True
CROPS_FILENAME = 'crops.csv'

#	Computation Settings
STEP = 500.0
SOWING_THRESHOLD = 30
START_DATE_INDEX = 0
MONSOON_END_DATE_INDEX = 182
END_DATE_INDEX = 364
