#!/usr/bin/env python3
import numpy

def main():
  f = open('test_data.txt')
  fab = numpy.zeros((1200, 1200))
  for line in f:
    line = line.replace('#', '')
    line = line.replace(':', '')
    line = line.replace('\n', '')
    line = line.replace(' @', '')
    line = line.replace('x', ',')
    wip1 = line.split(' ')

    cut_data = {int(wip1[0]): {'x': wip1[1].split(',')[0],
                               'y': wip1[1].split(',')[1],
                               'w': wip1[2].split(',')[0],
                               'h': wip1[2].split(',')[1],}}
    for key, value in cut_data.items():
      sx = int(value['x'])
      sy = int(value['y'])
      for xi in range(int(value['w'])):
        for yi in range(int(value['h'])):
          posx = sx + xi
          posy = sy + yi
          fab[posx][posy] += 1
  # Array created

    for key, value in cut_data.items():
      sx = int(value['x'])
      sy = int(value['y'])
      flag = 0

      for xi in range(int(value['w'])):
        for yi in range(int(value['h'])):
          posx = sx + xi
          posy = sy + yi
          if fab[posx][posy] > 1.0:
            flag += 1
      if flag == 0:
        print(key)

if __name__ == '__main__':
  main()