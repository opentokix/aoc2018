#!/usr/bin/env python3
import string
import numpy
numpy.set_printoptions(threshold=numpy.nan)

def main():
  f = open('one_input.txt')
  letters = []
  data = {}
  x_values = []
  y_values = []
  for first in string.ascii_uppercase:
    for second in string.ascii_uppercase:
      letters.append(first + second)
  c = 0
  for line in f:
    line = line.replace('\n', '')
    line = line.replace(' ', '')
    data[letters[c]] = line.split(',')
    x_values.append(int(data[letters[c]][0]))
    y_values.append(int(data[letters[c]][1]))
    c += 1
  x_values.sort()
  y_values.sort()
  field = numpy.empty((x_values[-1]+1,y_values[-1]+1), dtype=object)
  for key in data:
    x = int(data[key][0])
    y = int(data[key][1])
    field[x][y] = str(key)

  for i in range(len(field)):
    for j in range(len(field[i])):
      print(field[i][j])







if __name__ == '__main__':
  main()