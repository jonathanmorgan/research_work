'''
You must create an index-able instance and place it in my_index_instance before
    you run this code.  The index configuration in this file will be applied to
    the instance stored in "my_index_instance".
    
Objects you can pass in this instance:

from sourcenet_analysis.reliability.reliability_names_builder import ReliabilityNamesBuilder
from sourcenet_analysis.network.network_person_info import NetworkPersonInfo
'''

# imports
import datetime

# sourcenet imports
from sourcenet.shared.sourcenet_base import SourcenetBase

# sourcenet_analysis imports
from sourcenet_analysis.reliability.reliability_names_builder import ReliabilityNamesBuilder
from sourcenet_analysis.network.network_person_info import NetworkPersonInfo

# return reference
index_helper_OUT = None

# declare variables
tag_list = None
label = ""

# declare variables - user setup
my_info_instance = None
my_reliability_instance = None
current_coder = None
current_coder_id = -1
current_priority = -1

# declare variables - Article_Data filtering.
coder_type = ""

#===============================================================================
# configure
#===============================================================================

# list of tags of articles we want to process.
tag_list = [ "prelim_network", ]

# label to associate with results, for subsequent lookup.
label = "prelim_network"

# create index instances
my_info_instance = NetworkPersonInfo()
my_reliability_instance = ReliabilityNamesBuilder()

# ! ====> map coders to indices

# set it up so that...

# ...the ground truth user has highest priority (4) for index 1...
current_coder = SourcenetBase.get_ground_truth_coding_user()
current_coder_id = current_coder.id
current_index = 1
current_priority = 4
my_info_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# ...coder ID 8 is priority 3 for index 1...
current_coder_id = 8
current_index = 1
current_priority = 3
my_info_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# ...coder ID 9 is priority 2 for index 1...
current_coder_id = 9
current_index = 1
current_priority = 2
my_info_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# ...coder ID 10 is priority 1 for index 1...
current_coder_id = 10
current_index = 1
current_priority = 1
my_info_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# ...and automated coder (2) is index 2
current_coder = SourcenetBase.get_automated_coding_user()
current_coder_id = current_coder.id
current_index = 2
current_priority = 1
my_info_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )
my_reliability_instance.add_coder_at_index( current_coder_id, current_index, priority_IN = current_priority )

# and only look at coding by those users.  And...

# configure so that it limits to automated coder_type of OpenCalais_REST_API_v2.
coder_type = "OpenCalais_REST_API_v2"
#my_reliability_instance.limit_to_automated_coder_type = "OpenCalais_REST_API_v2"
my_info_instance.automated_coder_type_include_list.append( coder_type )
my_reliability_instance.automated_coder_type_include_list.append( coder_type )

index_helper_OUT = my_info_instance.get_index_helper()

print( "indexing for prelim_network (1 week) initialized at " + str( datetime.datetime.now() ) )