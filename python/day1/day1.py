def get_calibration_values(strings):
    vals = []
    for string in strings:
        firstdigit = ''
        seconddigit = ''
        for n in string:
            if n.isnumeric():
                firstdigit = n
                break
        length = len(string)
        for x in range(length):
            index = length - 1 - x
            n = string[index]
            if n.isnumeric():
                seconddigit = n
                break
        digits = str(firstdigit) + str(seconddigit)
        print(digits)
        vals.append(int(digits))
    return vals

f = open("input.txt", "r")

input = []
for x in f.readlines():
    input.append(x)

values = get_calibration_values(input)

print('sum: {}'.format(sum(values)))


