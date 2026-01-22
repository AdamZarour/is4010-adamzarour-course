Problem 1: Debugging
My Prompt:
Context: I am a student in an AI development class working on a Python function that is supposed to sum even numbers, but it is returning the wrong results.
Persona: Act as a Senior Python Developer and mentor. 
Task: Please analyze the provided code, identify the logical error, and provide a fixed version of the function. 
Format: Provide the corrected code in a Python code block and a brief, bulleted explanation of what was wrong and how you fixed it.
Code:
def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total

AI corrected code:
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Changed from 1 to 0 to target even numbers
            total += num
    return total

What I Learned: I learned that the modulo operator returns the remainder of a division. The original code was checking for num % 2 == 1, which identifies odd numbers. By changing the condition to num % 2 == 0, the function correctly identifies numbers that are perfectly divisible by 2 (even numbers).





Problem 2: Refactoring
My prompt:
Context:I am a student working on my ai app development class assignment. we were given a code that runs but isnt the neatest and easy to follow along. 
Persona: Take on the role of a senior python developer and mentor. 
Task: Please refactor this code to be more clear, consice, and idiomatic. 
Format: Provide the corrected code in a Python code block and a brief, bulleted explanation of what was wrong and how you fixed it.

code: 
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```

AI corrected code: 
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user['name'] for user in users if user['age'] >= 18]

What I Learned: I learned that the original code was "un-Pythonic" because it used unnecessary indexing with range(len()) to iterate through the list. By refactoring it into a list comprehension, I made the code more idiomatic, readable, and efficient by combining the loop, the conditional check, and the list creation into a single line.



Problem 3: Documenting
My prompt: 
Context: I am a student taking an AI app development class. I was given a fully working python code with no documentation. 
Persona: I need you to take on the role of a senior deveoper and mentor. 
Task: Please create a professional Numpy-style docstring for this function. 
Format: Provide the code with the new docstring included in a Python code block.

Code:
def calculate_area(length, width):
if length <= 0 or width <= 0:
raise ValueError("Length and width must be positive numbers.")
return length * width

AI corrected code: 
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Computes the area of a rectangle given its length and width.
    Both dimensions must be positive numbers.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be a positive number.
    width : float or int
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float or int
        The area of the rectangle (length × width).

    Raises
    ------
    ValueError
        If length or width is less than or equal to zero.

    Examples
    --------
    >>> calculate_area(5, 4)
    20
    >>> calculate_area(3.5, 2)
    7.0
    >>> calculate_area(-5, 4)
    Traceback (most recent call last):
        ...
    ValueError: Length and width must be positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width