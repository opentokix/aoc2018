#!/usr/bin/env python3
import string

def create_list(filename):
  f = open(filename)
  data = []
  for l in f:
    for c in l:
      data.append(c)
  data.pop(-1)
  return data

def check_pair(first, second):
  if first == 0 or second == 0: 
    return False
  if first.lower() != second.lower():
    return False
  elif first == second:
    return False
  else:
    return True

def remove_pairs(data):
  removed = 0
  for i in range(1, len(data)):
    if check_pair(data[i], data[i-1]):
      removed += 1
      data[i] = 0
      data[i-1] = 0
  data = list(filter(lambda a: a != 0, data))
  return data, removed

def del_char(s, c):
  result = s.replace(c, '')
  return result.replace(c.upper(), '')

def main():
  data = create_list('one_input.txt')
  flag = len(data)
  while flag != 0:
    data, flag = remove_pairs(data)
  print("Part 1:", len(data))

  alpha = list(string.ascii_lowercase)
  polymer = ''.join(data)
  polymer_size = []
  for c in alpha:
    result = del_char(polymer, c)
    r_list = list(result)
    flag = len(r_list)
    while flag != 0:
      r_list, flag = remove_pairs(r_list)
    polymer_size.append(len(r_list))
  polymer_size.sort()
  print("Part 2:", polymer_size[0])
  

if __name__ == '__main__':
  main()