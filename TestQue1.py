# 1. Write a Python program to read a CSV file and display its contents.

import csv

with open('example.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)