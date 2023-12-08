import re
import math

data = open('input.txt', 'r', -1, 'UTF-8').read()
data.replace('Card ', '')
lines = data.split('\n')
linecount = len(lines)
winning = []
revealed = []
points = 0

for x in lines:
    halves = x.split(' | ')
    winning.append(halves[0].split(': ')[1])
    revealed.append(halves[1])


for i in range(linecount):
    correct = 0
    assert correct==0
    new_points = 0
    winners = re.findall(r'\d{1,2}\b', winning[i])
    assert len(winners)==10
    actual_numbers = re.findall(r'\d{1,2}\b', revealed[i])
    if i==5:
        print(str(actual_numbers))
    assert len(actual_numbers)==25
    for winner in winners:
        if (winner in actual_numbers):
            correct = correct + 1
    if correct<2:
        new_points = correct
    else:
        new_points= int(math.exp2(correct-1))
    points += new_points



print('Points: '+str(points))
