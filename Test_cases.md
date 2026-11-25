## Test Cases 

TC-01: Display locations and roads 

Input:Choose menu option 1.  
Expected result:The program lists all locations and their connected roads.  
Actual result:Depot, Market, School, Clinic, Library, Warehouse, and their connected roads were displayed.  
Status:Pass


TC-02: Find shortest path  

Input:Choose option 2- enter `Depot` as the starting location and `Market` as the destination.  
Expected result:The program displays the shortest route and its distance.  
Actual result:The shortest path was `Depot → Market`, with a distance of `4.00 km`.  
Status:Pass


TC-03: Create delivery schedule

Input:Choose option 3 with the sample deliveries.  
Expected result:The program displays the route, total distance, estimated travel time, completed deliveries, and unreachable deliveries.  
Actual result:The route was `Depot → Market → Clinic → Library → Warehouse`. The total distance was `14.00 km`, estimated travel time was `0.47 hours`, four deliveries were completed, and none were unreachable.  
Status:Pass


TC-04: Display route map  

Input:Choose menu option 4.  
Expected result:The program displays the locations and highlights the optimized route.  
Actual result:The map was displayed, and the optimized route was highlighted in red.  
Status:Pass


TC-05: Benchmark shortest paths

Input:Choose menu option 5.  
Expected result:The program reports the number of locations and the average execution time.  
Actual result:The benchmark reported 6 locations, 100 runs, and an average shortest-path time of `0.00001867 seconds`.  
Status:Pass


TC-06: Exit program  

Input:Choose menu option 6.  
Expected result:The program displays a goodbye message and closes normally.  
Actual result:“Goodbye!” was displayed, and the process finished with exit code 0.  
Status:Pass


TC-07: Unknown starting location 

Input:Choose option 2- enter `depot` as the starting location and `clinic` as the destination.  
Expected result:The program reports the unknown location without crashing.  
Actual result:The program displayed `Unknown starting location: depot`.  
Status:Pass


TC-08: Disconnected delivery location

Input:Add `Island` as a location and delivery without connecting it to a road; then choose option 3.  
Expected result:The program reports `Island` as unreachable.  
Actual result:Four connected deliveries were completed, and `Island` appeared under unreachable deliveries.  
Status:Pass

TC-9: Empty delivery list

Input:Use an empty delivery list and choose option 3.  
Expected result:The route contains only the depot; distance and travel time are zero; no deliveries are completed or unreachable.  
Actual result:The route was `Depot`, the distance was `0.00 km`, the estimated travel time was `0.00 hours`, and both delivery lists were empty.  
Status:Pass