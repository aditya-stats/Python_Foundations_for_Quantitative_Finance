# Example of defining and printing an integer variable
int_var = 2006
print('Integer:', int_var)

# Example of defining and printing a float variable
float_var = 5.5
print('Float:', float_var)

# Example of defining and printing a string variable
str_var = "regression"
print('String:', str_var)

# Example of defining and printing a boolean variable
bool_var = False
print('Boolean:', bool_var)

#Example of using the type() function to check data types
print(type(int_var))    # Output: <class 'int'>
print(type(float_var))  # Output: <class 'float'>
print(type(str_var))    # Output: <class 'str'>
print(type(bool_var))   # Output: <class 'bool'>

# Example of implicit type conversion
imp_result = int_var + float_var  # int is converted to float
print('Implicit Type Conversion (int + float):', imp_result)
print('Type after implicit conversion:', type(imp_result))  # Output: <class 'float'>

# Example of explicit type conversion
exp_result = int(float_var)  # To convert float to int
print('Explicit Type Conversion (float to int):', exp_result)
print('Type after explicit conversion:', type(exp_result))  # Output: <class 'int'>

# Example of input() function to get user input
age = input('Enter your age: ')
print('Your age after 10 years will be:', int(age) + 10)