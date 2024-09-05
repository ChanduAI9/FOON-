import foon_search
import graph_vis

#goal states
def test_goal_search():
    foon_graph = foon_search.FoonGraph('foon_data.txt')
    
    goal_object = "onion"
    goal_state = "ring shaped"
    
    goal_units = foon_graph.search_goal(goal_object, goal_state)
    
    print(f"\nFunctional Units for Goal ({goal_object}, {goal_state}):")
    for unit in goal_units:
        print(unit)
        print('---')

#Available units for
def test_available_units():
    foon_graph = foon_search.FoonGraph('foon_data.txt')
    
    available_units = foon_graph.available_units('kitchen_data.txt')
    
    print("\nFunctional Units for Available Kitchen Items:")
    for unit in available_units:
        print(unit)
        print('---')


#Graph
def test_graph_conversion():
    foon_graph = foon_search.FoonGraph('foon_data.txt')
    
    graph_data = graph_vis.foon_to_graph(foon_graph.graph_data)
    
    print("\nGraph Data:")
    print(graph_data)

    graph_vis.visualize_graph(graph_data)

if __name__ == "__main__":
    # Run the test functions
    test_goal_search()
    test_available_units()
    test_graph_conversion()
