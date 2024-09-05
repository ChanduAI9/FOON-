import re

class FoonGraph:
    def __init__(self, foon_file):
        self.graph_data = self.load_foon(foon_file)

    def load_foon(self, foon_file):
        """Load and clean FOON file aggressively."""
        with open(foon_file, 'r') as f:
            lines = f.readlines()
        units = []
        current_unit = []
        for line in lines:
            line = re.sub(r'[^\w\s]', '', line).strip().lower()
            line = re.sub(r'\s+', ' ', line) 
            # print(f"Line loaded: '{line}'")  
            if line == '\\' or line == '':
                if current_unit:
                    units.append(current_unit)
                current_unit = []
            else:
                current_unit.append(line)
        return units

    def clean_text(self, text):
        """Aggressively clean and normalize text to eliminate any subtle differences."""
        return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', '', text).strip().lower())

    def log_comparison(self, goal, extracted, label):
        """Helper function to log comparisons of object and state."""
        print(f"\nComparing {label}:")
        print(f"Goal: '{goal}' | Extracted: '{extracted}'")
        print(f"Match: {goal == extracted}\n")

    def search_goal(self, goal_object, goal_state):
        """Search for functional units involving the goal object in the desired state."""
        result_units = []
        goal_object_clean = self.clean_text(goal_object)
        goal_state_clean = self.clean_text(goal_state)

        print(f"\nSearching for object: '{goal_object_clean}' with state: '{goal_state_clean}'")
        
        for unit in self.graph_data:
            object_match = False
            state_match = False
            for line in unit:
                parts = line.split()
                if line.startswith('o'):  
                    object_name = self.clean_text(parts[1])  
                    self.log_comparison(goal_object_clean, object_name, "Object")
                    if goal_object_clean == object_name:
                        object_match = True
                elif line.startswith('s'):  
                    state_value = self.clean_text(' '.join(parts[1:])) 
                    self.log_comparison(goal_state_clean, state_value, "State")
                    if goal_state_clean == state_value:
                        state_match = True

            if object_match and state_match:
                print(f"\nMatch found: {unit}")
                result_units.append(unit)

        if not result_units:
            print(f"\nNo matches found for '{goal_object_clean}' in state '{goal_state_clean}'.")

        return result_units

    def available_units(self, kitchen_file):
        """Check available kitchen items for matching functional units."""
        with open(kitchen_file, 'r') as f:
            kitchen_items = [self.clean_text(line.strip()) for line in f.readlines()]
        
        print(f"\nAvailable kitchen items: {kitchen_items}")

        result_units = []
        for unit in self.graph_data:
            input_objects = [line for line in unit if line.startswith('o')]
            
            
            ingredients_present = any(
                any(item in self.clean_text(obj.split()[1]) for item in kitchen_items) for obj in input_objects
            )
            
            if ingredients_present:
                print(f"\nMatching unit found: {unit}")
                result_units.append(unit)

        if not result_units:
            print("\nNo functional units found based on available kitchen items.")

        return result_units



if __name__ == "__main__":
    foon_graph = FoonGraph('foon_data.txt')


    goal_object = "onion"
    goal_state = "ring shaped"
    foon_graph.search_goal(goal_object, goal_state)

    
    foon_graph.available_units('kitchen_data.txt')
