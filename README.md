# Python: The Complete Developer Guide

> From zero to job-ready. Fundamentals, project structure, automation, data, databases, REST APIs, web backends, testing, and deployment, in one place.

**Who this is for:** beginners who want a full path, and working developers who want a solid reference.
**Python version:** 3.12 or newer (examples use modern syntax such as `str | None` and `match`).

---

## Table of Contents

1. [How to Use This Guide](#1-how-to-use-this-guide)
2. [Setup & Environment](#2-setup--environment)
3. [Fundamentals](#3-fundamentals)
4. [Intermediate Python](#4-intermediate-python)
5. [Project Structure & Tooling](#5-project-structure--tooling)
6. [Automation & Scripting](#6-automation--scripting)
7. [Working with Data](#7-working-with-data)
8. [Databases](#8-databases)
9. [REST APIs & Web Backends](#9-rest-apis--web-backends)
10. [Testing](#10-testing)
11. [Deployment](#11-deployment)
12. [Best Practices & Security](#12-best-practices--security)
13. [Cheat Sheets](#13-cheat-sheets)
14. [Practice Projects](#14-practice-projects)
15. [Job-Ready Roadmap & Checklist](#15-job-ready-roadmap--checklist)
16. [Resources](#16-resources)

---

## 1. How to Use This Guide

- Read in order if you are new. Skip to a section if you already know the basics.
- **Type every example yourself.** Copy-pasting teaches very little.
- After each section, build something small with it. Reading alone does not make you a developer.
- When something breaks, read the error from the **bottom up**: the last line tells you what went wrong, the lines above show where.

### What "job-ready" means

| Area | You can... |
|---|---|
| Core Python | Write clean functions, classes, and modules; handle errors; read/write files |
| Tooling | Use virtual environments, Git, a linter, and a formatter |
| Data & automation | Script repetitive tasks, call APIs, process CSV/JSON |
| Databases | Write SQL, use an ORM, design simple schemas |
| Backend | Build and document a REST API with auth and validation |
| Quality | Write automated tests and run them in CI |
| Delivery | Containerize and deploy an app with environment-based config |

---

## 2. Setup & Environment

### Install Python

Download from [python.org](https://www.python.org/downloads/) or use your OS package manager. Verify:

```bash
python --version      # on some systems: python3 --version
pip --version
```

### Run Python

```bash
python                # interactive shell (REPL), exit with exit() or Ctrl+D
python script.py      # run a file
python -m module      # run a module
```

### Virtual environments (always use one)

A virtual environment isolates a project's dependencies so projects don't conflict.

```bash
python -m venv .venv

# Activate
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows (cmd / PowerShell)

# Install and record dependencies
pip install requests
pip freeze > requirements.txt
pip install -r requirements.txt  # recreate the environment elsewhere

deactivate                       # leave the environment
```

Add `.venv/` to `.gitignore`. Never commit it.

### Modern alternative: `uv`

[`uv`](https://docs.astral.sh/uv/) is a fast, all-in-one project and package manager.

```bash
uv init my-project
cd my-project
uv add requests fastapi
uv add --dev pytest ruff
uv run main.py
```

### Editor

VS Code (with the Python and Pylance extensions) or PyCharm. Turn on format-on-save and linting from day one.

---

## 3. Fundamentals

### 3.1 Hello, Python

```python
print("Hello, world!")
```

Python uses **indentation** (4 spaces) instead of braces to define blocks. Comments start with `#`.

### 3.2 Variables & Data Types

```python
name = "Ada"          # str
age = 30              # int
height = 1.68         # float
is_dev = True         # bool
nothing = None        # NoneType

print(type(age))      # <class 'int'>
```

Variables are labels pointing to objects. There are no declarations and types are checked at runtime (dynamic typing).

**Naming:** `snake_case` for variables and functions, `PascalCase` for classes, `UPPER_CASE` for constants.

### 3.3 Type Conversion

```python
int("42")        # 42
float("3.14")    # 3.14
str(100)         # "100"
bool(0)          # False
list("abc")      # ['a', 'b', 'c']
```

**Falsy values:** `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`. Everything else is truthy.

### 3.4 Operators

```python
10 + 3    # 13
10 - 3    # 7
10 * 3    # 30
10 / 3    # 3.3333...  (always float)
10 // 3   # 3          (floor division)
10 % 3    # 1          (remainder)
2 ** 10   # 1024       (power)

x = 5
x += 1    # also -=, *=, /=, //=, %=, **=

# Comparison: == != < > <= >=
# Logical:    and  or  not
# Membership: in   not in
# Identity:   is   is not   (use `is None`, not `== None`)

1 < x < 10   # chained comparison works
```

### 3.5 Strings

```python
s = "Python"
s[0]        # 'P'
s[-1]       # 'n'
s[1:4]      # 'yth'   (start inclusive, stop exclusive)
s[::-1]     # 'nohtyP' (reverse)
len(s)      # 6

# f-strings (preferred formatting)
name, score = "Ada", 93.456
print(f"{name} scored {score:.1f}")        # Ada scored 93.5
print(f"{1_000_000:,}")                    # 1,000,000
print(f"{name!r:>10}")                     # right-aligned repr

# Common methods (strings are immutable, methods return new strings)
"  hi  ".strip()           # 'hi'
"a,b,c".split(",")         # ['a', 'b', 'c']
",".join(["a", "b", "c"])  # 'a,b,c'
"hello".upper()            # 'HELLO'
"hello".replace("l", "L")  # 'heLLo'
"hello".startswith("he")   # True
"hello".find("l")          # 2  (-1 if missing)

# Multi-line strings
text = """Line one
Line two"""
```

### 3.6 Input & Output

```python
name = input("Your name: ")      # always returns str
age = int(input("Your age: "))   # convert yourself
print("Hello", name, sep=" - ", end="!\n")
```

### 3.7 Collections

| Type | Syntax | Ordered | Mutable | Duplicates | Use for |
|---|---|---|---|---|---|
| `list` | `[1, 2, 3]` | Yes | Yes | Yes | Sequences you change |
| `tuple` | `(1, 2, 3)` | Yes | No | Yes | Fixed records |
| `dict` | `{"a": 1}` | Yes (insertion) | Yes | Unique keys | Lookups by key |
| `set` | `{1, 2, 3}` | No | Yes | No | Uniqueness, set math |

```python
# list
nums = [3, 1, 2]
nums.append(4)
nums.insert(0, 10)
nums.remove(1)
last = nums.pop()
nums.sort()                  # in place
sorted_copy = sorted(nums, reverse=True)

# tuple (and unpacking)
point = (3, 4)
x, y = point
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2, 3, 4]

# dict
user = {"name": "Ada", "age": 30}
user["email"] = "ada@example.com"
user.get("phone", "n/a")     # safe lookup with default
for key, value in user.items():
    print(key, value)
merged = user | {"age": 31}  # merge (3.9+)

# set
a, b = {1, 2, 3}, {3, 4}
a & b   # {3}        intersection
a | b   # {1, 2, 3, 4} union
a - b   # {1, 2}     difference
```

### 3.8 Control Flow

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# Ternary
label = "pass" if score >= 60 else "fail"

# match (3.10+): structural pattern matching
command = "stop"
match command:
    case "start":
        print("Starting")
    case "stop" | "halt":
        print("Stopping")
    case _:
        print("Unknown")
```

### 3.9 Loops

```python
for i in range(5):                 # 0..4
    print(i)

for i in range(2, 10, 2):          # 2, 4, 6, 8
    print(i)

fruits = ["apple", "banana"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

for a, b in zip([1, 2, 3], ["x", "y", "z"]):
    print(a, b)

count = 0
while count < 3:
    count += 1
    if count == 2:
        continue                   # skip rest of this iteration
    print(count)

for n in range(10):
    if n == 5:
        break                      # exit loop
else:
    print("only runs if no break happened")
```

### 3.10 Functions

```python
def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting. (This is a docstring.)"""
    return f"{greeting}, {name}!"

greet("Ada")                       # positional
greet(greeting="Hi", name="Ada")   # keyword

# *args and **kwargs
def total(*numbers: float) -> float:
    return sum(numbers)

def show(**options):
    for key, value in options.items():
        print(key, value)

# Keyword-only and positional-only parameters
def connect(host, /, port, *, timeout=5): ...

# Multiple return values (really a tuple)
def min_max(values):
    return min(values), max(values)

low, high = min_max([3, 1, 4])

# Lambda: small anonymous functions
square = lambda x: x * x
sorted(["bb", "a", "ccc"], key=lambda s: len(s))
```

**Classic pitfall: mutable default arguments**

```python
# Bad: the same list is shared across calls
def add_item(item, items=[]):
    items.append(item)
    return items

# Good
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 3.11 Comprehensions

```python
squares = [n * n for n in range(10)]
evens = [n for n in range(10) if n % 2 == 0]
lookup = {word: len(word) for word in ["a", "bb", "ccc"]}
unique_lengths = {len(word) for word in ["a", "bb", "cc"]}
lazy = (n * n for n in range(10**9))   # generator expression: no memory blowup
```

### 3.12 Scope (LEGB)

Python looks up names in this order: **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in.

```python
count = 0

def increment():
    global count      # avoid when you can; prefer returning values
    count += 1
```

---

## 4. Intermediate Python

### 4.1 Error Handling

```python
try:
    value = int(input("Number: "))
    result = 10 / value
except ValueError:
    print("That's not a number")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as exc:          # last resort, never use a bare `except:`
    print(f"Unexpected: {exc}")
else:
    print(result)                 # runs only if no exception
finally:
    print("Always runs (cleanup)")

# Raise your own
def set_age(age: int):
    if age < 0:
        raise ValueError("age must be non-negative")

# Custom exceptions
class InsufficientFunds(Exception):
    """Raised when a withdrawal exceeds the balance."""
```

### 4.2 Files & Context Managers

```python
from pathlib import Path

# Always use `with`: it closes the file even if an error occurs
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")

with open("notes.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# pathlib is the modern way to handle paths
path = Path("data") / "notes.txt"
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text("hello", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
print(path.exists(), path.suffix, path.stem)
```

**JSON & CSV**

```python
import json, csv

data = {"name": "Ada", "skills": ["python", "sql"]}
Path("data.json").write_text(json.dumps(data, indent=2))
loaded = json.loads(Path("data.json").read_text())

with open("people.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["age"])
```

**Write your own context manager**

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.3f}s")

with timer("work"):
    sum(range(1_000_000))
```

### 4.3 Modules & Packages

```python
# utils.py
def slugify(text: str) -> str:
    return text.lower().replace(" ", "-")

# main.py
import utils
from utils import slugify
from utils import slugify as make_slug
import math, random, datetime as dt, collections, itertools, functools
```

- A **module** is a `.py` file. A **package** is a folder of modules (usually with `__init__.py`).
- `if __name__ == "__main__":` runs code only when the file is executed directly, not when imported.

```python
def main():
    print("running")

if __name__ == "__main__":
    main()
```

### 4.4 Object-Oriented Programming

```python
class BankAccount:
    interest_rate = 0.02                      # class attribute (shared)

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner                    # instance attributes
        self._balance = balance               # _ = "internal, please don't touch"

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def __repr__(self) -> str:                # for developers
        return f"BankAccount({self.owner!r}, {self._balance})"

    def __str__(self) -> str:                 # for users
        return f"{self.owner}: ${self._balance:,.2f}"

    @classmethod
    def from_string(cls, text: str) -> "BankAccount":   # alternative constructor
        owner, balance = text.split(":")
        return cls(owner, float(balance))

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return amount > 0


# Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.03):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self._balance * self.rate)
```

**Prefer composition over deep inheritance.** Use inheritance for true "is-a" relationships only.

**Dataclasses** remove the boilerplate for data-holding classes:

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)          # frozen = immutable
class Item:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)
```

**Useful dunder methods:** `__len__`, `__getitem__`, `__iter__`, `__eq__`, `__lt__`, `__enter__`/`__exit__`, `__call__`.

### 4.5 Type Hints

Hints are not enforced at runtime, but editors and tools like `mypy` use them to catch bugs early.

```python
from typing import Optional, Callable, Any

def find_user(user_id: int) -> dict[str, Any] | None: ...
def apply(func: Callable[[int], int], value: int) -> int: ...
names: list[str] = []
scores: dict[str, float] = {}
```

### 4.6 Iterators & Generators

```python
def countdown(n: int):
    while n > 0:
        yield n          # pauses here, resumes on next()
        n -= 1

for x in countdown(3):
    print(x)             # 3 2 1

# Read huge files without loading them into memory
def read_lines(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")
```

### 4.7 Decorators

A decorator wraps a function to add behavior.

```python
import functools, time

def timer(func):
    @functools.wraps(func)                 # preserves name and docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def slow():
    time.sleep(0.1)
```

### 4.8 Useful Standard Library

```python
from collections import Counter, defaultdict, deque
from itertools import chain, groupby, islice
from functools import lru_cache, partial
import re, os, sys, subprocess, logging, datetime as dt, uuid, secrets, pathlib

Counter("mississippi").most_common(2)      # [('i', 4), ('s', 4)]

groups = defaultdict(list)
groups["fruits"].append("apple")

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)

now = dt.datetime.now(dt.timezone.utc)     # always prefer timezone-aware datetimes
```

### 4.9 Async Basics

Use `async` for I/O-bound work (network calls, databases) that spends time waiting. It does not speed up CPU-heavy work.

```python
import asyncio

async def fetch(n: int) -> int:
    await asyncio.sleep(1)        # pretend network call
    return n * 2

async def main():
    results = await asyncio.gather(fetch(1), fetch(2), fetch(3))
    print(results)                # [2, 4, 6] in ~1 second, not 3

asyncio.run(main())
```

### 4.10 Concurrency at a Glance

| Need | Use |
|---|---|
| Many network/disk waits | `asyncio` or `threading` |
| CPU-heavy parallel work | `multiprocessing` / `concurrent.futures.ProcessPoolExecutor` |
| Simple thread pool | `concurrent.futures.ThreadPoolExecutor` |

---

## 5. Project Structure & Tooling

### Recommended layout

```
my_project/
├── pyproject.toml          # project metadata, dependencies, tool config
├── README.md
├── .gitignore
├── .env.example            # documents required env vars (no real secrets)
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py         # entry point
│       ├── config.py       # settings from env vars
│       ├── models.py       # data models / DB models
│       ├── services/       # business logic
│       └── utils.py
├── tests/
│   ├── conftest.py         # shared fixtures
│   └── test_main.py
└── scripts/                # one-off helper scripts
```

Keep **business logic** separate from **I/O** (web routes, CLI, database). Logic that doesn't touch the outside world is easy to test.

### `pyproject.toml`

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["fastapi[standard]", "sqlalchemy", "python-dotenv"]

[project.optional-dependencies]
dev = ["pytest", "pytest-cov", "ruff", "mypy"]

[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### Quality tools

```bash
pip install ruff mypy pytest
ruff check .          # lint
ruff format .         # format
mypy src              # static type check
pytest                # tests
```

### Configuration with environment variables

Never hard-code secrets. Load them from the environment.

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()   # reads a local .env file (which is git-ignored)

DATABASE_URL = os.environ["DATABASE_URL"]            # required: fails loudly if missing
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
```

```bash
# .env (never commit)
DATABASE_URL=sqlite:///app.db
DEBUG=true
SECRET_KEY=change-me
```

### Logging (use it instead of `print`)

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

logger.info("Starting up")
logger.warning("Disk almost full")
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("Calculation failed")   # includes the traceback
```

### Git essentials

```bash
git init
git add .
git commit -m "Add user model"
git switch -c feature/login
git push -u origin feature/login
```

Write small commits with clear messages. A good `.gitignore` for Python includes `.venv/`, `__pycache__/`, `.env`, `*.pyc`, `.pytest_cache/`, `dist/`.

---

## 6. Automation & Scripting

Python shines at automating repetitive work.

### Command-line tools with `argparse`

```python
import argparse
from pathlib import Path
import shutil

CATEGORIES = {
    ".jpg": "Images", ".png": "Images",
    ".pdf": "Documents", ".docx": "Documents",
    ".zip": "Archives",
}

def organize(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_file():
            category = CATEGORIES.get(item.suffix.lower(), "Other")
            target = folder / category
            target.mkdir(exist_ok=True)
            shutil.move(str(item), target / item.name)

def main() -> None:
    parser = argparse.ArgumentParser(description="Sort files into folders by type")
    parser.add_argument("folder", type=Path)
    args = parser.parse_args()
    organize(args.folder)

if __name__ == "__main__":
    main()
```

Run: `python organize.py ~/Downloads`. For richer CLIs, look at **Typer** or **Click**.

### Calling web APIs with `requests`

```python
import requests

resp = requests.get(
    "https://api.github.com/users/octocat",
    headers={"Accept": "application/vnd.github+json"},
    timeout=10,                 # always set a timeout
)
resp.raise_for_status()         # raises on 4xx/5xx
data = resp.json()
print(data["public_repos"])

# POST JSON
requests.post("https://httpbin.org/post", json={"hello": "world"}, timeout=10)
```

Use `requests.Session()` when making many calls to the same host. For async code, use `httpx`.

### Web scraping (be respectful)

Check the site's terms of service and `robots.txt`, rate-limit your requests, and prefer an official API when one exists.

```python
import requests
from bs4 import BeautifulSoup

html = requests.get("https://example.com", timeout=10).text
soup = BeautifulSoup(html, "html.parser")

for link in soup.select("a[href]"):
    print(link.get_text(strip=True), link["href"])
```

JavaScript-rendered pages need a browser tool such as **Playwright**.

### Regular expressions

```python
import re

text = "Contact: ada@example.com, grace@example.org"
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)

m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2026-10-28")
if m:
    year, month, day = m.groups()

re.sub(r"\s+", " ", "too    many   spaces")   # 'too many spaces'
```

### Running other programs

```python
import subprocess

result = subprocess.run(
    ["git", "status", "--short"],
    capture_output=True, text=True, check=True,
)
print(result.stdout)
```

Pass a **list** of arguments, not a single string with `shell=True`, to avoid command injection.

### Scheduling

- **cron** (Linux/macOS) or **Task Scheduler** (Windows) run your script on a schedule.
- `schedule` library for simple in-process jobs.
- **GitHub Actions** with a `schedule:` trigger is a free way to run periodic scripts in the cloud.

```cron
# Every day at 08:00
0 8 * * * /path/to/.venv/bin/python /path/to/script.py
```

### Sending email (standard library)

```python
import smtplib, os
from email.message import EmailMessage

msg = EmailMessage()
msg["From"], msg["To"], msg["Subject"] = "me@example.com", "you@example.com", "Report"
msg.set_content("Your daily report is attached.")

with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
    server.login("me@example.com", os.environ["SMTP_PASSWORD"])
    server.send_message(msg)
```

---

## 7. Working with Data

### pandas essentials

```bash
pip install pandas matplotlib
```

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df.head()                         # first rows
df.info()                         # columns, types, nulls
df.describe()                     # summary statistics

df["total"] = df["qty"] * df["price"]            # new column
big = df[df["total"] > 1000]                     # filter rows
df = df.dropna(subset=["region"])                # drop rows with missing region
df["date"] = pd.to_datetime(df["date"])

summary = (
    df.groupby("region")["total"]
      .sum()
      .sort_values(ascending=False)
)

df.to_csv("clean.csv", index=False)
```

**Joins:**

```python
merged = orders.merge(customers, on="customer_id", how="left")
```

### Quick charts

```python
import matplotlib.pyplot as plt

summary.plot(kind="bar", title="Revenue by region")
plt.tight_layout()
plt.savefig("revenue.png", dpi=150)
```

### Data-cleaning checklist

1. Inspect: `info()`, `describe()`, `value_counts()`
2. Fix types (dates, numbers stored as text)
3. Handle missing values deliberately (drop, fill, or flag)
4. Remove duplicates: `df.drop_duplicates()`
5. Standardize text: `df["name"].str.strip().str.title()`
6. Validate: assert totals, ranges, and uniqueness

For numerical work see **NumPy**. For larger-than-memory data look at **Polars** or **DuckDB**.

---

## 8. Databases

### SQL you must know

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (email, name) VALUES ('ada@example.com', 'Ada');

SELECT id, name FROM users WHERE name LIKE 'A%' ORDER BY created_at DESC LIMIT 10;

UPDATE users SET name = 'Ada L.' WHERE id = 1;
DELETE FROM users WHERE id = 1;

-- Joins and aggregates
SELECT u.name, COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id
HAVING COUNT(o.id) > 2;
```

**Core concepts:** primary keys, foreign keys, indexes, normalization, transactions (ACID), one-to-many vs many-to-many relationships.

### `sqlite3` (built in)

```python
import sqlite3

conn = sqlite3.connect("app.db")
conn.row_factory = sqlite3.Row            # access columns by name
try:
    with conn:                            # commits on success, rolls back on error
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL)"
        )
        conn.execute("INSERT INTO users (email) VALUES (?)", ("ada@example.com",))
    rows = conn.execute("SELECT id, email FROM users").fetchall()
    for row in rows:
        print(row["id"], row["email"])
finally:
    conn.close()
```

> **Never build SQL with f-strings or string concatenation.** Always use placeholders (`?` or `%s`) so values are escaped. This prevents SQL injection.

```python
# DANGEROUS
conn.execute(f"SELECT * FROM users WHERE email = '{user_input}'")
# SAFE
conn.execute("SELECT * FROM users WHERE email = ?", (user_input,))
```

### SQLAlchemy ORM (2.0 style)

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine, ForeignKey, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    name: Mapped[str]
    posts: Mapped[list["Post"]] = relationship(back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[User] = relationship(back_populates="posts")

engine = create_engine("sqlite:///app.db")      # swap for a PostgreSQL URL in production
Base.metadata.create_all(engine)

with Session(engine) as session:
    ada = User(email="ada@example.com", name="Ada")
    ada.posts.append(Post(title="Hello"))
    session.add(ada)
    session.commit()

    users = session.scalars(select(User).where(User.name.like("A%"))).all()
```

### Migrations

Never edit production schemas by hand. Use **Alembic** (SQLAlchemy) or Django's built-in migrations so schema changes are versioned and repeatable.

### Choosing a database

| Database | Good for |
|---|---|
| SQLite | Prototypes, scripts, small apps, tests |
| PostgreSQL | The default choice for production web apps |
| MySQL / MariaDB | Common in existing stacks |
| Redis | Caching, queues, sessions |
| MongoDB | Document-shaped data when relational doesn't fit |

---

## 9. REST APIs & Web Backends

### REST in one table

| Method | Path | Meaning | Success code |
|---|---|---|---|
| `GET` | `/todos` | List | 200 |
| `GET` | `/todos/{id}` | Read one | 200 |
| `POST` | `/todos` | Create | 201 |
| `PUT` / `PATCH` | `/todos/{id}` | Replace / partial update | 200 |
| `DELETE` | `/todos/{id}` | Delete | 204 |

**Common error codes:** `400` bad request, `401` not authenticated, `403` forbidden, `404` not found, `409` conflict, `422` validation error, `429` too many requests, `500` server error.

**Design rules:** use nouns for resources (`/users`, not `/getUsers`), return JSON consistently, version your API (`/v1/...`), paginate lists, and never leak internal errors to clients.

### Choosing a framework

| Framework | Style | Choose it when |
|---|---|---|
| **FastAPI** | Modern, async-friendly, type-driven | Building APIs; automatic validation and interactive docs |
| **Flask** | Minimal and flexible | Small services, learning how the web works |
| **Django** | Batteries included (ORM, admin, auth) | Full sites, content apps, you want an admin panel fast |

### FastAPI: a complete mini API

```bash
pip install "fastapi[standard]"
```

```python
# main.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Todo API", version="1.0.0")

class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    done: bool = False

class Todo(TodoCreate):
    id: int

db: dict[int, Todo] = {}
next_id = 1

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(payload: TodoCreate):
    global next_id
    todo = Todo(id=next_id, **payload.model_dump())
    db[next_id] = todo
    next_id += 1
    return todo

@app.get("/todos", response_model=list[Todo])
def list_todos():
    return list(db.values())

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    if todo_id not in db:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db[todo_id]

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    if db.pop(todo_id, None) is None:
        raise HTTPException(status_code=404, detail="Todo not found")
```

```bash
fastapi dev main.py          # or: uvicorn main:app --reload
# Interactive docs: http://127.0.0.1:8000/docs
```

**Database sessions via dependency injection:**

```python
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    with Session(engine) as session:
        yield session

@app.get("/users")
def list_users(session: Session = Depends(get_db)):
    return session.scalars(select(User)).all()
```

**Allowing a frontend (React, Vue, etc.) to call your API: CORS**

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],   # your frontend origin(s), not "*" in production
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Flask: minimal example

```bash
pip install flask
```

```python
# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.post("/echo")
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(data), 201
```

```bash
flask --app app run --debug
```

### Django: quick start

```bash
pip install django
django-admin startproject config .
python manage.py startapp blog
```

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```bash
# add "blog" to INSTALLED_APPS in config/settings.py, then:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser     # then visit /admin
python manage.py runserver
```

For REST APIs in Django, add **Django REST Framework** (or Django Ninja).

### Authentication & security basics

1. **Never store plain-text passwords.** Hash them with a slow, modern algorithm (Argon2 or bcrypt).
2. Issue a short-lived token (JWT) or use server-side sessions after login.
3. Always serve over HTTPS in production.
4. Validate all input (Pydantic / Django forms / serializers).
5. Keep secrets in environment variables.

```python
# pip install "pwdlib[argon2]" pyjwt
from pwdlib import PasswordHash
import jwt, os
from datetime import datetime, timedelta, timezone

password_hash = PasswordHash.recommended()
hashed = password_hash.hash("correct horse battery staple")
assert password_hash.verify("correct horse battery staple", hashed)

SECRET = os.environ["SECRET_KEY"]

def create_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def read_token(token: str) -> int:
    payload = jwt.decode(token, SECRET, algorithms=["HS256"])
    return int(payload["sub"])
```

### Typical layered backend structure

```
app/
├── main.py            # creates the app, registers routers
├── routers/           # HTTP layer: parse request, return response
├── schemas/           # Pydantic models (API shapes)
├── models/            # DB models
├── services/          # business logic
├── repositories/      # database queries (optional layer)
├── core/              # config, security, logging
└── deps.py            # shared dependencies (db session, current user)
```

### Background work, caching, and queues

| Need | Tool |
|---|---|
| Run something after the response | FastAPI `BackgroundTasks` |
| Long or scheduled jobs | Celery, RQ, or Arq (with Redis) |
| Cache expensive results | Redis, or `functools.lru_cache` in-process |
| Real-time updates | WebSockets (built into FastAPI/Starlette) |

---

## 10. Testing

Tests let you change code without fear. Use **pytest**.

```bash
pip install pytest pytest-cov
pytest                      # run everything
pytest -x                   # stop at first failure
pytest -k "divide"          # run tests matching a name
pytest --cov=src --cov-report=term-missing
```

### Unit tests

```python
# tests/test_math_utils.py
import pytest
from my_project.math_utils import divide

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

@pytest.mark.parametrize("a, b, expected", [(4, 2, 2), (9, 3, 3), (7, 7, 1)])
def test_divide_many(a, b, expected):
    assert divide(a, b) == expected
```

### Fixtures (shared setup)

```python
# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from my_project.models import Base

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as s:
        yield s
```

### Testing a FastAPI app

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_todo():
    created = client.post("/todos", json={"title": "Learn Python"})
    assert created.status_code == 201
    todo_id = created.json()["id"]

    fetched = client.get(f"/todos/{todo_id}")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == "Learn Python"

def test_validation_error():
    assert client.post("/todos", json={"title": ""}).status_code == 422
```

### Mocking external services

```python
from unittest.mock import patch

@patch("my_project.client.requests.get")
def test_fetch_user(mock_get):
    mock_get.return_value.json.return_value = {"login": "octocat"}
    mock_get.return_value.raise_for_status.return_value = None

    from my_project.client import fetch_user
    assert fetch_user("octocat")["login"] == "octocat"
```

### Testing guidelines

- Follow **Arrange, Act, Assert**.
- Test behavior, not implementation details.
- Each test is independent and can run in any order.
- Never hit real external services or production databases in tests.
- Aim for meaningful coverage of important logic, not 100% for its own sake.

---

## 11. Deployment

### Production checklist

- [ ] `DEBUG` is off
- [ ] Secrets come from environment variables, not code
- [ ] A production database (e.g. PostgreSQL), with migrations applied
- [ ] HTTPS enabled
- [ ] CORS restricted to your real frontend origin(s)
- [ ] Structured logging, with errors visible somewhere
- [ ] A `/health` endpoint for uptime checks
- [ ] Pinned dependencies (`requirements.txt` or a lockfile)
- [ ] Tests pass in CI before every deploy

### Production servers

Do not use development servers in production.

```bash
# FastAPI / any ASGI app
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 2

# Flask / Django (WSGI)
gunicorn -w 4 -b 0.0.0.0:8000 app:app
gunicorn -w 4 -b 0.0.0.0:8000 config.wsgi:application
```

### Docker

```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t my-api .
docker run -p 8000:8000 --env-file .env my-api
```

**docker-compose** for app + database locally:

```yaml
services:
  api:
    build: .
    ports: ["8000:8000"]
    env_file: .env
    depends_on: [db]
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: example
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

### Continuous Integration (GitHub Actions)

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: ruff check .
      - run: pytest --cov=src
```

Check the Actions marketplace for the latest action versions.

### Where to host

| Option | Good for |
|---|---|
| Platform-as-a-service (Render, Railway, Fly.io, Heroku-style hosts) | Fastest path from Git repo to live API |
| Cloud containers (AWS ECS/App Runner, Google Cloud Run, Azure Container Apps) | Scalable, production-grade |
| A VPS (DigitalOcean, Hetzner, etc.) with Docker + a reverse proxy (Nginx/Caddy) | Full control, low cost |
| Serverless functions | Small, event-driven endpoints |

Typical flow: push to Git → CI runs tests → platform builds the image → run migrations → deploy → check `/health`.

---

## 12. Best Practices & Security

### Code style (PEP 8 essentials)

- 4-space indentation, lines up to ~100 characters
- `snake_case` functions/variables, `PascalCase` classes, `UPPER_CASE` constants
- Two blank lines between top-level definitions
- Imports at the top, grouped: standard library, third party, local
- Let `ruff format` handle the rest

### Writing good code

- Functions do **one thing** and have clear names.
- Prefer explicit over clever. Readability beats brevity.
- Avoid global state and mutable default arguments.
- Use type hints on public functions.
- Write docstrings for modules, classes, and public functions.
- Handle errors where you can meaningfully respond to them. Don't swallow exceptions silently.
- Don't repeat yourself, but don't abstract too early either.

### Security checklist

| Risk | Defense |
|---|---|
| SQL injection | Parameterized queries or an ORM, never string-built SQL |
| Leaked secrets | Environment variables, `.gitignore`, secret scanners; rotate if exposed |
| Weak passwords storage | Argon2/bcrypt hashing, never plain text or MD5/SHA1 |
| XSS (in server-rendered HTML) | Use template auto-escaping; never mark user input as safe |
| CSRF | Framework CSRF protection for cookie-based sessions |
| Dependency vulnerabilities | `pip-audit`, Dependabot, pin and update regularly |
| Unsafe deserialization | Never `pickle.load` untrusted data; never `eval`/`exec` user input |
| Command injection | `subprocess.run([...])` with a list, no `shell=True` on user input |
| Over-exposed data | Response schemas that whitelist fields |
| Brute force | Rate limiting, account lockouts |

Use the `secrets` module (not `random`) for tokens and anything security-sensitive.

### Performance basics

- Measure first: `cProfile`, `timeit`, or simple timers. Don't guess.
- Pick the right data structure (`set`/`dict` lookups are O(1); list `in` is O(n)).
- Use generators for large streams.
- Add database **indexes** for columns you filter or join on; avoid N+1 queries.
- Cache expensive, repeatable work.

### Debugging

```python
breakpoint()          # drops into the debugger (pdb); n=next, s=step, c=continue, p var
```

Learn your editor's debugger too. Prefer a debugger and logging over scattering `print` calls.

---

## 13. Cheat Sheets

### Python for JavaScript developers

| Concept | JavaScript | Python |
|---|---|---|
| Declare | `const x = 1` | `x = 1` |
| Equality | `===` | `==` (and `is` for identity) |
| Null | `null` / `undefined` | `None` |
| Boolean ops | `&&` `\|\|` `!` | `and` `or` `not` |
| String template | `` `Hi ${name}` `` | `f"Hi {name}"` |
| Array / object | `[]` / `{}` | `list` / `dict` |
| Loop | `for (const x of arr)` | `for x in arr:` |
| Map / filter | `arr.map(f)` | `[f(x) for x in arr]` |
| Function | `(a) => a + 1` | `lambda a: a + 1` |
| Async | `async/await`, Promises | `async/await`, `asyncio` |
| Packages | npm / `package.json` | pip / `pyproject.toml` |
| Dev server | Vite / Express | uvicorn / Flask / Django |
| Blocks | `{ }` | indentation |

Full-stack tip: a React (or any JS) frontend talks to a Python backend over JSON. Build the API, enable CORS for your frontend origin, and keep a shared contract (FastAPI's OpenAPI schema at `/openapi.json` can generate typed API clients).

### Built-in functions worth knowing

`len` `range` `enumerate` `zip` `map` `filter` `sorted` `reversed` `sum` `min` `max` `any` `all` `abs` `round` `isinstance` `type` `dir` `help` `open` `print` `input` `repr` `id` `getattr` `setattr` `hasattr`

### Quick syntax reference

```python
# Swap
a, b = b, a

# Default dict value
counts = {}
counts[key] = counts.get(key, 0) + 1

# Walrus operator
if (n := len(items)) > 10:
    print(f"too many: {n}")

# Unpack dicts
config = {**defaults, **overrides}

# Flatten
flat = [x for row in matrix for x in row]

# Sort by multiple keys
people.sort(key=lambda p: (p["age"], p["name"]))

# any / all
any(x > 5 for x in nums)
all(isinstance(x, int) for x in nums)

# Read help
help(str.split)
```

### Common errors

| Error | Usual cause |
|---|---|
| `SyntaxError` | Typo, missing colon/bracket/quote |
| `IndentationError` | Mixed tabs/spaces or wrong indent level |
| `NameError` | Variable used before it's defined, or misspelled |
| `TypeError` | Wrong type (e.g. `"a" + 1`) or wrong number of arguments |
| `ValueError` | Right type, bad value (`int("abc")`) |
| `KeyError` | Missing dict key (use `.get()`) |
| `IndexError` | List index out of range |
| `AttributeError` | Object doesn't have that attribute/method; often `None` |
| `ImportError` / `ModuleNotFoundError` | Not installed, wrong venv, or wrong module name |
| `FileNotFoundError` | Wrong path or working directory |

---

## 14. Practice Projects

Build these in order. Each uses skills from the previous.

### Beginner
1. **Number guessing game**: loops, input, conditionals
2. **To-do list CLI**: lists, functions, file persistence (JSON)
3. **Expense tracker**: dicts, CSV, simple reports
4. **Password generator**: `secrets`, argparse

### Intermediate
5. **File organizer / bulk renamer**: `pathlib`, `shutil`, CLI
6. **Weather or GitHub stats CLI**: `requests`, error handling, JSON
7. **Web scraper + CSV export**: `requests`, BeautifulSoup, pandas
8. **Library system**: OOP, dataclasses, unit tests

### Job-ready
9. **Todo / notes REST API**: FastAPI, SQLAlchemy, Pydantic, tests
10. **Auth system**: registration, login, JWT, protected routes
11. **URL shortener**: database, redirects, rate limiting, Docker
12. **Full-stack app**: Python API + a JavaScript frontend, PostgreSQL, CI pipeline, deployed live with a public URL
13. **Data dashboard**: pandas pipeline + API + scheduled refresh

**For each project:** use Git, write a good README, add tests, and deploy at least a few of them. A portfolio of deployed, documented projects matters more than certificates.

---

## 15. Job-Ready Roadmap & Checklist

### Suggested timeline (adjust to your pace)

| Weeks | Focus |
|---|---|
| 1-3 | Setup, fundamentals (sections 2-3), small exercises daily |
| 4-6 | Intermediate Python, OOP, files, errors (section 4) |
| 7-8 | Project structure, Git, tooling, automation scripts (sections 5-6) |
| 9-10 | SQL + SQLAlchemy, data with pandas (sections 7-8) |
| 11-13 | REST APIs with FastAPI or Django, auth (section 9) |
| 14-15 | Testing and CI (section 10) |
| 16 | Docker + deployment (section 11), polish portfolio |

### Skills checklist

**Core**
- [ ] Data types, collections, comprehensions
- [ ] Functions, scope, `*args` / `**kwargs`
- [ ] OOP: classes, inheritance, dunder methods, dataclasses
- [ ] Exceptions, context managers, file I/O
- [ ] Modules, packages, virtual environments

**Engineering**
- [ ] Git and GitHub workflow (branches, pull requests)
- [ ] Linting, formatting, type hints
- [ ] Logging and configuration via environment variables
- [ ] Reading other people's code and documentation

**Backend**
- [ ] SQL (joins, aggregates, indexes) and an ORM
- [ ] Designing and documenting REST endpoints
- [ ] Authentication and authorization
- [ ] Validation and error handling in APIs

**Quality & delivery**
- [ ] pytest: unit and API tests, fixtures, mocking
- [ ] Docker basics
- [ ] CI pipeline running tests and lint
- [ ] Deployed at least one app publicly

### Common interview topics

- Mutable vs immutable types; list vs tuple; dict internals at a high level
- `is` vs `==`; shallow vs deep copy
- Decorators, generators, context managers
- The GIL and when to use threads, processes, or `asyncio`
- Big-O of common operations
- `*args` / `**kwargs`; mutable default arguments
- SQL joins, indexes, transactions, N+1 queries
- REST design, status codes, idempotency, authentication flows
- How you would test, deploy, and monitor a service
- Classic coding questions: reverse a string, two-sum, anagram check, FizzBuzz, validate parentheses, merge intervals

Practice on LeetCode, HackerRank, Exercism, or Advent of Code, but keep shipping real projects alongside.

---

## 16. Resources

### Official documentation
- Python docs and tutorial: https://docs.python.org/3/
- FastAPI: https://fastapi.tiangolo.com
- Flask: https://flask.palletsprojects.com
- Django: https://docs.djangoproject.com
- SQLAlchemy: https://docs.sqlalchemy.org
- pytest: https://docs.pytest.org
- pandas: https://pandas.pydata.org/docs
- uv: https://docs.astral.sh/uv/

### Learning
- *Automate the Boring Stuff with Python* (Al Sweigart): practical automation for beginners
- *Fluent Python* (Luciano Ramalho): deep, idiomatic Python for when you're comfortable
- *Python Crash Course* (Eric Matthes): beginner-friendly with projects
- Real Python tutorials: https://realpython.com
- Exercism Python track: https://exercism.org/tracks/python

### Habits that compound
1. Code a little every day. Consistency beats marathon sessions.
2. Read the official docs and error messages before searching.
3. Build, break, fix, repeat.
4. Review your old code and refactor it.
5. Share your work: GitHub, a portfolio site, write-ups of what you learned.

---

*Happy coding. Build things, ship them, and keep iterating.*
