# Python Bootcamp

This repository is used to store stuff related to me learning Python from the course [The Modern Python 3 Bootcamp](https://www.udemy.com/the-modern-python3-bootcamp/learn/v4/t/lecture/9166920?start=0) at Udemy.com.

## Dictionaries

Like objects in JavaScript. Key-value pairs. Unordered (no index) and there can't be duplicates in the keys.

Example:

```python
  { 'name': 'hanna'}
```

## Tuples

A list of items that are unique and immutable. Can be used as keys in a dictionary.

Example:

```python
  # Tuple
  (23.14323, 25.2435)

  # Tuple used as key in a Dictionary
  {
    (23.14323, 25.2435): 'Coordinates to home'
  }
```

## Sets

Sort of like objects in JavaScript, but without pairing, just elements, with no index and no duplicates.

Example:

```python
  { 1, 2, 3, 4 }
```

| Command | What it does                                                 |
| :-----: | ------------------------------------------------------------ |
|  `\|`   | Joins two sets together, with no duplicates.                 |
|   `&`   | Intersection of two sets, returns items that exists in both. |

## Functions

Use `def` to define a function.

Example:

```python
# Defining function
def my_function ():
  # do stuff

# Using function
myFunction()
```

### \*args

Using `*args` collects the remaining arguments in a function into a tuple.

Example:

```python
def sum_all_nums (*args):
  total = 0
  for num in args:
    total += num
  return total

sum_all_nums(12, 14, 6)
# returns 32
```

### \*\*kwargs

Gathers remaining arguments as a dictionary.

Example:

```python
def fav_colors (**kwargs):
  return kwargs

fav_colors(first="purple", second="white", third="red")

# returns
# { "first": "purple", "second"="white", "third"="red" }
```
