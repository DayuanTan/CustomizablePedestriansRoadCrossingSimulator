import os
import sys
sys.path.append(os.getcwd()+'/DayuanTanPCS')
from BackendAPI import BackendAPI
import global_params.global_params as global_params

# Step 1: Go to global_params.py to modify parameters in global_params.py file. Or modify in step 3.
# Step 2: Enable global params
params = global_params.global_params()

# Possible step 3:
# you can also modiy parameters here (or during your code anywhere) according to your demand
# e.g. I changed ped amount from left to right to 11 to replace its default value 10
params.ped_amount_lr = 11

# Step 4: run simulation and get result
BackendAPI.set_peds_initial_positions(params)
BackendAPI.cross_street(params)
needed_time = BackendAPI.get_ped_needed_time_to_cross(params)
print("These pedestrains need ", needed_time, " seconds to cross the street.\n")
