#!/usr/bin/env python
# coding: utf-8

# In[46]:


#Taking operators in a list
operators= ['+','-','*','/']

#Taking user input
user_input= input('Enter input (Ex:2+3,2*3):')

# Removing spaces from the user input
user_input = user_input.replace(" ", "")

#Using indexing to take x, y and op values from users input
if len(user_input) < 3:
    print ('Invalid Input')
else:
    # Finding the index of the operator in the user input
    op_index = -1
    for i in range(len(user_input)):
        if user_input[i] in operators:
            op_index = i
            break
    # Checking if the operator is found
    if op_index == -1:
        print('Invalid Input')
    else:
        # Splitting the user input by the operator index
        x = float(user_input[:op_index])
        op = user_input[op_index]
        y = float(user_input[op_index + 1:])
    
#defining a simple calculator function 
def calc(x,op,y):
    if op not in operators:
        print('Invalid operators entered')
    if op in operators:
        if op == '+':
            print(x + y)
        elif op == '-':
            print(x - y)
        elif op == '*':
            print(x * y)
        elif op == '/':
            if y == 0:
                print("Can't divide by zero")
            else:
                print(x / y)
    
#Print the result by calling the function
result= calc(x, op, y)
if result is not None:
    print(result)


# In[ ]:





# In[ ]:




