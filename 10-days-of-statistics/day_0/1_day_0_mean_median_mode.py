import math

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

  mean_value = mean(number_array)
  median_value = median(number_array)
  mode_value = mode(number_array)
  print (mean_value)
  print (median_value)
  print (mode_value)

"""
calculate mean from given set of numbers
"""
def mean(number_array):
  mean_value = 0
  sum_number = 0
  number_of_input = len(number_array)
  for number in number_array:
    sum_number += number
  mean_value = sum_number / number_of_input
  mean_value = round(mean_value, 1)
  return mean_value

"""
calculate median from given set of numbers
TODO: find another approach to solve this
"""
def median(number_array):
  number_array = sorted(number_array)
  number_array_len = len(number_array)
  middle_number_sum = 0

  if ( number_array_len % 2 == 0):
    lower_bound = math.floor(number_array_len/2) - 1
    upper_bound = math.ceil(number_array_len/2)
    middle_number_sum += number_array[lower_bound]
    middle_number_sum += number_array[upper_bound]
  else:
    middle_bound = math.floor(number_array_len/2)
    middle_number_sum += number_array[middle_bound]

  medien_value = middle_number_sum
  if ( number_array_len % 2 == 0):
    medien_value = middle_number_sum / 2
  
  medien_value = round(medien_value, 1)
  return medien_value

"""
get mode from given set of numbers
TODO: find another approach to solve this
"""
def mode(number_array):
  occurances = {}
  number_array = sorted(number_array)
  for number in number_array:
    if str(number) not in occurances:
      occurances[str(number)] = 0

    occurance = occurances.get(str(number))
    occurance += 1
    occurances[str(number)] = occurance
  
  occurances = sorted(occurances.items(), key=lambda kv: kv[1], reverse=True)
  
  first_element = 0
  for element in occurances:
    for key in element:
      first_element = key
      break
    break
    
  return int(first_element)

"""
start application
"""
main()