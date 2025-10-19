# DECISIONS.md

## Why I refactored the loops into comprehensions
The original script used for loops with `append` and manual string concatenation.  
I replaced them with list comprehensions and the `join()` method because they make the code easier to read and more Pythonic.  
A comprehension clearly shows that the function’s purpose is to transform a collection and return the result, instead of building it piece by piece.  

In `transform_numbers`, the condition for even vs odd is visible in one clean expression, making it much easier to follow at a glance.  
In `process_strings`, `" ".join([...])` avoids inefficient string concatenation and makes the output behavior obvious in a single line.  
Both of these changes make the logic compact, efficient, and easier for anyone else to modify or extend.

---

## Why I renamed functions and variables
The old names (`do_math_stuff`, `do_string_stuff`, `list_of_nums`, etc.) didn’t tell me *what* the code was doing — only that it was “doing stuff.”  
I changed them to descriptive, PEP 8–friendly names like `transform_numbers`, `process_strings`, and `numbers`.  
These names make the code self-documenting and improve readability for anyone working on it later.  

I also added type hints (`List[int]`, `List[str]`) so editors and linters can help catch mistakes early.  
That’s the kind of polish that makes a script feel professional.

---

## Why I added docstrings and comments
Every function now has a PEP 257 docstring explaining what it does, its parameters, and what it returns.  
This is the kind of documentation that lets someone use or test the functions without even opening the full file.  

I kept inline comments minimal and only used them where the logic might not be obvious at first glance.  
The goal was to make the code readable *without* relying on a ton of extra notes.  

Overall, these changes make the script look cleaner, easier to maintain, and more professional for future collaboration.
