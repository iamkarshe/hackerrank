import math
import statistics

"""
main function
we used 'statistics' package of py3
"""
def main():
  x_elements = []
  
  number_of_elements = input()
  input_x_elements = input()

  # number_of_elements = 5
  # input_x_elements = "10 40 30 50 20"

  input_x_elements = input_x_elements.split(" ")
  for x_element in input_x_elements:
    x_elements.append(int(x_element))

  mean_value = statistics.mean(x_elements)

  squared_distance = 0
  for x_element in x_elements:
    distance = math.pow((x_element-mean_value), 2)
    squared_distance += distance

  deviation = math.sqrt( (squared_distance/len(x_elements) ) ) 
  deviation = round(deviation, 1)

  print (deviation)

main()