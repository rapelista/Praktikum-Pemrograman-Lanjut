# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# use of string
Tuple1 = ('Teknik', 'Komputer')
print("\nTuple with the use of String: ")
print(Tuple1)

# use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

# built-in function
Tuple1 = tuple('Informatika')
print("\nTuple with the use of function: ")
print(Tuple1)

tuple1 = (1, 2, 3)
print(tuple1)
tuple1 = list(tuple1)
tuple1[1] = 10
tuple1 = tuple(tuple1)
print(tuple1)
