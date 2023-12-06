import re

DIGITS = {
    'oneight': '18',
    'twone': '21',
    'threeight': '38',
    'fiveight': '58',
    'sevenine': '79',
    'eightwo': '82',
    'eighthree': '83',
    'nineight': '98',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def part2(line: str) -> int:
    part2sum=0

    for digit in DIGITS:
        line = line.replace(digit, DIGITS[digit])
    part2lines = line.split('\n')
    for x in part2lines:
        foundDigits = re.findall('\d', x)
        part2sum += int(foundDigits[0] + foundDigits[-1])
    return part2sum

INPUT = open('input.txt', 'r')
data = INPUT.read().strip()
lines = data.split('\n')
numbers = [re.findall('\d', x) for x in lines]
answer = sum(int(set[0]+set[-1]) for set in numbers)

answer2 = part2(data)

print('Output is: '+str(answer)+'Part2 is: '+str(answer2))
