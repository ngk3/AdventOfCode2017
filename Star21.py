
def read_file(file_name):
    n = 0
    e = 0
	#line = open(file_name).readline()
    #line = "ne,ne,ne"
    #line = "ne,ne,sw,sw"
    #line = "ne,ne,s,s"
    line = "se,sw,se,sw,sw"
    for s in line.split(","):
        if s == "n":
            n += 1
        elif s == "s":
            n -= 1
        elif s == "ne":
            n += 1
            e += 1
        elif s == "nw":
            n += 1
            e -= 1
        elif s == "se":
            n -= 1
            e += 1
        else:
            n -= 1
            e -= 1
    print "n:", n, "| e:",e
    count = abs(e)
    
    n = (abs(n) - count) * (n / abs(n)) 
    e = 0
    return count + abs(n) 

print read_file("star21_input.txt")