import math
import statistics

"""
main function
"""
def main():
  number_of_input = input()
  number_of_input = int(number_of_input)

  number_array = []
  input_numbers = input()
  input_numbers = input_numbers.split(" ")

  # number_of_input = 10
  # input_numbers = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
  
  for number in input_numbers:
    number_array.append(int(number))

  mean_value = statistics.mean(number_array)
  median_value = statistics.median(number_array)
  mode_value = statistics.mode(number_array)
  print (mean_value)
  print (median_value)
  print (mode_value)

"""
start application
"""
main()