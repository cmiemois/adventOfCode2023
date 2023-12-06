import re
RMAX = 12
GMAX = 13
BMAX = 14

answer = 0

data = open('input.txt', 'r', -1, 'UTF-8').read()
lines = data.replace('Game ', '').split('\n')


def determine(line: str) -> int:
    """Returns as 0 if the line was not possible, else the line number as an integer"""
    #split the line into a line number and the line info
    number_draws = line.split(':')
    #boolean to track if the game ever possible
    possible = True
    number = int(number_draws[0])
    draws = number_draws[1]

    #Each hand
    for draw in draws.split('; '):
        #Each color separately
        colors = draw.split(', ')
        for color in colors:
            color = color.strip()
            #0 is amount, 1 is color
            halves = color.split(' ')
            amount = int(halves[0])
            color_string = halves[1]

            match color_string:
                case 'red':
                    if amount>RMAX:
                        possible = False
                        break
                case 'green':
                    if amount>GMAX:
                        possible = False
                        break
                case 'blue':
                    if amount>BMAX:
                        possible = False
                        break
        if not possible:
            break

    if possible:
        print('Line ' + str(number_draws[0]) + ' was POSSIBLE')
        return number
    else:
        print('Line ' + str(number) + ' was NOT POSSIBLE')
        return 0

for line in lines:
    answer += determine(line)


#2457 is too low, sum of all lines is 5000
print('The sum of all possible games is: '+str(answer))