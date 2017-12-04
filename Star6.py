
def get_values(input_value):
    values = {}
    values["0 0"] = 1
    position = [0, 0]
    tracker = 0
    tracker_2 = -1
    while True:
        if position == [tracker, tracker]:
            position = [tracker + 1, tracker]
            sum_around = get_adjacent_sum(values, position)
            if sum_around > input_value:
                return sum_around
            values[str(tracker + 1) + " " + str(tracker)] = get_adjacent_sum(values, position)
            tracker += 1
            tracker_2 += 2
        else:
            for i in range(tracker_2):    
                position = [position[0], position[1] - 1]
                sum_around = get_adjacent_sum(values, position)
                if sum_around > input_value:
                    return sum_around
                values[str(position[0]) + " " + str(position[1])] = get_adjacent_sum(values, position)
            
            for j in range(tracker_2 + 1):
                position = [position[0] - 1, position[1]]
                sum_around = get_adjacent_sum(values, position)
                if sum_around > input_value:
                    return sum_around
                values[str(position[0]) + " " + str(position[1])] = get_adjacent_sum(values, position)
                
            for j in range(tracker_2 + 1):
                position = [position[0], position[1] + 1]
                sum_around = get_adjacent_sum(values, position)
                if sum_around > input_value:
                    return sum_around
                values[str(position[0]) + " " + str(position[1])] = get_adjacent_sum(values, position)
            
            for j in range(tracker_2 + 1):
                position = [position[0] + 1, position[1]]
                sum_around = get_adjacent_sum(values, position)
                if sum_around > input_value:
                    return sum_around
                values[str(position[0]) + " " + str(position[1])] = get_adjacent_sum(values, position)
        
def get_adjacent_sum(values, position):
    adj_values = [[position[0] + 1, position[1]], [position[0] + 1, position[1] - 1], [position[0] + 1, position[1] + 1], 
                  [position[0] - 1, position[1]], [position[0] - 1, position[1] + 1], [position[0] - 1, position[1] - 1], 
                  [position[0], position[1] + 1], [position[0], position[1] - 1]]
    total = 0
    for av in adj_values:
        coord = str(av[0]) + " " + str(av[1])
        if values.has_key(coord):
            total += values[coord]
    return total
    
# Open the file and call the function
print get_values(289326)