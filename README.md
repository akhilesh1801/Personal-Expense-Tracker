# Personal Expense Tracker (Python)

## About this project

This is a simple Python program I made to keep track of daily expenses. The idea was to have something basic where I can enter what I spent, see all entries later, and get a rough idea of how much money is going out.

I didn’t use any external libraries, just basic Python, so it can run anywhere easily (like Jupyter Notebook or any Python IDE).


## What it does

* Add new expenses (item, amount, category)
* Store data in a file
* View all saved expenses
* Calculate total money spent
* Show spending based on category (food, travel, other)
* Check if spending crosses a basic budget limit


## How to run

1. Open Jupyter Notebook or any Python editor
2. Copy the code into a file 
3. Run the program
4. Use the menu options by typing numbers


## Example usage

* Choose option `1` to add an expense

* Enter details like:

  * what you bought
  * how much you spent
  * category

* Use option `2` to view all entries

* Use option `3` to see total spending


## File storage

All data is stored in a file called:


Each entry is saved in this format:

item | amount | category


## Limitations

* No advanced error checking (basic input only)
* Categories are fixed (food, travel, other)
* Budget is hardcoded (5000)


## What I learned

* File handling in Python
* Using loops and conditions
* Organizing code into functions
* Basic menu-driven programs


## Future improvements

If I improve this later, I would:

* Add better input validation
* Allow custom categories
* Add monthly summaries
* Maybe create a simple UI


