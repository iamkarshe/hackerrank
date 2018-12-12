import math
import statistics

"""
"""
def main():
  x_elements = []
  f_elements = []
  elements = []

  number_of_elements = input()
  input_x_elements = input()
  input_f_elements = input()

  # number_of_elements = 6
  # input_x_elements = "6 12 8 10 20 16"
  # input_f_elements = "5 4 3 2 1 5"

  input_x_elements = input_x_elements.split(" ")
  for x_element in input_x_elements:
    x_elements.append(int(x_element))

  input_f_elements = input_f_elements.split(" ")
  for f_element in input_f_elements:
    f_elements.append(int(f_element))

  for index in range(len(x_elements)):
    x_element = x_elements[index]
    frequency = f_elements[index]
    for frq in range(frequency):
      elements.append(x_element)

  elements = sorted(elements)
  number_of_elements = len(elements)
  
  lower_half_array = []
  upper_half_array = []
  middle_value = math.floor(number_of_elements/2)

  lower_half_array = elements[:middle_value]
  upper_half_array = elements[middle_value+1:]

  q1 = round(statistics.median(lower_half_array), 1)
  q3 = round(statistics.median(upper_half_array), 1)

  diff = float(q3 - q1)
  diff = round(diff, 1)

  print(diff)
  

main()