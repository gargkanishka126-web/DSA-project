# Smart Delivery Route Optimization System

## Project Overview
This Python program represents delivery locations as a graph. It uses
Dijkstra's algorithm to find shortest paths and a greedy strategy to
schedule deliveries. It can also display the planned route on a map.

## Project Files
- `00_main.py` — Runs the program and displays the menu
- `graph.py` — Stores locations and roads and finds shortest paths
- `scheduler.py` — Creates a delivery schedule
- `visualization.py` — Displays the delivery route on a map
- `benchmark.py` — Measures runtime for different graph sizes
- `data/` — Contains sample map and delivery data
- `tests/` — Contains graph and scheduler tests
- `screenshots/` — Stores screenshots of program output

## Requirements
- Python 3
- matplotlib

Install matplotlib with:

    pip install matplotlib

## How to Run
Open a terminal in the project folder and run:

    python main.py

## Menu Options
- `1` — Show locations and roads
- `2` — Find the shortest path between two locations
- `3` — Create a delivery schedule
- `4` — Display the route map
- `0` — Exit the program

## Algorithms
- Dijkstra's algorithm finds the shortest path.
- A greedy nearest-delivery strategy chooses the next delivery stop.
- Python's `heapq` module helps Dijkstra's algorithm select the
  location with the smallest known distance.

## Assumptions
- Roads are two-way.
- Road distances are non-negative and measured in kilometers.
- The greedy scheduler chooses the nearest pending delivery from the
  current location. This is a practical heuristic and does not guarantee
  the globally shortest route for every set of deliveries.

## Screenshots
Save screenshots of the menu, shortest-path result, delivery schedule,
route map, and benchmark output in the `screenshots/` folder.