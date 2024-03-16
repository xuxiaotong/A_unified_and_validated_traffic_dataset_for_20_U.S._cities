import pandas as pd
import numpy as np
import geopandas as gpd

from aequilibrae.matrix import AequilibraeMatrix
from aequilibrae.paths import Graph
from aequilibrae.paths import TrafficAssignment
from aequilibrae.paths.traffic_class import TrafficClass


########   step 1:  identify the city and input file path       #############
city_No = '01'
city =  'San_Francisco'
city_path = city_No + '_' + city
AE_path = city_path + '/' + '03_AequilibraE_results'


########   step 2:  define the od matrix file and generate od index      #############
aemfile = AE_path + '/' + 'od_demand.aem'

od_data = pd.read_csv(city_path + '/' + '01_Input_data' + '/' + city + '_od.csv')
zones = int(max(od_data.O_ID.max() - 9999999, od_data.D_ID.max() - 9999999))
index = np.arange(zones) + 1


#######   step 3: define the trafffic assignment paramters    #####
connector_speed = 5
road_1_capacity = 6600  # 3 lanes in total, 2200 veh/h for each lane
road_1_speed = 90       # free flow speed (km/h)
road_2_capacity = 4000  # 2 lanes in total, 2000 veh/h for each lane
road_2_speed = 60
road_3_capacity = 1400  #  1400 veh/h for one lane
road_3_speed = 40
alpha = 0.5      #  alpha in BPR function
beta = 1.8       #  beta in BPR function
od_multiplier = 0.6


########   step 4:  select the initial network shapefile path      #############
net = gpd.read_file(AE_path + '/'+ city + '.shp')
net.drop('geometry', axis=1, inplace=True)
net.columns = ["ID", "DIR", "length", "LINK_ID", "a_node", "b_node", "capacity", "LENGTH1", "speed", "Lanes", "link_type"]


########   step 5:  modify the parameters for traffic assignment    #############

########### connector ##############
net.loc[net['link_type'] > 10, 'speed'] = connector_speed

########### road class 1 ##############
net.loc[net['link_type'].isin([1, 2]), 'capacity'] = road_1_capacity
net.loc[net['link_type'].isin([1, 2]), 'speed'] = road_1_speed

########### road class 2 ##############
net.loc[net['link_type'] == 3, 'capacity'] = road_2_capacity
net.loc[net['link_type'] == 3, 'speed'] = road_2_speed

########### road class 3 ##############
net.loc[net['link_type'].isin([4, 5]), 'capacity'] = road_3_capacity
net.loc[net['link_type'].isin([4, 5]), 'speed'] = road_3_speed

########### BPR function ##############
net['free_flow_time'] = net['length'] / net['speed'] * 60
net['a'] = alpha
net['b'] = beta

########### organize the network data fields ##############
network = net[['a_node', 'b_node', "capacity", 'free_flow_time', "a", "b"]]
network = network.assign(direction=1)
network["link_id"] = network.index + 1
network = network.astype({"a_node": "int64", "b_node": "int64"})



########### step 6: conduct the traffic assignment in AE ##############
g = Graph()
g.cost = network['free_flow_time'].values
g.capacity = network['capacity'].values
g.free_flow_time = network['free_flow_time'].values

g.network = network
g.network_ok = True
g.status = 'OK'
g.prepare_graph(index)
g.set_graph("free_flow_time")
g.cost = np.array(g.cost, copy=True)
g.set_skimming(["free_flow_time"])
g.set_blocked_centroid_flows(False)
g.network["id"] = g.network.link_id

aem = AequilibraeMatrix()
aem.load(aemfile)
aem.computational_view(["matrix"])

assigclass = TrafficClass("car", g, aem)

assig = TrafficAssignment()

assig.set_classes([assigclass])
assig.set_vdf("BPR")
assig.set_vdf_parameters({"alpha": "a", "beta": "b"})
assig.set_capacity_field("capacity")
assig.set_time_field("free_flow_time")
assig.set_algorithm("bfw")
assig.max_iter = 500
assig.rgap_target = 0.001
assig.execute()


########### step 7: save the output ##############
network.to_csv(AE_path + '\\' + 'network.csv')
assig.results().to_csv(AE_path+ '\\' + 'assignment_result.csv')
