#First option

def reverse_string(x):
  return x[::-1]

string_reversed = reverse_string('Today, 18 July 2019,  is a very lovely day.')
print (string_reversed)

#Second option

def reverse_this_string(x):
  i = len(x) - 1
  new_string =''
  while i >= 0:
    new_string = new_string + x[i]
    i -= 1
  return (new_string)  

string_reversed = reverse_this_string('Today, 18 July 2019,  is a very lovely day.')
print (string_reversed)