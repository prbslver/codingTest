'''
https://www.acmicpc.net/problem/18238
written 2021/02/09
'''

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(alphabet)
_alphabet = {}

for x, y in zip(alphabet, range(length)):
    _alphabet[x] = y

def forward(x, y):
    x = _alphabet[x]
    y = _alphabet[y]
    count = 0
    while True:
        if x + count == y or x + count - length == y:
            return count
        count = count + 1

def backward(x, y):
    x = _alphabet[x]
    y = _alphabet[y]
    count = 0
    while True:
        if x - count == y or x - count + length == y:
            return count
        count = count + 1

string = 'A' + input()

all_distance = 0

for x in range(0,len(string)):
    try:
        first = string[x]
        second = string[x + 1]
        forward_distance = forward(first, second)
        backward_distance = backward(first, second)
        if forward_distance < backward_distance:
            all_distance = all_distance + forward_distance 
        else:
            all_distance = all_distance + backward_distance
    except:
        print(all_distance)
