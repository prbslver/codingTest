'''
https://www.acmicpc.net/problem/17509
written 2020/02/09
'''

taken = []

incorrect = []

for x in range(0, 11):
    y = input().split(" ")
    taken.append(int(y[0]))
    incorrect.append(20 * int(y[1]))

taken.sort()

accumulated = 0

total = []

for x in taken:
    accumulated = accumulated + x
    total.append(accumulated)

print(sum(total) + sum(incorrect))
