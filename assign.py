import math
import csv

with open ("Data1.csv", newline = "") as f:
  reader = csv.reader(f)
  file_data = list(reader)

data = file_data[0]
n = len(data)

def mean(data):
  total = 0
  for x in data :
    total = total + int(x)
  mean = total/n
  return mean

sum = 0
for num in data:
  a = int(num) - mean(data)
  a = a**2
  sum = sum + a

result = sum/(n-1)
sd = math.sqrt(result)

print("Standard Deviation =",sd)