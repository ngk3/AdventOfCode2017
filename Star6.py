
# Function used to search for the highest value given the conditions of the spiral greater than input_value
def get_values(input_value):
    # Used to track the situation and the coordinate values 
    values = {}
    values["0 0"] = 1
    position = [0, 0]
    tracker = 0
    tracker_2 = -1
    # Loop this until a value is found satisfying the before mentioned conditions
    while True:
        # If at the end of the spiral, move right one space, check if value fits and then continue 
        if position == [tracker, tracker]:
            position = [tracker + 1, tracker]
            sum_around = get_adjacent_sum(values, position)
            if sum_around > input_value:
                return sum_around
            values[str(tracker + 1) + " " + str(tracker)] = get_adjacent_sum(values, position)
            tracker += 1
            tracker_2 += 2
        else:
            # Going up the spiral 
            for i in range(tracker_2):    
                position = [position[0], position[1] - 1]
                sum_around = get_adjacent_sum(values, position)
                if sum_around > input_value:
                    return sum_around
                values[str(position[0]) + " " + str(position[1])] = get_adjacent_sum(values, position)
            
            # Going left of spiral
            for j in range(tracker_2 + 1):
                position = [position[0] - 1, position[1]]
                sum_around = get_adjacent_sum(values, position)
                if sum_around > input_value:
                    return sum_around
                values[str(position[0]) + " " + str(position[1])] = get_adjacent_sum(values, position)
            
            # Goind down of spiral 
            for j in range(tracker_2 + 1):
                position = [position[0], position[1] + 1]
                sum_around = get_adjacent_sum(values, position)
                if sum_around > input_value:
                    return sum_around
                values[str(position[0]) + " " + str(position[1])] = get_adjacent_sum(values, position)
            
            # Completing the spiral loop
            for j in range(tracker_2 + 1):
                position = [position[0] + 1, position[1]]
                sum_around = get_adjacent_sum(values, position)
                if sum_around > input_value:
                    return sum_around
                values[str(position[0]) + " " + str(position[1])] = get_adjacent_sum(values, position)

# Function used to add all the adjacent values up given the list of current values and the current position                
def get_adjacent_sum(values, position):
    # All the coordinates that surround position
    adj_values = [[position[0] + 1, position[1]], [position[0] + 1, position[1] - 1], [position[0] + 1, position[1] + 1], 
                  [position[0] - 1, position[1]], [position[0] - 1, position[1] + 1], [position[0] - 1, position[1] - 1], 
                  [position[0], position[1] + 1], [position[0], position[1] - 1]]
    # Add the coordinates together if they exist in values
    total = 0
    for av in adj_values:
        coord = str(av[0]) + " " + str(av[1])
        if values.has_key(coord):
            total += values[coord]
    return total
    
# Open the file and call the function
print get_values(289326)