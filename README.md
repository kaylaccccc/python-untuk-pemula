# Python for Beginners

A hands-on practice repository covering the fundamentals of Python programming. Each chapter is added as a separate, well-documented commit, with an execution screenshot as proof of the result.


## About the Project

This repository documents my learning journey through the basics of Python. All example code lives in a single file, `main.py`, and grows chapter by chapter. The repository also includes a virtual environment setup, a pinned dependency list, and shared editor settings, so the project can be reproduced on any machine.

## Topics Covered

| Chapter | Topic | Description |
|---|---|---|
| 1 | Introduction & Python Installation | First program, checking the installed Python version |
| 2 | Variables and Data Types | Integers, floats, strings, booleans |
| 3 | Python Operators | Arithmetic, comparison and logical operators |
| 4 | Conditional Statements | `if`, `elif`, `else` and indentation rules |
| 5 | Loops | `for`, `while`, `break`, `continue` |
| 6 | Lists and Dictionaries | Indexing, adding, updating and removing items |
| 7 | Functions | Arguments, `*args`, `**kwargs`, default values |
| 8 | Classes and Objects | Properties, constructors, methods |
| 9 | PIP and Virtual Environments | Installing packages, isolating dependencies |
| 10 | IDE / Environment Configuration | Shared VS Code settings |
| 11 | README.md & requirements.txt | Project documentation and dependency list |

## Project Structure

```text
python-untuk-pemula/
├── .vscode/
│   └── settings.json      # Shared VS Code configuration
├── screenshots/
│   ├── bab01.png          # Execution screenshots, one per chapter
│   ├── ...
│   └── bab11.png
├── .gitignore             # Files and folders ignored by Git
├── main.py                # All chapter examples
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## Prerequisites

Make sure the following are installed on your machine:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- A code editor such as [Visual Studio Code](https://code.visualstudio.com/) (recommended)

Check your installation:

```bash
python --version
git --version
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/kaylaccccc/python-untuk-pemula.git
   cd python-untuk-pemula
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   ```bash
   # Windows (Git Bash)
   source venv/Scripts/activate

   # Windows (CMD)
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

4. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main program:

```bash
python main.py
```

To leave the virtual environment when you are done:

```bash
deactivate
```

## Screenshots

Each chapter has an execution screenshot stored in the `screenshots/` folder.

| Chapter | Screenshot |
|---|---|
| 1. Introduction & Python Installation | [bab01.png](screenshots/bab01.png) |
| 2. Variables and Data Types | [bab02.png](screenshots/bab02.png) |
| 3. Python Operators | [bab03.png](screenshots/bab03.png) |
| 4. Conditional Statements | [bab04.png](screenshots/bab04.png) |
| 5. Loops | [bab05.png](screenshots/bab05.png) |
| 6. Lists and Dictionaries | [bab06.png](screenshots/bab06.png) |
| 7. Functions | [bab07.png](screenshots/bab07.png) |
| 8. Classes and Objects | [bab08.png](screenshots/bab08.png) |
| 9. PIP and Virtual Environments | [bab09.png](screenshots/bab09.png) |
| 10. IDE / Environment Configuration | [bab10.png](screenshots/bab10.png) |
| 11. README.md & requirements.txt | [bab11.png](screenshots/bab11.png) |

## Commit Convention

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```text
<type>(<scope>): <short description>

- <detail 1>
- <detail 2>

Refs: <reference>
```

| Type | Purpose |
|---|---|
| `feat` | Adding new code or examples |
| `chore` | Configuration and environment setup |
| `docs` | Documentation changes |

## Author

**kaylaccccc**

- GitHub: [@kaylaccccc](https://github.com/kaylaccccc)