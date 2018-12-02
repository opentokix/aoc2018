#!/usr/bin/env python3

import collections

def main():
  data = []
  freq = []
  twos = 0
  threes = 0

  f = open('one_input.txt')
  for line in f:
    counter = collections.Counter(list(line))
    print(counter.values())
    if 2 in counter.values():
      twos += 1
    if 3 in counter.values():
      threes += 1
  result = twos * threes
  print(result)

if __name__ == '__main__':
  main()