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



def run():
    """execute the TraCI control loop"""
    step = 0
    arrivedPersonCtr = 0
    alivePersonIDList = list()
    pedestrian_total_waited_time = 0
    pedID2waitingTime = dict()

    #while traci.simulation.getTime() <209:#unit is s. Set a short time for testing
    while traci.simulation.getMinExpectedNumber() > 0 : # run until all v and ped have arrived. 
        traci.simulationStep() # forward one step

        # first 52 s set as red light so no car pass intersection.
        if step < 52:
            traci.trafficlight.setPhase("centernode", 2)
        # Start the first phase in first cycle at 52 s, following real world
        if step == 52:
            traci.trafficlight.setPhase("centernode", 0) 

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
    tripinfo_output_filename = "output/1stexperiment.tripinfo." +dt_string+".xml"
    emission_output_filename = "output/1stexperiment.emission." +dt_string+".xml"
    ped_waitingtime_output_filename = "output/1stexperiment.ped_waitingtime." +dt_string+".xml"
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
    
    