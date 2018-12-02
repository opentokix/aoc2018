#!/usr/bin/env python3

import collections

def main():
  data = []
  f = open('one_input.txt')
  for line in f:
    data.append(list(line))
  for s in data:
    for c in data:
      f = 0
      if len(s) == len(c):
        for i in range(len(c)):
          if s[i] != c[i]:
            f += 1
        if f == 1:
          print("".join(s), "".join(c))

if __name__ == '__main__':
  main()