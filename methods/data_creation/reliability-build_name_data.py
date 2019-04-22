from __future__ import unicode_literals

# django imports
from django.contrib.auth.models import User

# sourcenet imports
from sourcenet.shared.sourcenet_base import SourcenetBase

# context_analysis imports
from context_analysis.reliability.reliability_names_builder import ReliabilityNamesBuilder

# declare variables
my_reliability_instance = None
tag_list = None
label = ""

# declare variables - user setup
current_coder = None
current_coder_id = -1
current_index = -1
current_priority = -1

# declare variables - Article_Data filtering.
coder_type = ""

# make reliability instance
my_reliability_instance = ReliabilityNamesBuilder()

#===============================================================================
# configure
#===============================================================================

# list of tags of articles we want to process.
#tag_list = [ "prelim_reliability_combined", ]
#tag_list = [ "prelim_reliability_test", ]
#tag_list = [ "prelim_reliability_test", ]
tag_list = [ "grp_month", ]

# label to associate with results, for subsequent lookup.
#label = "prelim_reliability_combined_human"
#label = "prelim_reliability_combined_all"
#label = "prelim_reliability_test_human"
#label = "prelim_reliability_test_all"
#label = "prelim_reliability_combined_human_final"
label = "prelim_month"

# ! ====> map coders to indices

# set it up so that...

# ...the ground truth user has highest priority (4) for index 1...
current_coder = SourcenetBase.get_ground_truth_coding_user()
current_coder_id = current_coder.id
current_index = 1
current_priority = 4
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# ...coder ID 8 is priority 3 for index 1...
current_coder_id = 8
current_index = 1
current_priority = 3
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# ...coder ID 9 is priority 2 for index 1...
current_coder_id = 9
current_index = 1
current_priority = 2
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# ...coder ID 10 is priority 1 for index 1...
current_coder_id = 10
current_index = 1
current_priority = 1
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# ...and automated coder (2) is index 2
current_coder = SourcenetBase.get_automated_coding_user()
current_coder_id = current_coder.id
current_index = 2
current_priority = 1
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# and only look at coding by those users.  And...

# configure so that it limits to automated coder_type of OpenCalais_REST_API_v2.
coder_type = "OpenCalais_REST_API_v2"
#my_reliability_instance.limit_to_automated_coder_type = "OpenCalais_REST_API_v2"
my_reliability_instance.automated_coder_type_include_list.append( coder_type )

# output debug JSON to file
#my_reliability_instance.debug_output_json_file_path = "/home/jonathanmorgan/" + label + ".json"

#===============================================================================
# process
#===============================================================================

# process articles
my_reliability_instance.process_articles( tag_list )

# output to database.
my_reliability_instance.output_reliability_data( label )
