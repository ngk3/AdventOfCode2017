
def read_file(file_name):
    line_splitted = open(file_name).readline().split(",")
    for ls in range(len(line_splitted)):
        line_splitted[ls] = int(line_splitted[ls])
    return line_splitted
    
def knot_hash(lengths):
    complete_list = []
    for i in range(256):
        complete_list.append(i)
    current_index = 0
    skip_size = 0

    for l in lengths:
        reversing = []
        for i in range(l):
            if current_index + i > 255:
                reversing.append(current_index + i - 256)
            else:
                reversing.append(current_index + i)
        reversing.reverse()
        
        for i in range(l / 2):
            if current_index + i > 255:
                temp = complete_list[current_index + i - 256]
                complete_list[current_index + i - 256] = complete_list[reversing[i]]
                complete_list[reversing[i]] = temp
            else:
                temp = complete_list[current_index + i]
                complete_list[current_index + i] = complete_list[reversing[i]]
                complete_list[reversing[i]] = temp
        
        current_index += l + skip_size
        if current_index > 255:
            current_index -= 256
        skip_size += 1
        
    return complete_list 

lengths = read_file("star19_input.txt")
complete_list = knot_hash(lengths)
print complete_list
print "list[0] * list[1] = ", complete_list[0] * complete_list[1]