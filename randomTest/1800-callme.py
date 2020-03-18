digit_map = {
    ' ': ' ',
    '!': '!',
    '.': '-',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def word_numbers(st):
    ret = ['']
    for char in st:
        letters = digit_map.get(char, '')
        ret = [prefix + letter for prefix in ret for letter in letters]
    return ret


number = input('input numbers : ')
ans = word_numbers(number)
for i in ans:
    print(i)