Feature: The calculator

Scenario Outline: Get sum total
  Given a <values_add> to sum
  When the calculator sums the values
  Then the <total_add> of sum is correct

  Examples: values_add
  | values_add         | total_add |
  | 5,7                | 12        |
  | 5,3                | 8         |
  | 15,33              | 48        |
  | 33,15              | 48        |

Scenario Outline: Get sub total
  Given a <values_sub> to substract
  When the calculator substract the values
  Then the <total_sub> of substraction is correct

  Examples: values_sub
  | values_sub          | total_sub |
  | 5,7                 | -2        |
  | 5,3                 | 2         |
  | 115,30              | 85        |
