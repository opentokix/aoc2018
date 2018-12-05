#!/usr/bin/env python3
import numpy

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
        data.setdefault(guard, 0)
    if 'asleep' in l:
      start_time = l[1].split(':')[1]
    if 'wakes' in l:
      end_time = l[1].split(':')[1]
      time = (int(end_time)- int(start_time))
      src_time = data[guard]
      data[guard] = src_time + time

  sorted_data = sorted(data.items(), key=lambda kv: kv[1])
  most_sleeping = str(sorted_data[-1][0])
  most_sleeping = int(most_sleeping.replace('#', ''))
  hour = {}
  for i in range(60):
    hour.update({i: 0})
  
  flag = False
  f = open('one_input.txt')
  for line in f:
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace('\n', '')
    l = line.split(' ')
    search_string = "#" + str(most_sleeping)
    if 'Guard' in l:
      flag = False
      if search_string in l:
        flag = True
    if flag and 'asleep' in l:
      start_time = int(l[1].split(':')[1])
    if flag and 'wakes' in l:
      end_time = int(l[1].split(':')[1])
      for i in range(start_time, end_time):
        hour[i] += 1
  sorted_hour = sorted(hour.items(), key=lambda kv: kv[1])
  answer = int(sorted_hour[-1][0]) * int(most_sleeping)
  print("Answer: ", answer)

if __name__ == '__main__':
  main() 