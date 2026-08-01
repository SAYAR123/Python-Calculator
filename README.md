# 🧮 Python Calculator

A simple **Command-Line Calculator** built with **Python 3.10+** that performs basic arithmetic operations using the modern **`match-case`** statement. The calculator runs continuously until the user chooses to exit and safely handles division by zero.

---

## 📖 Overview

This project demonstrates the fundamentals of Python programming, including:

- User input handling
- Infinite loops
- Pattern matching (`match-case`)
- Conditional statements
- Arithmetic operations
- Formatted output using f-strings

It is an excellent beginner project for learning Python basics.

---

## ✨ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- ⚠️ Division-by-zero protection
- 🔁 Continuous calculations until the user exits
- 🚪 Exit option (`e`)
- 🆕 Built using Python's `match-case` statement

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Command Line Interface (CLI)**

---

## 📂 Project Structure

```
Python-Calculator/
│
├── calc.py
└── README.md

```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10** or later

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## ▶️ Running the Application

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Python-Calculator.git
```

Navigate to the project directory:

```bash
cd Python-Calculator
```

Run the calculator:

```bash
python calculator.py
```

---

# 📸 Sample Output

## Addition

```text
Enter a number: 10
Enter another number: 5

Operator list:
    For addition press +
    For subtraction press -
    For multiplication press *
    For division press /
    For exiting press e

Enter operator: +

10.0+5.0 = 15.0
```

---

## Multiplication

```text
Enter a number: 12
Enter another number: 6

Operator list:
    For addition press +
    For subtraction press -
    For multiplication press *
    For division press /
    For exiting press e

Enter operator: *

12.0*6.0 = 72.0
```

---

## Division

```text
Enter a number: 25
Enter another number: 5

Operator list:
    For addition press +
    For subtraction press -
    For multiplication press *
    For division press /
    For exiting press e

Enter operator: /

25.0/5.0 = 5.0
```

---

## Division by Zero

```text
Enter a number: 20
Enter another number: 0

Operator list:
    For addition press +
    For subtraction press -
    For multiplication press *
    For division press /
    For exiting press e

Enter operator: /

Cannot divide by zero
```

The calculator immediately starts the next calculation without displaying an incorrect result.

---

## Exit

```text
Enter operator: e
```

The application exits successfully.

---

# 🖼️ Output Screenshot

<img width="1028" height="292" alt="image" src="https://github.com/user-attachments/assets/7f0544f5-2a2a-4aa4-b2c1-b336159f82aa" />

---

## ⚙️ Supported Operations

| Operator | Description |
|----------|-------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `e` | Exit Program |

---

## 🧠 Concepts Demonstrated

- Variables
- User Input (`input()`)
- Type Casting
- Arithmetic Operators
- Infinite Loops (`while`)
- Pattern Matching (`match-case`)
- Conditional Statements (`if-else`)
- Loop Control (`continue`, `break`)
- Formatted Strings (`f-string`)

---

## 📌 Current Limitations

- Does not validate non-numeric input.
- Accepts only two operands at a time.
- Invalid operators display an error message and continue execution.

---

## 🔮 Future Enhancements

- Input validation using `try-except`
- Modulus (`%`) operation
- Exponentiation (`**`)
- Square root calculations
- Scientific calculator functions
- Calculation history
- Graphical User Interface (Tkinter)
- Web version using Flask or Streamlit

---

## 👨‍💻 Author

**Sayar Sekhar Ghosh**

GitHub: https://github.com/SAYAR123

---

## ⭐ Show Your Support

If you found this project helpful, please consider giving it a ⭐ on GitHub!
