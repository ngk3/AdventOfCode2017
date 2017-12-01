
# Function used to count all the digits that match halway around the circular list and return the sum
def get_all_sequential_digits(input):
    count = 0
    # Go from 0 to n / 2 and compare i to (n / 2) + i, adding into count if matched
    for i in range(0, len(input) / 2):
        if input[i] == input[(len(input) / 2) + i]:
            count += (int(input[i]) * 2)
    return count

f = open("star1_input.txt")
print get_all_sequential_digits(f.readline())