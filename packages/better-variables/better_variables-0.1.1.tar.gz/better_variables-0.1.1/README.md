# Better Variables
Better Variables is a simple project aiming to offer a better way to manage variables in your projects. It is a simple and easy-to-use library that allows you to manage your variables in a more organized way, adding descriptions, custom function assignation and much more.
## Installation
```bash
pip install better-variables
```
## Usage
```python
from better_variables import BetterVariable

# Create a new variable
my_var = BetterVariable("Hello World", description="This is my variable")

def reverse_string(value):
    return value[::-1]

# Now you can apply a custom function to the variable
my_var_2 = my_var @ reverse_string

# Get the value of the variable
print(my_var_2) # dlroW olleH

# Print the entire variable
print(my_var)
# Variable name: my_var
# Variable type: <class 'str'>
# Variable value: Hello World
# Variable description: This is my variable
```