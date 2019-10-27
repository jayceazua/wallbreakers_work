"""
Given a rectangular matrix m and an integer k, 
  consider all the k * k contiguous square submatrices of m.
  Your task is the following:

- Calculate the sum of all the numbers within each k x k submatrix.
- Determine the maximum of all these sums
- Find all the "distinct" numbers that appear in any of the squares with a sum equal to the maximum. 
- Each integer from these squares should be calculated exactly once.
- Return the sum of the these distinct numbers.

Example:

  m = [
    [1, 0, 1, 5, 6],
    [3, 3, 0, 3, 3],
    [2, 9, 2, 1, 2],
    [0, 2, 4, 2, 0],
  ]
  k = 2

  Output should be 29


  [ 
    [1,   0,  1, {5, 6}],
    [{3,  3}, 0, {3, 3}],
    [{2, {9}, 2}, 1, 2],
    [0,  {2,  4}, 2, 0],
  ]

If we consider all the 2 x 2 squares in m, there are 3 of them with a maximum sum of 17

[ [5, 6], 
  [3, 3]]
(5 + 6 + 3 + 3) = 17

[ [3, 3], 
  [2, 9]]
(3 + 3 + 2 + 9) = 17

[ [9, 2], 
  [2, 4]]
(9 + 2 + 2 + 4) = 17

Among these 3 squares which each have the maximum sum,
  only the distinct numbers 2, 3, 4, 5, 6, 9 appear.
So the answer is 2 + 3 + 4 + 5 + 6 + 9 = 29


Input/ output

[execution time limit] 4s

[input] array.array.integer m


  Guranteed Constraints
  - 1 <= m.length <= 100
  - 1 <= m[i].length <= 100
  - 0 <= m[i][j] <= 100

[input] integer k
  Guarenteed Constraints
  - 1 <= k <= min(m.length, m[i].length)

[output] integer
 - The sum of all distinct integers within the k x k squares with the maximal sum 

"""



m = [
    [1, 0, 1, 5, 6],
    [3, 3, 0, 3, 3],
    [2, 9, 2, 1, 2],
    [0, 2, 4, 2, 0],
]

k = 2

def foo_bar(m, k):
  max_box = 0
  all_values = set()
  for i in range(len(m) - k + 1):
    for j in range(len(m[i]) - k + 1):
      max_value, values = sum_submatrix(m, i, j, i+k, j+k)

      if max_value > max_box:
        max_box = max_value
        all_values.clear()
        for v in values:
          all_values.add(v)
      elif max_value == max_box:
        for v in values:
          all_values.add(v)
  
  return sum(all_values)


def sum_submatrix(box, x1, y1, x2, y2):
  total = 0
  values = []
  for i in range(x1, x2):
    for j in range(y1, y2):
      total += box[i][j]
      values.append(box[i][j])

  return (total, values)



foo_bar(m, k)
