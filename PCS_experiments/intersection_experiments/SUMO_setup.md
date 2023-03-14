# SUMO Set up

This file records how I set up the experiments.

## Step 1: Nodes

All nodes are set up in "```dayuan.nod.xml```" file. In this file, each node is assigned with its coordinates (x,y).

The definitions of the attributes in the node file are listed below.

- (a) id: the ID name of the node, defined by users with numbers, word strings or both.
- (b) x: the x-coordinate location of the defined node (in meters)
- (c) y: the y-coordinate location of the defined node (in meters)
- (d) type: the signal control type of the defined node. It is an optional attribute and defined with priority and traffic_light for unsignalized and signalized intersections respectively.

**Note**: Must add "type="traffic_light"" if want to use custom tlLogic file as input file in netccfg file.
```xml
<node id="centernode" x="0.0" y="0.0" type="traffic_light"/>
```

## Step 2: Edges (links)

All edges (road segments, or called "link" in SUMO) are set up in "```dayuan.edg.xml```" file.

The defined attributes include:

- (a) id: link ID, defined by users with numbers, word strings or both.
- (b) from: ID of the upstream node of the respective link.
- (c) to: ID of the downstream node of the respective link.
- (d) type: ID of the link type, defined in the link type file.
- (e) allow/disallow: ID of the vehicle group which is defined in the SUMO and might not be identical with the vehicle types defined by users.

The definiton of those types are set up in "```dayuan.typ.xml```" file.

Four attributes are defined:

- (a) id: defined by users with numbers, word strings or both.
- (b) priority: driving priority based on traffic regulations and is defined with numbers. The higher the number, the higher the priority for the respective road. The priority information will override information from the node file, if both of them exist.
- (c) numLanes: number of lanes on the respective road. **This doesn't count sidewalk lanes for ped.** So in our case it is still 4, even thought there are totally 5 lanes when write connections.
- (d) speed: maximum allowed link speed.
- **sidewalkWidth="a number"** are necessary to make netconvert to generate a pedestrian side walk among lanes for vehicles.
- **disallow="pedestrian"** is used to make sure no ped will walk on vehicle lanes. 



## Step 3: Connections between lanes

Since each edge has 4 lanes, they can not connect to each other freely. The connection between each lanes are set up in "```dayuan.con.xml```" file.

Specially when there are ped sidewalk existing, it is also counted as a lane. So there are **5 lanes** actually for each edge.

Note: lane number count from right hand, i.e. the right most lane is lane 0, the left most lane in our case is lane 4. **The lane 0 is side walk for ped only. The lane 1-4 are for vehicles only**, in our case, by using "disallow="pedestrian"" in above edge type file. 

When we write connections in con.xml file, we only need to connect lanes for vehicles. This is why the fromLane and toLane have only 1~4 in our con.xml file.

The meaning of each attribute is as following:

- (a) from: ID of the link which the traffic movements will be specified.
- (b) to: ID of the link which is the downstream link of the above defined link.
- (c) fromLane/toLane: lane number of the defined link in (a) and the lane number of the link in (b), which are connected.

## Step 4: Add Crosswalks

Add crosswalks by hand at the end of connection file "```dayuan.con.xml```". They are bidirectional.

- node:	id (string)	The name of the node at which this crossing is located
- edges:	ids (list of strings)	The (road) edges which are crossed
- priority:	bool	Whether the pedestrians have priority over the vehicles (automatically set to true at tls-controlled intersections).
- width:	real (m)	The width of the crossings.
- shape:	List of positions; each position is encoded in x,y or x,y,z in meters (do not separate the numbers with a space!).	specifies a custom shape for this crossing. By default it is straight. Caution: The shape must be defined in counter-clockwise direction around the intersection.
- linkIndex:	int	specifies a custom index within the signal plan (for the forward direction)
- linkIndex2:	int	specifies a custom index within the signal plan (for the backward direction)
- discard:	bool	Whether the crossing with the given edges shall be discarded. If discard is set to true omitting the edges attribute results in discarding all crossings.



## Step 5: Custom tlLogic file

I create my custom tlLogic file "```dayuan.tllogic.xml```" to follow the real traffic lights logic in  real world.

### \<tlLogic\> Attributes

- **id**	id (string)	The id of the traffic light. This must be an existing traffic light id in the .net.xml file. Typically the id for a traffic light is identical with the junction id. The name may be obtained by right-clicking the red/green bars in front of a controlled intersection. **This id must be node's id.**
- **type**	enum (static, actuated, delay_based)	The type of the traffic light (fixed phase durations, phase prolongation based on time gaps between vehicles (actuated), or on accumulated time loss of queued vehicles (delay_based) )
- **programID**	id (string)	The id of the traffic light program; This must be a new program name for the traffic light id. Please note that "off" is reserved, see below.
- **offset**	int	The initial time offset of the program


