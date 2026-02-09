Question 1: 
prompt: I have a function that finds the common elements between two lists. it takes the 2 lists and then returns the elements that is common in both of them into another list, it can be in any order at the end. What python data structure should I use?

Answer: For finding common elements between two lists, sets are the best choice in Python.
Here's why:
Set intersection: Sets have a built-in .intersection() method (or & operator) that efficiently finds common elements
Performance: Set operations are O(n) instead of O(n²) with nested loops
Automatic deduplication: Sets automatically remove duplicates
Order doesn't matter: Since you said the result can be in any order, sets are perfect




Question 2: 
prompt: I have an application that loads a list of user profiles from a database as a dictionary- each with their unique username, age, and an email. I will frequently need to pull the full profile by name and performance is important, what python data structure do i use?

Answer: Use a dictionary keyed by the user's name. Dictionaries provide average O(1) lookup time, which is much faster than scanning a list (O(n)). Converting the list into a dictionary makes repeated lookups efficient.




Question 3:
prompt: i have a function that takes in an input list and then returns a new list that contains only the even numbers. the order in the output list must be the same as the order in the input list. what python data structure or approach should i use and why?

Answer: Use a list (specifically a list comprehension). Lists preserve order, and a list comprehension allows filtering elements while keeping their original sequence. This is the simplest and most readable approach.
