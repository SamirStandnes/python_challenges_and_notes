from tests import *


def test_list(p):
  test_range = range(1, len(p)+1, 1)
  print(test_range)
  for e in p:
    #print(e)
    if sum(e) != sum(test_range):
      return False
    for i in range(len(e)):
      #print(e[i], e[i+1:])
      if (not isinstance(e[i], int)):
          return False
      try:
        if (e[i+1:].index(e[i]) != -1):
          return False
      except:
        #print('not there')
        continue
  return True

#print(test_list([[1,2,4,3], [2, 3, 1, 4], [3, 1, 2, 1], [4,4,3,2]]))

#print(test_list([[1,2,3,4], [2,4,1,3], [3,1,4,2], [4,3,2,1]]))

def group(p):
  columns = []
  for i in range(len(p)):
    col = []
    for e in p:
      print(e[i])
      col.append(e[i])
      if len(col) == len(p):
        columns.append(col)
        col =[]
  print('columns', columns)
  return columns

#print(group([[1,2,3,4], [2,4,1,3],  [3,1,4,2], [4,3,2,1]]) )

def check_sudoku(s):
  for e in s:
    for i in range(len(e)):
      if not isinstance(e[i], int):
        return False
  columns = group(s)
  print(test_list(s))
  print(test_list(columns))
  if (test_list(s) and test_list(columns)):
    return True
  return False

#print(check_sudoku([[1,2,3,4], [2,4,1,3], [3,1,4,2], [4,3,2,1]]))
    
print(check_sudoku(incorrect))
#>>> False

#print(check_sudoku(correct))
#>>> True

#print(check_sudoku(incorrect2))
#>>> False

#print(check_sudoku(incorrect3))
#>>> False

#print(check_sudoku(incorrect4))
#>>> False
