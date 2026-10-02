# Python Calculator with Execution Time

A simple command-line calculator developed in Python. The calculator performs basic arithmetic operations and measures the execution time of each calculation.

## Features

* Addition
* Subtraction
* Multiplication
* Division
* Division-by-zero handling
* Invalid input handling
* Execution time measurement
* Simple command-line interface

## Technologies Used

* Python 3
* `time` module

## Operations

| Operator | Operation      |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |

## How It Works

The program uses Python's `time.perf_counter()` function to measure how long the calculation takes.

The execution time is calculated using:

```python
start_time = time.perf_counter()

# Calculation

end_time = time.perf_counter()

execution_time = end_time - start_time
```

`time.perf_counter()` provides a high-resolution timer suitable for measuring short execution times.

## Requirements

Python 3.x must be installed on your system.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/python-calculator.git
```

Navigate to the project directory:

```bash
cd python-calculator
```

Run the calculator:

```bash
python calculator.py
```

## Example

```text
===== Python Calculator =====

Operations: +  -  *  /
Enter 'q' to quit

Enter operation: +

Enter first number: 15
Enter second number: 25

Result: 40.0
Execution Time: 0.0000004000 seconds
```

## Project Structure

```text
python-calculator/
│
├── calculator.py
└── README.md
```

## Purpose

The purpose of this project is to demonstrate basic Python programming, arithmetic operations, input handling, exception handling, and execution-time measurement.

## Author

Abdullah Kaleem

## License

This project is created for educational purposes.
