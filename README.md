# 🧮 Python Calculator

A simple and interactive **Command-Line Calculator** built using **Python 3.10+**. This calculator performs basic arithmetic operations using Python's modern **`match-case`** statement and provides a user-friendly menu to start or exit the application.

---

## 📖 Overview

This project is designed for beginners to understand the fundamentals of Python programming. It demonstrates concepts such as loops, conditional statements, pattern matching, user input handling, and arithmetic operations in a clean and interactive manner.

---

## ✨ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🧮 Modulus (Remainder)
- ⚠️ Division-by-zero handling
- ❌ Invalid operator detection
- 🔁 Perform unlimited calculations
- 🚪 Start or exit from the welcome menu
- 🆕 Uses Python 3.10 `match-case`

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Command Line Interface (CLI)**

---

## 📂 Project Structure

```
Python-Calculator/
│
├── README.md
└── calculator.py

```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10** or later

Check your installed version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## ▶️ Running the Program

Clone the repository:

```bash
git clone https://github.com/SAYAR123/Python-Calculator.git
```

Navigate into the project directory:

```bash
cd Python-Calculator
```

Run the calculator:

```bash
python calculator.py
```

---

# 📸 Sample Output

### Welcome Screen

```text
Welcome to Python Calculator!

Press c to continue
Press e to exit

c
```

---

### Addition

```text
Enter a number: 15
Enter another number: 8

Operator list:
    For addition press +
    For subtraction press -
    For multiplication press *
    For division press /
    For modulo press %

Enter operator: +

15.0 + 8.0 = 23.0
```

---

### Multiplication

```text
Enter a number: 12
Enter another number: 5

Operator list:
    For addition press +
    For subtraction press -
    For multiplication press *
    For division press /
    For modulo press %

Enter operator: *

12.0 * 5.0 = 60.0
```

---

### Division

```text
Enter a number: 18
Enter another number: 6

Operator list:
    For addition press +
    For subtraction press -
    For multiplication press *
    For division press /
    For modulo press %

Enter operator: /

18.0 / 6.0 = 3.0
```

---

### Modulus

```text
Enter a number: 17
Enter another number: 5

Operator list:
    For addition press +
    For subtraction press -
    For multiplication press *
    For division press /
    For modulo press %

Enter operator: %

17.0 % 5.0 = 2.0
```

---

### Division by Zero

```text
Enter a number: 20
Enter another number: 0

Operator list:
    For addition press +
    For subtraction press -
    For multiplication press *
    For division press /
    For modulo press %

Enter operator: /

Cannot divide by zero
```

The calculator returns to the main menu for the next calculation.

---

### Invalid Operator

```text
Enter operator: ^

Invalid operator
```

The calculator returns to the main menu without crashing.

---

### Exit

```text
Welcome to Python Calculator!

Press c to continue
Press e to exit

e
```

The application terminates successfully.

---

## 🖼️ Screenshot

Include a screenshot of the calculator running in your terminal.

<img width="512" height="440" alt="image" src="https://github.com/user-attachments/assets/dfd84c27-f70a-470c-a45d-c8a9a7a376b5" />

---

## ⚙️ Supported Operations

| Operator | Operation |
|:--------:|-----------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulus |

---

## 🧠 Concepts Demonstrated

- Variables and Data Types
- User Input (`input()`)
- Type Casting (`float`)
- Arithmetic Operators
- Infinite Loops (`while`)
- Conditional Statements (`if`)
- Pattern Matching (`match-case`)
- Loop Control (`break`, `continue`)
- Formatted Strings (`f-string`)

---

## 📌 Current Limitations

- Non-numeric inputs are not validated.
- Only two operands are supported.
- Unary operators not supported.

---

## 🔮 Future Enhancements

- Input validation using `try-except`
- Support decimal values correctly for both operands
- Exponentiation (`**`)
- Square root and logarithmic functions
- Scientific calculator mode
- Calculation history
- Graphical User Interface (Tkinter)
- Web application using Flask or Streamlit

---

## 👨‍💻 Author

**Sayar Sekhar Ghosh**

GitHub: https://github.com/SAYAR123

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
