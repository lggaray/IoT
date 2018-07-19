inp = []
for i in range(3):
    inp.append(input('Enter an integer {}: '.format(i+1)))
print('{} is greatest number of {}, {} and {}!'.format(max(inp), inp[0], inp[1], inp[2]))
