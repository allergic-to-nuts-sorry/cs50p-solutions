Solutions to Harvard's CS50: Programming with Python

Topics Covered:

Lecture 0: Functions and Variables
* escaping character (backslash)
* f-strings
* string methods
* type conversion

Lecture 1: Conditionals
* if, elif, else
* match-case
* return ... if .. else

Lecture 2: Loops

Lecture 3: Exceptions
* SyntaxError, ValueError, NameError
* try, except, else, pass, raise

Lecture 4: Libraries
* modules, packages, __init__.py
* import, from
* random - randint, shuffle
* sys - .argv, .exit()
* PyPI, pip
* APIs, requests library, .get(), .json()

Lecture 5: Unit Tests
* assert, AssertionError
* pytest

Lecture 6: File I/O
* with open(filename, mode) as f: (default mode "r")
* .readlines(), .write()
* for line in file
* sorted function, its key argument
* lambda functions (lambda student, x ,y: student["name"] + x + y)
* csv library
* reader = csv.reader(file)
* reader = csv.DictReader()
* writer = csv.writer(file), writer.writerow([name,home])
* writer = csv.DictWriter(file, fieldnames = ["name","home"]), writer.writerow({"name":name,"home":home})
* Images, PIL library

Lecture 7: regex
* ., *, +, ?, {m}, {m,n}
* start, end: ^,$
* re.IGNORECASE argument (also .MULTILINE and .DOTALL)
* [...], [^...]
* \ escape characted
* \d, \D, \w, \W, \b, \B, \s, \S
* A|B, (...), (?...)
* re.search(), .match, .fullmatch, .sub
* walrus operator :=

Lecture 8: Object Oriented Programming
* __init__(self,...), __str__(...)
* @Property- takes self, returns property value, @PropertyName.setter- takes self and property value and assigns it
* private variables- e.g. _house
* @classmethod, @staticmethod
* Inheritence- super().__init__(eg name) has to be in __init__ fn of child
* Operator Overloading- e.g. def__add__(e.g. self, others), def __sub__(...)

Lecture 9: Et Cetera
* set
* global
* type hints - def meow(n: int)-> str:
* Docstrings (fn explanation comment in code)
* argparse
* unpacking lists using *
* unpacking dicts using **
* *args, **kwargs
* map: e.g. uppercased = map(str.upper, words)
* list comprehensions - e.g. [word.upper() for word in words]
* filter: e.g. gryfs = filter(is_gryf, students)
* Dict Comprehenions - e.g. gryfs = [{"name":n , "house":"gryf"} for n in students]
* enumerate
* Generators, yield, Iterators
