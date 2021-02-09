'''
https://www.acmicpc.net/problem/20115
written 2021/02/09
'''

sequence = input("enter the sequence: ").split(" ")
_sequence = []

for x in sequence:
    _sequence.append(int(x))
_sequence.sort()

while len(_sequence) > 1:
    biggest = _sequence[-1]
    del _sequence[-1]
    second = _sequence[-1]
    del _sequence[-1]
    _sequence.append(biggest + second/2.0)
    print(_sequence)

print(_sequence[-1])
