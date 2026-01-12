#Example of defining and printing a list
my_list = [5, 55, 555, 5555, 55555, 555555]
print('List:', my_list)

##Example of converting a string to a list
dev = "aditya"
list(dev)
print('List from string:', list(dev))

len(my_list)
print('Length of my_list:', len(my_list))

##Example of accessing an element from a list using indexing
my_list[1]
print('Element at index 1 of my_list:', my_list[1])

##Example of list nested inside a list and its access
nested_list = [10, 20, [30, 40], 50]
nested_list[2]
print('list present at index 2 of nested_list:', nested_list[2])
nested_list[2][1]
print('Element at index 1 of the list present at index 2 of nested_list:', nested_list[2][1])

##Example of unpacking a list into variables
details = ["aditya", 19, "statistics"]
name, age, major = details
print('Name:', name)
print('Age:', age)
print('Major:', major)

##Example of index method to find the index of an element in a list
my_list.index(555)
print('Index of 555 in my_list:', my_list.index(555))

##Example of slicing a list
my_list[1:3]
print('Elements from index 1 to 3 of my_list:', my_list[1:3])

##Example of negative indexing in a list
my_list[-1]
print('Last element of my_list :', my_list[-1])

##Example of incremental slicing in a list
my_list[0::2]
print('Elements from index 0 to end with step 2 of my_list:', my_list[0::2])

#Example of defining and printing a tuple
my_tuple = ('Atlanta', 'Luxor', 'Bengaluru', 777, 888, 555)
print('Tuple:', my_tuple)

##Example of converting a string to a tuple
data = "stats"
tuple(data)
print('Tuple from string:', tuple(data))

##Example of accessing an element from a tuple using indexing
my_tuple[2]
print('Element at index 2 of my_tuple:', my_tuple[2])

##Example of checking the presence of an element in a tuple
777 in my_tuple
print('Is 777 present in my_tuple?:', 777 in my_tuple)

##Example of slicing a tuple
my_tuple[1:4]
print('Elements from index 1 to 4 of my_tuple:', my_tuple[1:4])

##Example of optional start and stop in indexing a tuple
tuple_2 = (10, 20, 30, 40, 50, 20, 60)
tuple_2.index(20, 1, 4)
print('Index of 20 in tuple_2 between index 1 and 4:', tuple_2.index(20, 1, 4))

##Example of using count() method in a tuple
tuple_2.count(20)
print('Count of 20 in tuple_2:', tuple_2.count(20))

##Example of using sorted() function on a tuple
sorted(tuple_2)
print('Sorted tuple_2:', sorted(tuple_2))

##Example of using reverse parameter and key parameter in sorted() function
sorted(tuple_2, key=None, reverse=True)
print('Sorted tuple_2 in descending order:', sorted(tuple_2, key=None, reverse=True))