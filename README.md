# password-strength-tool
# 🔐 Python Password Strength Evaluator

A lightweight, security-focused Python utility that evaluates the strength of a password based on standard Information Security (InfoSec) compliance rules. Built with computational efficiency in mind, this tool utilizes "Pythonic" logic (generator expressions and short-circuiting) for rapid credential validation. 

Perfect for quick integration into security labs or as a standalone CLI tool.

## ✨ Features
* **Comprehensive Validation:** Enforces minimum security standards by checking for length (8+ characters), uppercase, lowercase, numbers, and symbols.
* **Computational Efficiency:** Replaces verbose manual loops with C-optimized built-in functions (`any()`).
* **Interactive CLI:** Includes a continuous loop for testing multiple credentials directly in the terminal.
* **Production-Ready:** Implements Type Hints and Enumerations (`Enum`) for safe, predictable behavior.

## 🚀 Getting Started

### Prerequisites
* Python 3.6 or higher (No external libraries required)

### Usage
Run the script directly from your terminal:
```bash
python password_checker.py
