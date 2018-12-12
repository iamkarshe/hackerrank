import math

"""
main function
"""
def main():
  """
      [1] [2] [3] [4] [5] [6]
  [1] 2   3   4   5   6   7
  [2] 3   4   5   6   7   8
  [3] 4   5   6   7   8   9
  [4] 5   6   7   8   9  10'
  [5] 6   7   8   9  10' 11'
  [6] 7   8   9  10' 11' 12'  
  """

  total_number = 36
  sum_more_than_nine = 6
  sum_less_than_nine = total_number - sum_more_than_nine 
  probability = sum_less_than_nine / total_number
  probability = round(probability, 1)
  
  print(probability)

main()