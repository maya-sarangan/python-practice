To test the student's mastery of the **Python Basics** curriculum—including variables, strings, mathematical operations, booleans, conditionals, and functions—here is a set of 

**50 command-line-based programming assignments**.
These are designed to be more challenging than standard introductory exercises, pushing the student to think critically about logic and data flow without using external video game libraries.

### **Variables and Data Types**
1.  **Variable Swap:** Write a script that takes two inputs, `a` and `b`, and swaps their values.

2.  **Bio-Data Collector:** Create a program that asks for a name, age, and height. Print a single sentence using all three, ensuring the age is an integer and height is a float.

3.  **Data Type Identifier:** Write a program where the student assigns five different types of data (string, int, float, boolean, list) to variables and prints the `type()` of each.

4.  **Personalized Greeting Logic:** Ask for a first name and last name. Print them in "Last, First" format, all in uppercase.

5.  **Constant Challenge:** Define a variable `PI = 3.14159`. Ask the user for a radius and calculate the circumference, but ensure `PI` cannot be changed by the user input.

6.  **The "About Me" Dict:** (Preparation for later topics) Store five facts about yourself in variables and print them in a formatted table layout using only spaces and pipes (`|`).

7.  **Dynamic Story:** Create a "Mad Libs" game with 10 variables that the user must fill in before the final story is revealed.

8.  **Age in Seconds:** Ask for the user's age in years and calculate approximately how many seconds they have been alive.

9.  **Budget Tracker:** Ask for a starting balance and three separate expenses. Subtract the expenses and display the remaining balance with a dollar sign.

10. **Type Error Fixer:** Provide a script that intentionally adds a string and an integer. The student must use type casting (e.g., `str()` or `int()`) to fix it so it prints "The total is 10".

### **Strings and Text Manipulation**
11. **Reverse Name:** Take a user's name and print it backwards.

12. **The "Secret" Index:** Ask for a long sentence and a number. Print the character at that specific index location.

13. **Vowel Counter:** Take a string and count how many times the letter 'a' appears (using string methods, not loops yet).

14. **Word Replacer:** Ask for a sentence, a word to find, and a word to replace it with. Print the modified sentence.

15. **Email Formatter:** Ask for a name and a domain. Generate an email address: `firstname.lastname@domain.com` in all lowercase.

16. **String Slicer:** Take a word and print only the first three and last three letters combined.

17. **Space Remover:** Ask for a sentence with accidental leading/trailing spaces and print it "cleaned up" using `.strip()`.

18. **Acronym Creator:** Take three words (like "Central Intelligence Agency") and print the first letter of each in uppercase.

19. **Palindrome Checker (Basic):** Ask for a word and check if it is the same when reversed using string slicing `[::-1]`.

20. **Caesar Cipher Prep:** Take a word and shift every letter one step forward in the alphabet (e.g., "abc" becomes "bcd") using `ord()` and `chr()`.

### **Numbers and Mathematical Operations**
21. **Bill Splitter (Advanced):** Ask for the bill total, the tip percentage, and the number of people. Calculate the total per person, rounded to 2 decimal places.

22. **Exponent Calculator:** Ask for a base number and an exponent number. Calculate the result without using the `**` operator (use `pow()`).

23. **Temperature Converter:** Create a program that converts Celsius to Fahrenheit and Kelvin.

24. **Area of a Triangle:** Ask for the base and height, then calculate the area using the formula (0.5 * b * h).

25. **Floor and Modulo:** Ask for two numbers. Print the result of floor division (`//`) and the remainder (`%`).

26. **Time Converter:** Ask for a number of minutes and convert it into "X hours and Y minutes."

27. **Compound Interest:** Ask for principal, rate, and time. Calculate the final amount using the formula $A = P(1 + r)^t$.

28. **Quadratic Tool (Simple):** Ask for `a`, `b`, and `c` and calculate the discriminant ($b^2 - 4ac$).

29. **BMI Calculator:** Ask for weight (kg) and height (m). Calculate the Body Mass Index and print the raw number.

30. **Rounding Challenge:** Ask for a long decimal and a "precision" number. Round the decimal to that many places.

### **Booleans and Conditionals**
31. **The Bouncer:** Ask for an age. If 18+, print "Welcome"; if 13-17, "Bring a parent"; if under 13, "Access denied".

32. **Even or Odd:** Take a number and use the modulo operator to tell the user if it is even or odd.

33. **Grading System:** Ask for a score (0-100). Print A, B, C, D, or F based on standard ranges.

34. **Leap Year Checker:** Ask for a year and determine if it is a leap year using nested `if` statements.

35. **Login Simulator:** Create a "hardcoded" username and password. Ask the user to log in. Tell them if the username is wrong, the password is wrong, or both are correct.

36. **Movie Ticket Booking:** Ask for age and the time of day. Morning tickets are $5, adult evening is $12, and senior evening is $8.

37. **Password Strength:** Ask for a password. If it is shorter than 8 characters, print "Too short."

38. **Calculator (CLI):** Ask for two numbers and an operator (+, -, *, /). Perform the correct math based on the input.

39. **Rock, Paper, Scissors (Logic Only):** Take two inputs (Player 1 and Player 2) and print who wins.

40. **Range Tester:** Ask for a number. Check if it is between 1 and 100 (inclusive) and also check if it is a multiple of 5.

### **Functions and Scope**
41. **Greeting Function:** Write a function called `greet_user(name)` that prints a customized welcome.

42. **Area Function:** Create a function that takes `length` and `width` and returns the area of a rectangle.

43. **Apply Discount:** Write a function that takes a price and a discount percentage, then returns the new price.

44. **Currency Converter Function:** Write a function that converts Dollars to Euros based on a set exchange rate.

45. **Global vs. Local:** Create a global variable `balance`. Write a function that tries to change it and explain why it requires the `global` keyword.

46. **The Validator:** Write a function that returns `True` if a string contains an '@' symbol and `False` otherwise.

47. **Max of Three:** Write a function that takes three numbers as arguments and returns the largest one without using the `max()` built-in.
48. **RPG Character Stats:** Write a function that generates a "Character Profile" string based on input parameters (name, class, strength).
49. **Circle Tool Function:** Write a function that returns both the area and the circumference of a circle as a tuple.
50. **Unit Tester:** Write a function that takes two inputs and a "target" result. It should print "Pass" if the inputs added together equal the target, and "Fail" otherwise.

***
