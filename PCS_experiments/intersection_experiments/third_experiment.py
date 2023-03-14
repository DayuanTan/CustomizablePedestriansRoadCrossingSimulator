from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import optparse
import xml.etree.ElementTree as ET

# we need to import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)

    dayuanSUMOpath = os.path.join("/usr","local","opt","sumo","share","sumo","tools")
    sys.path.append(dayuanSUMOpath)
    print("PATH:",sys.path)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")



from datetime import datetime
from sumolib import checkBinary  
import traci  
import traci.constants as tc # used for subscription

sys.path.append(os.getcwd()+'/DayuanTanPCS')
from BackendAPI import BackendAPI # PCS
import global_params.global_params as global_params # PCS

def is_Sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and i+n<len(l) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True

	return sub_set


def get_ped_direction2count():
    print_system_on = False #True #False
    all_ped_list = list()

    #count ped
    allPedOnN1 = traci.edge.getLastStepPersonIDs("N1")
    if print_system_on: print("\nN allPedOnN1: ", allPedOnN1)
    for pedi in allPedOnN1:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
        if traci.person.getLanePosition(pedi) >= 180: #max 183.2
            all_ped_list.append(pedi)
    allPedOnN2 = traci.edge.getLastStepPersonIDs("N2")
    if print_system_on: print("\nN allPedOnN2: ", allPedOnN2)
    for pedi in allPedOnN2:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
        if traci.person.getLanePosition(pedi) <= 3:
            all_ped_list.append(pedi)

    allPedOnE1 = traci.edge.getLastStepPersonIDs("E1")
    if print_system_on: print("\nN allPedOnE1: ", allPedOnE1)
    for pedi in allPedOnE1:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
        if traci.person.getLanePosition(pedi) >= 180:
            all_ped_list.append(pedi)
    allPedOnE2 = traci.edge.getLastStepPersonIDs("E2")
    if print_system_on: print("\nN allPedOnE2: ", allPedOnE2)
    for pedi in allPedOnE2:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
        if traci.person.getLanePosition(pedi) <= 3:
            all_ped_list.append(pedi)

    allPedOnS1 = traci.edge.getLastStepPersonIDs("S1")
    if print_system_on: print("\nN allPedOnS1: ", allPedOnS1)
    for pedi in allPedOnS1:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
        if traci.person.getLanePosition(pedi) >= 180:
            all_ped_list.append(pedi)
    allPedOnS2 = traci.edge.getLastStepPersonIDs("S2")
    if print_system_on: print("\nN allPedOnS2: ", allPedOnS2)
    for pedi in allPedOnS2:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
        if traci.person.getLanePosition(pedi) <= 3:
            all_ped_list.append(pedi)

    allPedOnW1 = traci.edge.getLastStepPersonIDs("W1")
    if print_system_on: print("\nW allPedOnW1: ", allPedOnW1)
    for pedi in allPedOnW1:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
        if traci.person.getLanePosition(pedi) >= 180:
            all_ped_list.append(pedi)
    allPedOnW2 = traci.edge.getLastStepPersonIDs("W2")
    if print_system_on: print("\nW allPedOnW2: ", allPedOnW2)
    for pedi in allPedOnW2:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
        if traci.person.getLanePosition(pedi) <= 3:
            all_ped_list.append(pedi)

    #c0 north crosswalk
    allPedOn_centernode_c0 = traci.edge.getLastStepPersonIDs(":centernode_c0")
    if print_system_on: print("\nN allPedOn_centernode_c0: ", allPedOn_centernode_c0)
    for pedi in allPedOn_centernode_c0:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
    #c1 east crosswalk
    allPedOn_centernode_c1 = traci.edge.getLastStepPersonIDs(":centernode_c1")
    if print_system_on: print("\nE allPedOn_centernode_c1: ", allPedOn_centernode_c1)
    for pedi in allPedOn_centernode_c1:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
    #c2 south crosswalk
    allPedOn_centernode_c2 = traci.edge.getLastStepPersonIDs(":centernode_c2")
    if print_system_on: print("\nS allPedOn_centernode_c2: ", allPedOn_centernode_c2)
    for pedi in allPedOn_centernode_c2:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
    #c3 west crosswalk
    allPedOn_centernode_c3 = traci.edge.getLastStepPersonIDs(":centernode_c3")
    if print_system_on: print("\nW allPedOn_centernode_c3: ", allPedOn_centernode_c3)
    for pedi in allPedOn_centernode_c3:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
    
    #w0 north west corner
    allPedOn_centernode_w0 = traci.edge.getLastStepPersonIDs(":centernode_w0")
    if print_system_on: print("\nNW allPedOn_centernode_w0: ", allPedOn_centernode_w0)
    for pedi in allPedOn_centernode_w0:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
    #w1 north east corner
    allPedOn_centernode_w1 = traci.edge.getLastStepPersonIDs(":centernode_w1")
    if print_system_on: print("\nNE allPedOn_centernode_w1: ", allPedOn_centernode_w1)
    for pedi in allPedOn_centernode_w1:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
    #w2 south east corner
    allPedOn_centernode_w2 = traci.edge.getLastStepPersonIDs(":centernode_w2")
    if print_system_on: print("\nSE allPedOn_centernode_w2: ", allPedOn_centernode_w2)
    for pedi in allPedOn_centernode_w2:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
    #w3 south west corner
    allPedOn_centernode_w3 = traci.edge.getLastStepPersonIDs(":centernode_w3")
    if print_system_on: print("\nSW allPedOn_centernode_w3: ", allPedOn_centernode_w3)
    for pedi in allPedOn_centernode_w3:
        if print_system_on: print("pedi: ", pedi, " getEdges: ", traci.person.getEdges(pedi), " getLaneID: ", traci.person.getLaneID(pedi), " getLanePosition: ", traci.person.getLanePosition(pedi), " getNextEdge: ", traci.person.getNextEdge(pedi), " getStage: ", traci.person.getStage(pedi))
    
    # get all ped
    # all_ped_list = allPedOnN1 + allPedOnN2 + allPedOnE1 + allPedOnE2 + allPedOnS1 +  allPedOnS2 + allPedOnW1 + allPedOnW2 + allPedOn_centernode_c0 + allPedOn_centernode_c1 + allPedOn_centernode_c2 + allPedOn_centernode_c3 + allPedOn_centernode_w0 + allPedOn_centernode_w1 + allPedOn_centernode_w2 + allPedOn_centernode_w3
    other_ped_list = allPedOn_centernode_c0 + allPedOn_centernode_c1 + allPedOn_centernode_c2 + allPedOn_centernode_c3 + allPedOn_centernode_w0 + allPedOn_centernode_w1 + allPedOn_centernode_w2 + allPedOn_centernode_w3
    all_ped_list.extend(other_ped_list)
    # remove duplicate
    temp = set(all_ped_list)
    all_ped_list = list(temp)
    # count for each direction
    ped_direction2count = {
        "N_W2E": 0, "N_E2W": 0, 
        "E_N2S": 0, "E_S2N": 0,
        "S_W2E": 0, "S_E2W": 0,
        "W_N2S": 0, "W_S2N": 0
    }
    ped_direction2personID = {
        "N_W2E": list(), "N_E2W": list(), 
        "E_N2S": list(), "E_S2N": list(),
        "S_W2E": list(), "S_E2W": list(),
        "W_N2S": list(), "W_S2N": list()
    }
    for pedi in all_ped_list:
        if is_Sublist(list(traci.person.getEdges(pedi)), ['N1', 'N2']):        
            ped_direction2count["N_W2E"] += 1
            ped_direction2personID["N_W2E"].append(pedi)
        elif is_Sublist(list(traci.person.getEdges(pedi)), ['N2', 'N1']): 
            ped_direction2count["N_E2W"] += 1
            ped_direction2personID["N_E2W"].append(pedi)
        elif is_Sublist(list(traci.person.getEdges(pedi)), ['E1', 'E2']):
            ped_direction2count["E_N2S"] += 1
            ped_direction2personID["E_N2S"].append(pedi)
        elif is_Sublist(list(traci.person.getEdges(pedi)), ['E2', 'E1']):
            ped_direction2count["E_S2N"] += 1
            ped_direction2personID["E_S2N"].append(pedi)
        elif is_Sublist(list(traci.person.getEdges(pedi)), ['S2', 'S1']):
            ped_direction2count["S_W2E"] += 1
            ped_direction2personID["S_W2E"].append(pedi)
        elif is_Sublist(list(traci.person.getEdges(pedi)), ['S1', 'S2']):
            ped_direction2count["S_E2W"] += 1
            ped_direction2personID["S_E2W"].append(pedi)
        elif is_Sublist(list(traci.person.getEdges(pedi)), ['W2', 'W1']):
            ped_direction2count["W_N2S"] += 1
            ped_direction2personID["W_N2S"].append(pedi)
        elif is_Sublist(list(traci.person.getEdges(pedi)), ['W1', 'W2']):
            ped_direction2count["W_S2N"] += 1
            ped_direction2personID["W_S2N"].append(pedi)
    if print_system_on: print("ped_direction2count: ", ped_direction2count)
    # print("ped_direction2count: ", ped_direction2count)

    return ped_direction2count, ped_direction2personID

 # kill those person object (they have crossed in theory)
