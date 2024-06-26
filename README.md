# Table of Contents
- [Introduction](#introduction)
- [About the dataset](#about-the-dataset)
  - [Data contents](#data-contents)
  - [20 U.S. cities](#20-us-cities)
  - [Dataset usage](#dataset-usage)
- [Publication](#publication)
- [Contact](#contact)


# Introduction
This is an introduction about a unified and validated traffic dataset for 20 U.S. cities. The input data were all collected and processed from multi-source open public datasets. We applied two traffic modelling platforms ([TransCAD](https://www.caliper.com/tcovu.htm) and [AequilibraE](http://www.aequilibrae.com/python/latest/index.html)) simultaneously to obtain the final results.



# About the dataset

## Data contents
- 01 Input data
  - the initial network data obtained from [OpenStreetMap](https://www.openstreetmap.org/) (OSM)
  - the visualization of the OSM data
  - processed node/link/od data
  
  A brief demonstration about the input data is provided [here](https://github.com/xuxiaotong/A_unified_and_validated_traffic_dataset_of_20_U.S._cities/blob/main/Input%20data%20introduction.ipynb).

- 02 TransCAD results (software version: 9.0)
  - cityname.dbd : geographical network database of the city supported by **TransCAD (version 9.0)**
  - cityname_link.shp / cityname_node.shp : network data supported by GIS software, which can be imported into TransCAD manually. Then the corresponding '.dbd' file can be generated for **TransCAD with a lower version than 9.0**
  - od.mtx : OD matrix supported by TransCAD
  - LinkFlows.bin / LinkFlows.csv : traffic assignment results by TransCAD
  - ShortestPath.mtx / ue_travel_time.csv : the travel time (min) between OD pairs by TransCAD

  A guide for TransCAD users who want to get access to the results is provided [here](https://github.com/xuxiaotong/A_unified_and_validated_traffic_dataset_of_20_U.S._cities/blob/main/A%20guide%20for%20TransCAD%20users.md). 

- 03 AequilibraE results (software version: 0.9.3)
  - cityname.shp : shapefile network data of the city support by [QGIS](https://www.qgis.org/en/site/) or other GIS software
  - od_demand.aem : OD matrix supported by AequilibraE
  - network.csv : the network file uesed for traffic assignment in AequilibraE
  - assignment_result.csv : traffic assignment results by AequilibraE

  A python code file for AequilibraE users who want to get access to the results is provided [here](https://github.com/xuxiaotong/A_unified_and_validated_traffic_assignment_dataset_of_20_U.S._cities/blob/main/AequilibraE_assignment.py). 



## 20 U.S. cities
The 20 U.S. cities included in this dataset are listed below.

| No. |City           |State          |TAZs  |Nodes  |Links  |
|:----|:--------------|:--------------|:-----|:------|:------|
| 1   | San Francisco |  California   | 194  | 4986  | 18002 |
| 2   | Seattle       |  Washington   | 139  | 6891  | 27361 |
| 3   | Portland      |  Oregon       | 157  | 8245  | 31939 |
| 4   | Las Vegas     |  Nevada       | 175  | 7823  | 28831 |
| 5   | Chicago       |  Illinois     | 819  | 14434 | 54469 |
| 6   | New Orleans   |  Louisiana    | 185  | 7217  | 24073 |
| 7   | Austin        |  Texas        | 199  | 10717 | 40158 |
| 8   | Minneapolis   | Minnesota     | 130  | 4004  | 15363 |
| 9   | Dallas        | Texas         | 328  | 21389 | 77818 |
| 10  | Milwaukee         | Wisconsin | 234  | 8521  | 30747 |
| 11  | New York City     | New York  | 2005 | 28626 | 99410 |
| 12  | Washington    |  District of Columbia | 179  | 6136  | 23573 |
| 13  | Boston        |  Massachusetts        | 191  | 5542  | 20487 |
| 14  | Philadelphia  |  Pennsylvania         | 389  | 10410 | 38641 |
| 15  | Pittsburgh    |  Pennsylvania         | 149  | 3532  | 13662 |
| 16  | Miami         |  Florida              | 108  | 4121  | 15108 |
| 17  | Atlanta       | Georgia               | 141  | 5207  | 20243 |
| 18  | Phoenix       | Arizona               | 378  | 15324 | 58070 |
| 19  | Denver        |  Colorado             | 175  | 9205  | 34724 |
| 20  | Honolulu      |  Hawaii               | 117  | 2982  | 11205 |



## Dataset usage
**Download:**
[A unified and validated traffic dataset for 20 U.S. cities](https://doi.org/10.6084/m9.figshare.24235696)

**Citation:**
Xu, Xiaotong; Zheng, Zhenjie; Hu, Zijian; Feng, Kairui; Ma, Wei (2023). A unified and validated traffic dataset for 20 U.S. cities. figshare. Dataset. https://doi.org/10.6084/m9.figshare.24235696

**Note:**
More detailed illustration for compiling the traffic dataset can be referred to [GitHub code](https://github.com/kelvinfkr/Unified_UE_US_cities/blob/main/Illustrative_unified_dataset_traffic_assignment.ipynb) or [Colab code](https://colab.research.google.com/drive/19iGXJAHx5_vvoZMbOmbBXdTwxzVogB2V?usp=sharing)

# Publication
Xu, X., Zheng, Z., Hu, Z. et al. A unified dataset for the city-scale traffic assignment model in 20 U.S. cities. Sci Data 11, 325 (2024). https://doi.org/10.1038/s41597-024-03149-8

# Contact
Xiaotong Xu: kid-a.xu@connect.polyu.hk
