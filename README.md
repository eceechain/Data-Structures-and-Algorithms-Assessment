# Data Structures and Algorithms Project

This project includes Python implementations for various functions related to stacks, sequences (lists/tuples), and dictionaries.

from stacks.balanced_parentheses import is_balanced

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

## Sequences (Lists/Tuples)

### Function: remove_duplicates(sequence)

Removes duplicates from the given sequence (list or tuple) while preserving the original order. Returns a new sequence without duplicates.

#### Usage

```python
from sequences.remove_duplicates import remove_duplicates

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

## Dictionaries

### Function: word_frequency(sentence)

Returns a dictionary containing the frequency of each word in the given sentence. Ignores punctuation and considers words in a case-insensitive manner.

#### Usage

```python
from dictionaries.word_frequency import word_frequency

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
```

### Installation

### To install the required dependencies, use the following command:

```bash
pipenv install
```
Usage

### Clone the repository and run the scripts as follows:

```bash
python stacks/balanced_parentheses.py
python sequences/remove_duplicates.py
python dictionaries/word_frequency.py
```
### Author

Jared Amima

### Email 
jaredamima4@.com 

### License

This project is licensed under the MIT License 