def kill_personobject(ped_direction2personID, direction1, direction2):
    for pedi in ped_direction2personID[direction1]:
        traci.person.removeStages(pedi)
    for pedi in ped_direction2personID[direction2]:
        traci.person.removeStages(pedi)


def run():
    """execute the TraCI control loop"""
    step = 0
    arrivedPersonCtr = 0
    alivePersonIDList = list()
    pedestrian_total_waited_time = 0
    pedID2waitingTime = dict()

    phaseNoCurr = 0
    phaseNoPrevious = 0 # total 4 phases

    #while traci.simulation.getTime() <209:#unit is s. Set a short time for testing
    while traci.simulation.getMinExpectedNumber() > 0 : # run until all v and ped have arrived. 
        traci.simulationStep() # forward one step
        # print("\n\n----------------\nstep: ", step)

        # first 52 s set as red light so no car pass intersection.
        if step < 52:
            traci.trafficlight.setPhase("centernode", 2)
        # Start the first phase in first cycle at 52 s, following real world
        if step == 52:
            traci.trafficlight.setPhase("centernode", 0) 


        # change green light duration
        phaseNoCurr = traci.trafficlight.getPhase("centernode")
        # calc green duration for NS
        if phaseNoCurr == 0 and (phaseNoPrevious == 2 or phaseNoPrevious == 3): 
            vNumTurnLeft_N, vNumOther_N = 0, 0
            vIDs = traci.edge.getLastStepVehicleIDs("N1")
            for vID in vIDs:
                routeID = traci.vehicle.getRouteID(vID)
                if routeID in ["N2E", "S2W", "E2S", "W2N"]: # if turn left
                    vNumTurnLeft_N += 1
                else:
                    vNumOther_N += 1
            
            vNumTurnLeft_S, vNumOther_S = 0, 0
            vIDs = traci.edge.getLastStepVehicleIDs("S1")
            for vID in vIDs:
                routeID = traci.vehicle.getRouteID(vID)
                if routeID in ["N2E", "S2W", "E2S", "W2N"]: # if turn left
                    vNumTurnLeft_S += 1
                else:
                    vNumOther_S += 1

            ped_direction2count, ped_direction2personID =  get_ped_direction2count()
            # W
            # PCS
            # Step 1: Modify parameters in global_params.py file. I have done it.
            # Step 2: Enable global params
            params = global_params.global_params()
            # Possible step 3:
            params.crosswalk_width = 360 #cm
            params.crosswalk_length = 4362 #cm
            params.waiting_area_width = params.crosswalk_width
            params.waiting_area_length = 300 #cm
            params.total_length = params.waiting_area_length * 2 + params.crosswalk_length
            params.outside_margin_width = 100 # cm
            params.waiting_area_position_x_offset_min = 0 - params.waiting_area_length
            params.waiting_area_position_x_offset_max = params.waiting_area_length
            params.waiting_area_position_x_offset_mean = 0 #coordinate
            params.waiting_area_position_x_offset_sigma = params.waiting_area_length / 2 # max = mean + 2*sigma
            params.waiting_area_position_y_min = 0
            params.waiting_area_position_y_max = params.crosswalk_width
            params.waiting_area_position_y_mean = params.crosswalk_width / 2 #coordinate
            params.waiting_area_position_y_sigma = params.crosswalk_width / 2 # max = mean + 2*sigma => sigma = (max - mean )/2
            
            params.ped_amount_lr = ped_direction2count["W_N2S"]
            params.ped_amount_rl = ped_direction2count["W_S2N"]
            # clean variables
            params.all_peds_lr = list() # all ped who want go from left to right
            params.all_peds_rl = list() # all ped who want go from right to left
            params.all_peds = list()  # all ped 
            params.all_peds_lr_sorted_by_x = list() # all sorted ped who want go from left to right, sorted by x reversed, biggest x first
            params.all_peds_rl_sorted_by_x = list() # all sorted ped who want go from right to left, sorted by x, smallest x first 
            params.all_peds_ordered = list()
            # Step 4: run simulation and get result
            BackendAPI.set_peds_initial_positions(params)
            BackendAPI.cross_street(params)
            W_needed_time = BackendAPI.get_ped_needed_time_to_cross(params)
            # print("W These pedestrains need ", W_needed_time, " seconds to cross the street.\n")
            # kill those persons (they have crossed in theory)
            kill_personobject(ped_direction2personID, "W_N2S", "W_S2N")

            # E
            # PCS
            # Step 1: Modify parameters in global_params.py file. I have done it.
            # Step 2: Enable global params
            params = global_params.global_params()
            # print("test: ", params.all_peds)
            # Possible step 3:
            params.crosswalk_width = 360 #cm
            params.crosswalk_length = 4362 #cm
            params.waiting_area_width = params.crosswalk_width
            params.waiting_area_length = 300 #cm
            params.total_length = params.waiting_area_length * 2 + params.crosswalk_length
            params.outside_margin_width = 100 # cm
            params.waiting_area_position_x_offset_min = 0 - params.waiting_area_length
            params.waiting_area_position_x_offset_max = params.waiting_area_length
            params.waiting_area_position_x_offset_mean = 0 #coordinate
            params.waiting_area_position_x_offset_sigma = params.waiting_area_length / 2 # max = mean + 2*sigma
            params.waiting_area_position_y_min = 0
            params.waiting_area_position_y_max = params.crosswalk_width
            params.waiting_area_position_y_mean = params.crosswalk_width / 2 #coordinate
            params.waiting_area_position_y_sigma = params.crosswalk_width / 2 # max = mean + 2*sigma => sigma = (max - mean )/2

            params.ped_amount_lr = int(ped_direction2count["E_N2S"])
            params.ped_amount_rl = int(ped_direction2count["E_S2N"])
            # clean variables
            params.all_peds_lr = list() # all ped who want go from left to right
            params.all_peds_rl = list() # all ped who want go from right to left
            params.all_peds = list()  # all ped 
            params.all_peds_lr_sorted_by_x = list() # all sorted ped who want go from left to right, sorted by x reversed, biggest x first
            params.all_peds_rl_sorted_by_x = list() # all sorted ped who want go from right to left, sorted by x, smallest x first 
            params.all_peds_ordered = list()
            # Step 4: run simulation and get result
            BackendAPI.set_peds_initial_positions(params)
            BackendAPI.cross_street(params)
            E_needed_time = BackendAPI.get_ped_needed_time_to_cross(params)
            # print("E These pedestrains need ", E_needed_time, " seconds to cross the street.\n")
            # kill those persons (they have crossed in theory)
            kill_personobject(ped_direction2personID, "E_N2S", "E_N2S")

            # greenDur1 = max(vNumOther_N / 4 * 4 , W_needed_time) + vNumTurnLeft_S * 4 # 4lanes, avg 4 seconds per veh to pass intersection
            # greenDur2 = max(vNumOther_S / 4 * 4 , E_needed_time) + vNumTurnLeft_N * 4
            greenDur1 = max(vNumOther_N / 4 * 4  + vNumTurnLeft_S * 4 , W_needed_time) # 4lanes, avg 4 seconds per veh to pass intersection
            greenDur2 = max(vNumOther_S / 4 * 4  + vNumTurnLeft_N * 4 , E_needed_time)
            
            greenDur = max(greenDur1, greenDur2)
            # print("calculated greenDur1: veh GS TR: ", vNumOther_N / 4 * 4, "  ped W_needed_time: ", W_needed_time, " veh TL: ", vNumTurnLeft_S* 4)
            # print("calculated greenDur2: veh GS TR: ", vNumOther_S / 4 * 4, "  ped E_needed_time: ", E_needed_time, " veh TL: ", vNumTurnLeft_N* 4)
            # print("calculated green dur: ", greenDur)
            traci.trafficlight.setPhaseDuration("centernode", float(greenDur))
        # calc green duration for WE
        elif phaseNoCurr == 2 and phaseNoPrevious == 1: 
            vNumTurnLeft_W, vNumOther_W = 0, 0
            vIDs = traci.edge.getLastStepVehicleIDs("W1")
            for vID in vIDs:
                routeID = traci.vehicle.getRouteID(vID)
                if routeID in ["N2E", "S2W", "E2S", "W2N"]: # if turn left
                    vNumTurnLeft_W += 1
                else:
                    vNumOther_W += 1

            vNumTurnLeft_E, vNumOther_E = 0, 0
            vIDs = traci.edge.getLastStepVehicleIDs("E1")
            for vID in vIDs:
                routeID = traci.vehicle.getRouteID(vID)
                if routeID in ["N2E", "S2W", "E2S", "W2N"]: # if turn left
                    vNumTurnLeft_E += 1
                else:
                    vNumOther_E += 1


            ped_direction2count, ped_direction2personID =  get_ped_direction2count()
            # N
            # PCS
            # Step 1: Modify parameters in global_params.py file. I have done it.
            # Step 2: Enable global params
            params = global_params.global_params()
            # Possible step 3:
            params.crosswalk_width = 640 #cm
            params.crosswalk_length = 4769 #cm
            params.waiting_area_width = params.crosswalk_width
            params.waiting_area_length = 300 #cm
            params.total_length = params.waiting_area_length * 2 + params.crosswalk_length
            params.outside_margin_width = 100 # cm
            params.waiting_area_position_x_offset_min = 0 - params.waiting_area_length
            params.waiting_area_position_x_offset_max = params.waiting_area_length
            params.waiting_area_position_x_offset_mean = 0 #coordinate
            params.waiting_area_position_x_offset_sigma = params.waiting_area_length / 2 # max = mean + 2*sigma
            params.waiting_area_position_y_min = 0
            params.waiting_area_position_y_max = params.crosswalk_width
            params.waiting_area_position_y_mean = params.crosswalk_width / 2 #coordinate
            params.waiting_area_position_y_sigma = params.crosswalk_width / 2 # max = mean + 2*sigma => sigma = (max - mean )/2

            params.ped_amount_lr = ped_direction2count["N_W2E"]
            params.ped_amount_rl = ped_direction2count["N_E2W"]
            # clean variables
            params.all_peds_lr = list() # all ped who want go from left to right
            params.all_peds_rl = list() # all ped who want go from right to left
            params.all_peds = list()  # all ped 
            params.all_peds_lr_sorted_by_x = list() # all sorted ped who want go from left to right, sorted by x reversed, biggest x first
            params.all_peds_rl_sorted_by_x = list() # all sorted ped who want go from right to left, sorted by x, smallest x first 
            params.all_peds_ordered = list()
            # Step 4: run simulation and get result
            BackendAPI.set_peds_initial_positions(params)
            BackendAPI.cross_street(params)
            N_needed_time = BackendAPI.get_ped_needed_time_to_cross(params)
            # print("N These pedestrains need ", N_needed_time, " seconds to cross the street.\n")
            # kill those persons (they have crossed in theory)
            kill_personobject(ped_direction2personID, "N_W2E", "N_E2W")

            # S
            # PCS
            # Step 1: Modify parameters in global_params.py file. I have done it.
            # Step 2: Enable global params
            params = global_params.global_params()
            # Possible step 3:
            params.crosswalk_width = 640 #cm
            params.crosswalk_length = 4769 #cm
            params.waiting_area_width = params.crosswalk_width
            params.waiting_area_length = 300 #cm
            params.total_length = params.waiting_area_length * 2 + params.crosswalk_length
            params.outside_margin_width = 100 # cm
            params.waiting_area_position_x_offset_min = 0 - params.waiting_area_length
            params.waiting_area_position_x_offset_max = params.waiting_area_length
            params.waiting_area_position_x_offset_mean = 0 #coordinate
            params.waiting_area_position_x_offset_sigma = params.waiting_area_length / 2 # max = mean + 2*sigma
            params.waiting_area_position_y_min = 0
            params.waiting_area_position_y_max = params.crosswalk_width
            params.waiting_area_position_y_mean = params.crosswalk_width / 2 #coordinate
            params.waiting_area_position_y_sigma = params.crosswalk_width / 2 # max = mean + 2*sigma => sigma = (max - mean )/2

            params.ped_amount_lr = ped_direction2count["S_W2E"]
            params.ped_amount_rl = ped_direction2count["S_E2W"]
            # clean variables
            params.all_peds_lr = list() # all ped who want go from left to right
            params.all_peds_rl = list() # all ped who want go from right to left
            params.all_peds = list()  # all ped 
            params.all_peds_lr_sorted_by_x = list() # all sorted ped who want go from left to right, sorted by x reversed, biggest x first
            params.all_peds_rl_sorted_by_x = list() # all sorted ped who want go from right to left, sorted by x, smallest x first 
            params.all_peds_ordered = list()
            # Step 4: run simulation and get result
            BackendAPI.set_peds_initial_positions(params)
            BackendAPI.cross_street(params)
            S_needed_time = BackendAPI.get_ped_needed_time_to_cross(params)
            # print("S These pedestrains need ", S_needed_time, " seconds to cross the street.\n")
            # kill those persons (they have crossed in theory)
            kill_personobject(ped_direction2personID, "S_W2E", "S_E2W")

            # greenDur1 = max(vNumOther_W / 4 * 4 , S_needed_time) + vNumTurnLeft_E * 4 # 4lanes, avg 4 seconds per veh to pass intersection
            # greenDur2 = max(vNumOther_E / 4 * 4 , N_needed_time) + vNumTurnLeft_W * 4
            greenDur1 = max(vNumOther_W / 4 * 4  + vNumTurnLeft_E * 4, S_needed_time) # 4lanes, avg 4 seconds per veh to pass intersection
            greenDur2 = max(vNumOther_E / 4 * 4  + vNumTurnLeft_W * 4, N_needed_time)
            greenDur = max(greenDur1, greenDur2)
            # print("calculated greenDur1: veh GS TR: ", vNumOther_W / 4 * 4, "  ped W_needed_time: ", S_needed_time, " veh TL: ", vNumTurnLeft_E* 4)
            # print("calculated greenDur2: veh GS TR: ", vNumOther_E / 4 * 4, "  ped E_needed_time: ", N_needed_time, " veh TL: ", vNumTurnLeft_W* 4)
            # print("calculated green dur: ", greenDur)
            traci.trafficlight.setPhaseDuration("centernode", float(greenDur))

        # if (phaseNoCurr == 0 and (phaseNoPrevious == 2 or phaseNoPrevious == 3) ) or (phaseNoCurr == 2 and phaseNoPrevious == 1):
            # print("getCompleteRedYellowGreenDefinition: ", traci.trafficlight.getCompleteRedYellowGreenDefinition("centernode") )
            # print("getPhaseDuration: ", traci.trafficlight.getPhaseDuration("centernode"), "\n")

        arrivedPersonCtr += traci.simulation.getArrivedPersonNumber()
        
        alivePersonIDList.extend( traci.simulation.getDepartedPersonIDList())
        arrivedPersonIDList = traci.simulation.getArrivedPersonIDList()
        alivePersonIDList = [personID for personID in alivePersonIDList if personID not in arrivedPersonIDList]

        for pID in alivePersonIDList:            
            if pID not in pedID2waitingTime:
                pedID2waitingTime[pID] = 0
            if traci.person.getSpeed(pID) <= 0.1: #m/s
                pedestrian_total_waited_time += 1
                pedID2waitingTime[pID] += 1


       
        step += 1
        phaseNoPrevious = phaseNoCurr

    print("step: ", step)
    print("arrivedPersonCtr: ", arrivedPersonCtr)
    print("pedestrian_total_waited_time: ", pedestrian_total_waited_time)
    print("pedestrian avg waited time: ", pedestrian_total_waited_time / arrivedPersonCtr, "\n")
    traci.close()
    sys.stdout.flush()
    return pedID2waitingTime


