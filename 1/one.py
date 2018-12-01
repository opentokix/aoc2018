#!/usr/bin/env python3
import requests

def main():
  with open('one_input.txt') as f:
    data = f.read().splitlines()
  value = 0
  for d in data:
    value += int(d)
  print(value)

if __name__ == '__main__':
  main()