### \<phase\> Attributes

- **duration**	time (int)	The duration of the phase
- **state**	list of signal states	The traffic light states for this phase. **The len(state) muse eqaul to *len(connection) in con.xml*.** To check len(connections) you can count \<connection\> in con.xml file, or see it when SUMO-GUI open net.xml file with "show link junction index" checked. **The last 4 bits are crosswalks signals.**
- **minDur**	time (int)	The minimum duration of the phase when using type actuated. Optional, defaults to duration.
- **maxDur**	time (int)	The maximum duration of the phase when using type actuated. Optional, defaults to duration.
- **name**	string	An optional description for the phase. This can be used to establish the correspondence between SUMO-phase-indexing and traffic engineering phase names.
- **next**	list of phase indices (int ...)	The next phase in the cycle after the current. This is useful when adding extra transition phases to a traffic light plan which are not part of every cycle. Traffic lights of type 'actuated' can make use of a list of indices for selecting among alternative successor phases.



## Step 6: Network generation (use netconvert)

All 5 files above will be used as input to generate the network file "```dayuan.net.xml```" using ```netconvert``` command.

Before that, let set up all parameters into 1 file "```dayuan.netccfg```" since there are too much parameters.

In this parameter file "```dayuan.netccfg```", we will set ```"dayuan.nod.xml", "dayuan.edg.xml", "dayuan.typ.xml", "dayuan.con.xml", "dayuan.tllogic.xml"``` all 5 above files as input files. And then set a out put file, which is our network file "```dayuan.net.xml```".

