import math
import statistics

"""
main function
we used 'statistics' package of py3
"""
def main():

  number_array = []
  number_of_elements = input()
  input_numbers = input()

  # number_of_elements = 12
  # input_numbers = "19 26 25 37 32 28 22 23 29 34 39 31"

  input_numbers = input_numbers.split(" ")
  for number in input_numbers:
    number_array.append(int(number))

  number_array = sorted(number_array)
  number_array_len = len(number_array)

  lower_half_array = []
  upper_half_array = []

  median_value = statistics.median(number_array)

  middle_value = math.floor(number_array_len/2)

  lower_half_array = number_array[:middle_value]
  upper_half_array = number_array[middle_value+1:]
  
  # event number -- include median
  if (number_array_len % 2 == 0):
    lower_half_array.append(median_value)
    upper_half_array.append(median_value)

  q1 = int(statistics.median(lower_half_array))
  q2 = int(median_value)
  q3 = int(statistics.median(upper_half_array))

  print(q1)
  print(q2)
  print(q3)

main()