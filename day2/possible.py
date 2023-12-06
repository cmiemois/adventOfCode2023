import re
RMAX = 12
GMAX = 13
BMAX = 14

answer = 0

data = open('input.txt', 'r', -1, 'UTF-8').read()
lines = data.replace('Game ', '').split('\n')

#If not performed, the last index will just be an empty string which causes issues
lines.pop()

def determine(line: str) -> int:
    """Returns as 0 if the line was not possible, else the line number as an integer"""
    #split the line into a line number and the line info
    number_draws = line.split(':')
    #boolean to track if the game ever failed
    failed = False
    print(str(number_draws))
    answer = int(number_draws[0])
    draws = number_draws[1]

    #Each hand
    for draw in draws.split('; '):

        #Each color separately
        colors = draw.split(', ')
        for color in colors:
            #0 is amount, 1 is color
            halves = color.split(' ')
            print('halves[0]: '+str(halves[1]))
            amount = int(halves[0])
            color_string = halves[1]
            match color_string:
                case 'red':
                    if amount>RMAX:
                        print('red maxed out, line is ' +str(answer))
                        answer=0
                        failed = True
                        break
                case 'green':
                    if amount>GMAX:
                        answer=0
                        failed = True
                        break
                case 'blue':
                    if amount>BMAX:
                        answer=0
                        failed = True
                        break
        if failed:
            break

    if answer!=0:
        print('Line ' + str(answer) + ' was POSSIBLE')
    else:
        print('Line '+str(answer)+' was NOT POSSIBLE')

    return answer

answer = sum(determine(x) for x in lines)


print('The sum of all possible games is: '+str(answer))