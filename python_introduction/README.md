Introduction to Python
 Novice
 Weight: 1
 Project will start Dec 9, 2024 12:00 AM, must end by Dec 16, 2024 12:00 AM
 Checker was released at Dec 9, 2024 12:00 AM
 An auto review will be launched at the deadline


This project serves as a gentle introduction to the world of Python programming. You’ll explore what Python is, its applications, and gain practical experience setting up your development environment.

Additionally, you’ll delve into the basics of Python syntax, understanding its focus on readability and the importance of proper indentation.

Project Objectives:
By the end of this project, you should be able to:

Define what Python is and understand its key characteristics as a high-level programming language.
Identify various application areas where Python is commonly used.
Install Python on your system and set up a development environment to start writing Python code.
Explain the importance of indentation in Python code and how it contributes to code readability.
Write basic Python code following proper syntax guidelines.
This project lays the foundation for your Python programming journey, equipping you with the essential knowledge to begin writing simple Python programs and progress towards more complex concepts.

Tasks
0. Basic Arithmetic Exercise
mandatory
Objective: To practice basic arithmetic operations in Python by performing predefined calculations.

Task Description:

You are required to complete a Python script that performs basic arithmetic operations with two predefined numbers. The script should do the following:

Assign specific values to two variables, number1 and number2.
Perform addition, subtraction, and multiplication on these numbers.
Print the results of these operations in a human-readable format.
Instructions:

Create a file named basic_operations.py.
In this file, you will define two variables: number1 and number2, with the values 10 and 5, respectively.
You do not need to write any functions or import any modules.
Calculate the sum, difference (by subtracting number2 from number1), and product of number1 and number2.
Print the results of each operation in the format: [operation] of [number1] and [number2] is [result].
Expected Output:

When executed, your script should print the following (assuming number1 = 10 and number2 = 5):

How to execute

python3 basic_operations.py
Here is the outcome

Addition of 10 and 5 is 15
Subtraction of 10 and 5 is 5
Multiplication of 10 and 5 is 50
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: basic_operations.py
1. Simple Interest Calculator
mandatory
Objective: Apply basic Python arithmetic operations and variable assignments to calculate the simple interest on a given principal amount, rate of interest, and time.

Task Description:

Your task is to complete a Python script that calculates the simple interest earned on an investment over a period of time. The formula for simple interest is (I = P * R * T), where:

( I ) is the interest earned,
( P ) is the principal amount (initial investment),
( R ) is the annual interest rate (as a decimal),
( T ) is the time the money is invested for in years.
Instructions:

Create a file named simple_interest.py.
Define three variables in this file:
principal with a value of 1000 (representing $1000),
rate with a value of 0.05 (representing 5% annual interest rate),
time with a value of 3 (representing 3 years).
Calculate the simple interest using the formula provided and store the result in a variable named interest.
Print the calculated interest in a format: The simple interest is: [interest].
Expected Output:

When executed, your script should print the simple interest calculated with the provided values. For principal = 1000, rate = 0.05, and time = 3, the output should be:

The simple interest is: 150.0
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: simple_interest.py
2. Calculate the Area of a Rectangle
mandatory
Objective: Use basic Python arithmetic operations and variable assignments to calculate the area of a rectangle using its length and width.

Task Description:

For this task, you are to write a Python script that calculates the area of a rectangle. The area of a rectangle is found by multiplying its length by its width.

Instructions:

Create a file named rectangle_area.py.
Define two variables in this file:
length with a value representing the length of the rectangle.
width with a value representing the width of the rectangle.
For simplicity, let’s use length = 10 and width = 5.
Calculate the area of the rectangle using the formula (Area = length × width) and store the result in a variable named area.
Print the calculated area in a format: The area of the rectangle is: [area].
Expected Output:

When executed, your script, with the provided values (length = 10 and width = 5), should print the area of the rectangle:

The area of the rectangle is: 50
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: rectangle_area.py
3. Convert Hours to Seconds
mandatory
Objective: Demonstrate understanding of variable assignments and arithmetic operations by converting a given number of hours into seconds.

Task Description:

For this task, write a Python script that converts a specific number of hours into seconds. This task reinforces the concept of arithmetic operations within a practical context.

Instructions:

Create a file named hours_to_seconds.py.
Define a variable named hours and assign it a value representing the number of hours you want to convert to seconds. Use hours = 2.
Calculate the number of seconds in the given hours. Remember, there are 3600 seconds in an hour (since there are 60 minutes in an hour and 60 seconds in a minute, thus 60 x 60 = 3600).
Store the result of the conversion in a variable named seconds.
Print the result in the format: [hours] hour(s) is [seconds] seconds.
Expected Output:

Given the value hours = 2, your script should output:

2 hour(s) is 7200 seconds.
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: hours_to_seconds.py
4. User Input Age Calculator
mandatory
Objective: Practice receiving user input in Python and perform a simple arithmetic operation to calculate the user’s age in a future year.

Task Description:

Create a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.

Instructions:

Create a file named future_age_calculator.py.
Prompt the user to input their current age with the question: “How old are you? ”.
Assume the user will input a valid integer value.
Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.
Expected Script Flow:

The script prompts the user for their current age.
The user enters their age.
The script calculates and prints how old the user will be in 2050.
Example Interaction:

If the user inputs 30 when prompted for their current age, the output should be:

In 2050, you will be 57 years old.
Repo:

GitHub repository: alx_be_python
Directory: python_introduction
File: future_age_calculator.py
