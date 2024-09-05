# FOON Search Project

This project is designed to load, search, and visualize data from a **Functional Object-Oriented Network (FOON)** graph. FOON represents the relationships between kitchen objects, their states, and the manipulations that change their states. The project allows users to search for specific objects and states, check the functionality of available kitchen items, and visualize these processes as a graph.

## Features

- **Load FOON Data**: The project loads FOON data, which represents functional units of kitchen objects and manipulations.
- **Goal Search**: Allows you to search for a specific object and its state within the FOON data (e.g., "onion" in the "ring-shaped" state).
- **Kitchen Items Search**: Checks available kitchen items and finds functional units that can be executed based on the items available in the kitchen.
- **Graph Visualization**: Converts FOON data into a graph that can be visualized using graph libraries.

## Project Structure

```
.
├── foon_search.py           # Main FOON search logic and functionality
├── test_script.py           # Test script for searching goals and available units
├── graph_vis.py             # Script for graph visualization
├── foon_data.txt            # FOON data representing functional units (example)
├── kitchen_data.txt         # Kitchen data listing available items (example)
└── README.md                # Project documentation
```

## Prerequisites

- **Python 3.x**
- Python libraries:
  - `networkx` for graph visualization
  - `matplotlib` for plotting graphs
  - (optional) Any graph rendering tools such as `graphviz` for visual outputs

### Install required dependencies:

```bash
pip install networkx matplotlib
```

## Usage

1. **FOON Data and Kitchen Data**:
   - You can input your own FOON data and kitchen data by formatting them as shown below.

### FOON Data Example (foon_data.txt)

```
o onion
s whole
o knife
m chop
o onion
s ring shaped
\
o bowl
s empty
o wheat flour
s in cup
m pour
o bowl
s contains wheat flour
\
```

### Kitchen Data Example (kitchen_data.txt)

```
onion
knife
bowl
water
butter
```

2. **Running the Project**:

   - To search for a goal object and its state, run the following command:

   ```bash
   python foon_search.py
   ```

   - To test the functionality of available kitchen items, run:

   ```bash
   python test_script.py
   ```

3. **Graph Visualization**:
   - The `graph_vis.py` script converts the FOON data into a graph structure and visualizes it. Run the script:

   ```bash
   python graph_vis.py
   ```

## How It Works

### FOON Search:

- **Goal Search**: The project searches for a functional unit containing the desired object and its state. For example, searching for an "onion" in the "ring-shaped" state will return the functional unit describing how to chop the onion.
  
- **Available Kitchen Items**: The system checks the kitchen items listed in `kitchen_data.txt` and determines which functional units can be executed with the available items.

### Graph Visualization:

- The project builds a directed graph where nodes represent kitchen objects and manipulations, and edges represent transformations (e.g., "chop" transforms an "onion" from "whole" to "ring-shaped"). This graph can then be visualized.

## Example Output

For the following FOON data:

```
o onion
s whole
o knife
m chop
o onion
s ring shaped
```

The search for "onion" in "ring-shaped" state will output:

```
Functional Units for Goal (onion, ring shaped):
['o onion', 's whole', 'o knife', 'm chop', 'o onion', 's ring shaped', 'o knife']
```

Algorithm:

Explanation of FOON Functional Units:
The first functional unit describes chopping an onion into a ring-shaped state:
Input: An onion in a "whole" state and a knife.
Manipulation: "chop" the onion using the knife.
Output: An onion in a "ring-shaped" state.

The second functional unit describes pouring wheat flour into a bowl:
Input: A bowl that is "empty" and wheat flour "in a cup."
Manipulation: "pour" the flour into the bowl.
Output: A bowl that "contains wheat flour."


Loading FOON Data:
The FoonGraph class loads the functional units into memory using the load_foon() method. It reads the file line by line, cleans it (removes extra spaces and non-alphanumeric characters), and then organizes the data into "units." Each unit is a functional sequence representing an action (like chopping or pouring).

Searching for a Goal:
The search_goal() function takes a goal object and state as input (e.g., "onion" and "ring shaped"). It iterates through each functional unit to check if the specified object and state are present in the functional unit.

Comparing Objects and States:
For each line that starts with o (object) or s (state), the function compares the goal object and goal state with the ones in the FOON data. If both the object and state match, it identifies this functional unit as relevant to the goal.

Example Execution of search_goal():
If you search for the goal "onion" in the state "ring shaped", the function will:

Find the first occurrence of the object "onion" in the "whole" state, but this does not match the goal state, so it moves on.
Continue until it finds an object "onion" in the "ring shaped" state. Since both the object and the state match, it identifies this functional unit as a match and returns it.


#Searching for Functional Units Based on Available Kitchen Items:
The available_units() method checks which functional units can be executed based on the items available in the kitchen.

It reads the kitchen items from the file (kitchen_data.txt) and compares them with the objects (lines starting with o) in each functional unit.
If all required objects for a functional unit are available in the kitchen, that functional unit is identified as executable.
