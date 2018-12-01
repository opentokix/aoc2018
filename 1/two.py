#!/usr/bin/env python3
from sys import exit as bail
from itertools import cycle 

def main():
  freq = []
  data_list = []
  value = 0
  freq.append(value)
  iterations = 0

  with open('one_input.txt') as f:
    data = f.read().splitlines()
  for d in data:
    data_list.append(int(d))

  pool = cycle(data_list)
  for item in pool:
    iterations += 1
    value += item 
    if value in freq:
      print("Took ", iterations, " iterations to get value: ", value)
      bail(0)
    freq.append(value)

if __name__ == '__main__':
  main()