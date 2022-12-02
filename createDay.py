import os


print("What day is it?")
day = input()
path = f'./d{day}'
os.mkdir(path)
open(f'{path}/test.txt', "x")
open(f'{path}/input.txt', "x")
open(f'{path}/p1.py', "x")
open(f'{path}/p2.py', "x")
print(f'Day {day} created!')

os.system(f'cd d{day}')