def calAvgWaitTime(tripinfo_output_filename):
    tree = ET.parse(tripinfo_output_filename) # get the file
    root = tree.getroot() # loc the root

    vCount = 0
    vWaitingTimeTotal = 0
    for tripinfo in root.findall('tripinfo'):
        vCount += 1
        vID = tripinfo.get('id')
        vType = tripinfo.get('vType')
        vDuration = tripinfo.get('duration')
        vRouteLength = tripinfo.get('routeLength')
        vWaitingTime = tripinfo.get('waitingTime')
        vWaitingCount = tripinfo.get('waitingCount')
        vWaitingTimeTotal += float(vWaitingTime)
        #print(vID)
        #print(vType)
        #print(vWaitingTime)

    CO_all = 0
    CO2_all = 0
    HC_all = 0
    PMx_all = 0
    NOx_all = 0
    fuel_all = 0
    eletricity_all = 0
    for tripinfo in root.findall('tripinfo'):
        CO_all += float( tripinfo.find('emissions').get('CO_abs'))
        CO2_all += float( tripinfo.find('emissions').get('CO2_abs'))
        HC_all += float( tripinfo.find('emissions').get('HC_abs'))
        PMx_all += float( tripinfo.find('emissions').get('PMx_abs'))
        NOx_all += float( tripinfo.find('emissions').get('NOx_abs'))
        fuel_all += float( tripinfo.find('emissions').get('fuel_abs'))
        eletricity_all += float( tripinfo.find('emissions').get('electricity_abs'))

    vWaitingTimeAvg = vWaitingTimeTotal / vCount
    print("vWaitingTimeTotal:", vWaitingTimeTotal)
    print("vCount:", vCount)
    print("CO_all: ", CO_all )
    print("CO2_all: ", CO2_all )
    print("HC_all: ", HC_all )
    print("PMx_all: ", PMx_all )
    print("NOx_all: ", NOx_all )
    print("total_car_exhausts: ", CO_all+CO2_all+HC_all+PMx_all+NOx_all )
    print("fuel_all: ", fuel_all )
    print("eletricity_all: ", eletricity_all )
    print("vWaitingTimeAvg:", vWaitingTimeAvg)


    pedCount = 0
    for tripinfo in root.findall('personinfo'):
        pedCount += 1
    print("\npedCount:", pedCount)
        


         


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options

# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    

    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
    print("date and time =", dt_string)	


    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    tripinfo_output_filename = "output/3rdexperiment.tripinfo." +dt_string+".xml"
    emission_output_filename = "output/3rdexperiment.emission." +dt_string+".xml"
    ped_waitingtime_output_filename = "output/3rdexperiment.ped_waitingtime." +dt_string+".xml"
    traci.start([sumoBinary, "-c", "dayuan.sumocfg",
                             "--tripinfo-output", tripinfo_output_filename,
                             "--emission-output", emission_output_filename])
    
    
    # implement my alg
    pedID2waitingTime = run()
    outfile = open(ped_waitingtime_output_filename,"w")
    outfile.write(str(  dict(sorted(pedID2waitingTime.items(), key=lambda item: item[1]))   ))#sort by value
    outfile.close()

    # calculate avg waiting time
    calAvgWaitTime(tripinfo_output_filename)
    print("Done!")
    
    