As shown in SUMO project files structure: 
![](https://github.com/DayuanTan/SUMO_dt_public/blob/master/dayuan/imgs/structure.gif)

BTW, If u-turn movements are not allowed, the command ```<no-turnarounds value="true"/>``` should be added to the configuration file. The prohibition of u-turn movements can only be conducted globally.

I also set --sidewalks.guess Ture to ask it generate sidewalks. 


Run ```netconvert -c dayuan.netccfg``` to generate file "```dayuan.net.xml```".
```python
roadnet$ netconvert -c dayuan.netccfg
Loading configuration ... done.
Parsing types from 'dayuan.typ.xml' ... done.
Parsing nodes from 'dayuan.nod.xml' ... done.
Parsing edges from 'dayuan.edg.xml' ... done.
Parsing connections from 'dayuan.con.xml' ... done.
Parsing traffic lights from 'dayuan.tllogic.xml' ... done.
 Import done:
   5 nodes loaded.
   1 types loaded.
   8 edges loaded.
Removing self-loops ... done (0ms).
Removing empty nodes ... done (1ms).
   0 nodes removed.
Moving network to origin ... done (0ms).
Computing turning directions ... done (0ms).
Assigning nodes to traffic lights ... done (0ms).
Sorting nodes' edges ... done (0ms).
Computing node shapes ... done (1ms).
Computing edge shapes ... done (0ms).
Computing node types ... done (0ms).
Computing priorities ... done (0ms).
Computing approached edges ... done (0ms).
Guessing and setting roundabouts ... done (0ms).
Computing approaching lanes ... done (0ms).
Dividing of lanes on approached lanes ... done (0ms).
Processing turnarounds ... done (0ms).
Rechecking of lane endings ... done (0ms).
Computing traffic light control information ... done (0ms).
Computing node logics ... done (1ms).
Computing traffic light logics ... done (0ms).
 1 traffic light(s) computed.
Building inner edges ... done (1ms).
-----------------------------------------------------
Summary:
 Node type statistics:
  Unregulated junctions       : 0
  Dead-end junctions          : 4
  Priority junctions          : 0
  Right-before-left junctions : 0
  Traffic light junctions      : 1
 Network boundaries:
  Original boundary  : -200.00,-200.00,200.00,200.00
  Applied offset     : 200.00,200.00
  Converted boundary : 0.00,0.00,400.00,400.00
-----------------------------------------------------
Writing network ... done (3ms).
Success.
```

This will generate a default tlLogic in ```dayuan.net.xml``` file.  

This command can be used to show the roadnet if want:
```linux
roadnet$ sumo-gui dayuan.net.xml
``` 




## Step 7: Traffic demand

Then I set up traffic flow information into "```dayuan.rou.xml```".

To reproduce the **real traffic flow in real world**. The traffic demand follows the [real wordl filed study records](../raw_data/README.md). 

**Firstly** I define 2 types of cars. 

For vehicle types, I just used default value of each types (https://sumo.dlr.de/docs/Vehicle_Type_Parameter_Defaults.html).

- All small vehicles use "passenger" vtype in SUMO.
- All big vehicles use "bus" vtype in SUMO.

How we category vehicles are defined in [raw data record](../raw_data/README.md#vehicle-types).



**Secondly** 12 routes are assigned to let each vehicle to select from.

Following the vehicle type information traffic route data need to be defined as well. The input attributes include:

- (a) ***id***: ID of a certain route and defined by users with numbers, word strings or both.
- (b) ***edges***: The sequence of the names of the links, composing the defined route.


**Thirdly** it's the traffic flow (traffic demand) design (**vehicles** only). 

I used python file [roadnet/py4rouFile/py2genRouFile.py](roadnet/py4rouFile/py2genRouFile.py) to read from [../raw_data/0826_7pm_vehicles_N_ped_count_colored.xlsx](../raw_data/0826_7pm_vehicles_N_ped_count_colored.xlsx) and write into [roadnet/py4rouFile/py4rouFile.txt](roadnet/py4rouFile/py4rouFile.txt). Then I copied contents of roadnet/py4rouFile.txt into [```roadnet/dayuan.rou.xml```](roadnet/dayuan.rou.xml).


The 1st cycle 1 phase starts at 52 second  as real world records. 

Vehicles starting points are at the dead end of each edge. So we start those vehicles before their correspoding green light phase to make sure when turning to their correspoding green light phase, they are aleready waiting just before the intersection. They depart one per second during the 2 phase before their correspoding green light phase.


Traffic demand data are defined with four attributes:

- (a) ***depart***: departure time of a certain vehicle.
- (b) ***id***: ID of a certain vehicle and defined by users with numbers, word strings or both.
- (c) ***route***: the route used by the defined vehicle;
- (d) ***type***: ID of the defined vehicle type.

**Fourthly** I define the traffic demand for **pedestrians**.


I used python file [roadnet/py4rouFile/py2genPedTripFile.py](roadnet/py4rouFile/py2genPedTripFile.py) to read from [../raw_data/0826_7pm_vehicles_N_ped_count_colored.xlsx](../raw_data/0826_7pm_vehicles_N_ped_count_colored.xlsx) and write into [roadnet/py4rouFile/py4PedTripFile.txt](roadnet/py4rouFile/py4PedTripFile.txt). Then I copied contents of roadnet/py4rouFile.txt into [```roadnet/dayuan.ped.trip.xml```](roadnet/dayuan.ped.trip.xml).

All pedestrians just start when their correspoding green light phase starts since their starting and stoping point are just at the margin of the crosswalk. 

###  \<person\> attributes
- **id**	string	valid XML ids	-	
- **depart**	float(s)	≥0 or 'triggered'	-	See ride for an explanation of 'triggered'
- **departPos**	float(s)	≥0	-	the distance along the edge that the person is created
- **type**	string	any declared vType	DEFAULT_PEDTYPE	the type should have vClass pedestrian
- **width**	float (s)	≥0	0,48	The person's width [m]
- **lenght**	float (s)	≥0	0,21	The person's netto-length (length) (in m)
- **mingap**	float (s)	≥0	0,25	Empty space after leader [m]
- **maxSpeed**	float (s)	≥0	1,39	The person's maximum velocity (in m/s)
- **jmDriveAfterRedTime**	float (s)	≥0	-1	This value causes persons to violate a red light if the duration of the red phase is lower than the given threshold. When set to 0, persons will always walk at yellow but will try to stop at red. If this behavior causes a person to walk so fast that stopping is not possible any more it will not attempt to stop.

### \<walk\> attributes
- **route**	string	valid route id	-	the id of the route to walk
- **edges**	list	valid edge ids	-	id of the edges to walk
- **from**	string	valid edge ids	-	id of the start edge (optional, if it is a subsequent movement)
- **to**	string	valid edge ids	-	id of the destination edge
- **busStop**	string	valid bus stop ids	-	id of the destination stop
- **duration**	float(s)	>0	-	override walk duration (otherwise determined by the person type and the pedestrian dynamics)
- **speed**	float(m/s)	>0	-	override walking speed (otherwise determined by the person type and individual speed factor)
- **arrivalPos**	float(m)		middle of edge	arrival position on the destination edge
- **departPosLat**	float(m)		right side in walking direction	custom lateral position on lane at departure


## Step 8: Run

<img src="https://github.com/DayuanTan/SUMO_dt_public/blob/master/dayuan/imgs/2nd/4.gif" />

Then I set up some configurations for running into file "```dayuan.sumocfg```", including 
- net-file "```dayuan.net.xml```", 
- route-files "```dayuan.rou.xml```" and 
- gui-settings-file "```dayuan.viewsettings.xml```".

After having all above, we can run the simulation using this command 
```
intersection_experiments$ sumo-gui -c dayuan.sumocfg
``` 

Usually we write a python file to run it. See [README.md](README.md).