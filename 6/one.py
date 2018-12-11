#!/usr/bin/env python3
import string
import numpy
from scipy.spatial import distance
from collections import OrderedDict
from operator import itemgetter
from itertools import islice

numpy.set_printoptions(threshold=numpy.nan)
numpy.set_printoptions(linewidth=600)

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
  x_max = max(x_values)+2
  y_max = max(y_values)+1

  field = numpy.empty((x_max, y_max), dtype=object)
  for key in data:
    x = int(data[key][0])
    y = int(data[key][1])
    field[x][y] = str(key)

  field = numpy.swapaxes(field, 1, 0)

  for i in range(len(field)):
    for j in range(len(field[i])):
      dist_dict = {}
      for key in data:
        x = int(data[key][0])
        y = int(data[key][1])
        dist = distance.cityblock([i, j], [x, y])
        dist_dict[key] = dist
      o_dists = OrderedDict(sorted(dist_dict.items(), key = itemgetter(1), reverse = False))
      first_value, second_value = islice(o_dists.values(), 2)
      first_item = list(o_dists.keys())[0]
      second_item = list(o_dists.keys())[1]
      if field[i][j] is None:
        if first_value == second_value:
          field[i][j] = '.'
        else:
          field[i][j] = first_item.lower()

  x_len = len(field)-1
  y_len = len(field[0])-1
  items_to_remove = []
  for i in range(x_len):
    items_to_remove.append(field[i][0])
    items_to_remove.append(field[i][y_len])
  for i in range(y_len):
    items_to_remove.append(field[0][i])
    items_to_remove.append(field[x_len][i])
  
  items_to_remove = set(items_to_remove)
  for i in range(len(field)):
    for j in range(len(field[i])):
      if field[i][j] in items_to_remove:
        field[i][j] = '.'


  result = []
  for key in data:
    counter = 1
    nyckel = key.lower()
    for i in range(len(field)):
      for j in range(len(field[i])):
        if field[i][j] == nyckel:
          counter += 1
    result.append(counter)
  print(result)
  print(max(result))
  




if __name__ == '__main__':
  main()