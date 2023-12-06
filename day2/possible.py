import re
RMAX = 12
GMAX = 13
BMAX = 14

answer = 0
answer_p2 = 0

data = open('input.txt', 'r', -1, 'UTF-8').read()
lines = data.replace('Game ', '').split('\n')

def split_line(line: str) -> list[str]:
    """
    Splits the game line into the game number at index 0 and the draw info at index 1.
    """
    return line.split(': ')



def determine(line: str) -> int:
    """Returns as 0 if the line was not possible, else the line number integer."""
    #split the line into a line number and the line info
    number_draws = split_line(line)
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
        return number
    else:
        return 0
    
def find_power(line: str) -> int:
    red_max = 0
    green_max = 0
    blue_max = 0
    split = split_line(line)
    game = int(split[0])
    hands = split[1].split('; ')

    for hand in hands:
        hand.strip()
        colors = hand.split(', ')
        #del colors[0]
        for color in colors:
            segregated = color.split(' ')
            amount = int(segregated[0])
            specific_color = segregated[1]
            match specific_color:
                case 'red':
                    red_max = amount if (amount>red_max) else red_max
                case 'green':
                    green_max = amount if (amount>green_max) else green_max
                case 'blue':
                    blue_max = amount if (amount>blue_max) else blue_max

    return (red_max*green_max*blue_max)

for line in lines:
    answer += determine(line)
    answer_p2 += find_power(line)


print('The sum of all possible games is: '+str(answer))
#2507 is too low a power
print('The power of all lines is: '+str(answer_p2))