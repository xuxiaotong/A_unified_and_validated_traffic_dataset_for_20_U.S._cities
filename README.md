# Table of Contents
- [Introduction](#introduction)
- [About the dataset](#about-the-dataset)
  - [Data contents](#data-contents)
  - [20 U.S. Cities](#20-us-cities)
  - [Dataset usage](#dataset-usage)
- [Publication](#publication)
- [Contact](#contact)


# Introduction
This is an introduction about a unified and validated traffic assignmnet dataset for 20 U.S. cities. The input data were all collected and processed from multi-source open public datasets. We applied two traffic modelling platforms ([TransCAD](https://www.caliper.com/tcovu.htm) and [AequilibraE](http://www.aequilibrae.com/python/latest/index.html)) simultaneously to obtain the final results.



# About the dataset

## Data contents
- 01 input data
  - the initial network data obtained from [OpenStreetMap](https://www.openstreetmap.org/) (OSM)
  - the visualization of the OSM data
  - processed node data
  - processed link data
  - processed od data
  
  A brief demonstration about the input data is provided [here](https://github.com/xuxiaotong/A_unified_traffic_assignment_dataset_of_20_U.S._cities/blob/main/input%20data%20introduction.ipynb).

- 02 TransCAD results (software version: 9.0)
  - cityname.dbd : geographical network database of the city supported by TransCAD
  - od.mtx : OD matrix supported by TransCAD
  - LinkFlows.bin / LinkFlows.csv : traffic assignment results by TransCAD
  - ShortestPath.mtx / ue_travel_time.csv : the traval time (min) between OD pairs by TransCAD

  A guide for TransCAD users who want to get access to the results is provided [here](https://github.com/xuxiaotong/A_unified_traffic_assignment_dataset_of_20_U.S._cities/blob/main/A%20Guide%20for%20TransCAD%20Users.md). 

- 03 AequilibraE results (software version: 0.9.3)
  - cityname.shp : shapefile network data of the city support by [QGIS](https://www.qgis.org/en/site/) or other GIS software
  - od_demand.aem : OD matrix supported by AequilibraE
  - network.csv : the network file uesed for traffic assignment in AequilibraE
  - assignment_result.csv : traffic assignment results by AequilibraE

  A python code file for AequilibraE users who want to get access to the results is provided [here](). 



## 20 U.S. Cities
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
| 9   | Dallas-Fort Worth | Texas     | 328  | 21389 | 77818 |
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
Download: [A unified traffic assignment dataset for 20 U.S. cities](https://figshare.com/s/6987aceb18cf029edc66)


Citation: Xu, Xiaotong; Zheng, Zhenjie; Hu, Zijian; Feng, Kairui; Ma, Wei (2023). A unified and validated traffic assignment dataset for 20 U.S. cities.rar. figshare. Dataset. https://doi.org/10.6084/m9.figshare.24235696



# Publication

# Contact
Xiaotong Xu: kid-a.xu@connect.polyu.hk
