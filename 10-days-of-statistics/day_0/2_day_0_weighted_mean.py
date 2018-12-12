import math

"""
main function
"""
def main():
  number_of_input = input()
  x_inputs = input()
  w_inputs = input()

  # x_inputs = "10 40 30 50 20"
  # w_inputs = "1 2 3 4 5"

  xw_inputs = {}

  x_inputs = x_inputs.split(" ")
  w_inputs = w_inputs.split(" ")

  input_length = len(x_inputs)

  sum_of_xw_inputs = 0
  sum_of_w_inputs = 0

  for index in range(0, input_length):
    x_input = int(x_inputs[index])
    w_input = int(w_inputs[index])
    sum_of_xw_inputs += (x_input * w_input)
    sum_of_w_inputs += (w_input)

  weighted_sum = sum_of_xw_inputs / sum_of_w_inputs
  weighted_sum = round(weighted_sum, 1)

  print (weighted_sum)

main()