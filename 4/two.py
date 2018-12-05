#!/usr/bin/env python3
import numpy
import operator

def main():
  f = open('one_input.txt')
  data = {}
  guard = None
  start_time = -1
  end_time = -1
  flag = 0
  time = 0
  for line in f:
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace('\n', '')
    l = line.split(' ')
    if 'Guard' in l:
      guard = l[3]
      if guard not in data:
        hour = {}
        for i in range(60):
          hour.update({i: 0})
        data.setdefault(guard, hour)
    if 'asleep' in l:
      start_time = l[1].split(':')[1]
    if 'wakes' in l:
      end_time = l[1].split(':')[1]
      time = (int(end_time)- int(start_time))
      for i in range(int(start_time), int(end_time)):
        data[guard][i] += 1
  for key in data:
    s_dict = sorted(data[key].items(), key=operator.itemgetter(1))
    print(key, ":", s_dict[-1])

if __name__ == '__main__':
  main() 