# start to support python 3:
from __future__ import unicode_literals
from __future__ import division

#==============================================================================#
# ! imports
#==============================================================================#

# grouped by functional area, then alphabetical order by package, then
#     alphabetical order by name of thing being imported.

# context_analysis imports
from context_analysis.reliability.reliability_names_analyzer import ReliabilityNamesAnalyzer

#==============================================================================#
# ! logic
#==============================================================================#

# declare variables
my_analysis_instance = None
label = ""
indices_to_process = -1
result_status = ""

# make reliability instance
my_analysis_instance = ReliabilityNamesAnalyzer()

# database connection information - 2 options...  Enter it here:
#my_analysis_instance.db_username = ""
#my_analysis_instance.db_password = ""
#my_analysis_instance.db_host = "localhost"
#my_analysis_instance.db_name = "context_text"

# Or set up the following properties in Django_Config, inside the django admins.
#     All have application of: "context_text-db-admin":
#     - db_username
#     - db_password
#     - db_host
#     - db_port
#     - db_name

# run the analyze method, see what happens.
#label = "prelim_reliability_test"
#indices_to_process = 3
#label = "prelim_reliability_combined_human"
#indices_to_process = 3
#label = "name_data_test_combined_human"
#indices_to_process = 3
#label = "prelim_reliability_combined_human_final"
#indices_to_process = 3
#label = "prelim_reliability_combined_all"
#indices_to_process = 4
#label = "prelim_reliability_combined_all_final"
#indices_to_process = 4
#label = "prelim_reliability_test_human"
#indices_to_process = 3
#label = "prelim_reliability_test_all"
#indices_to_process = 4
label = "prelim_month"
indices_to_process = 2
result_status = my_analysis_instance.analyze_reliability_names( label, indices_to_process )
