# PnCcalculator
Combinatorics calculator
# 🎲 Permutation, Combination, and Factorial Calculator

This Python script allows you to easily compute **Permutations**, **Combinations**, and **Factorials** for any set of numbers. With a simple user interface, you can run multiple tests and choose the operation type that suits your needs.

---

## 🛠️ Features
- **Factorial Calculation**: Computes the factorial of a number `n`.
- **Combination Calculation**: Calculates the number of combinations (`nCr`), where order doesn't matter.
- **Permutation Calculation**: Calculates the number of permutations (`nPr`), where order matters.
- Option to run multiple tests based on user input.

---

## 📋 How to Use

### Input Options
1. **Number of Tests**: The script will first prompt you to specify how many tests you want to run. If the number exceeds 10, a confirmation is required.
2. **Operation Type**: You can choose from:
   - **Permutation** (`p`)
   - **Combination** (`c`)
   - **Factorial** (`f`)
3. **Indexes or Number**: Based on the chosen operation, provide the necessary input values (`n` and `r` for permutations/combinations or just `n` for factorial).

---

### 🖥️ Example Usage

1. Run the script.
2. Input the number of times you want to perform a test.
3. Select the operation:
   - **p** for permutation,
   - **c** for combination, or
   - **f** for factorial.
4. The script will print the result of each operation.

### 🔍 Sample Run:
```bash
How many times do you want to run this test? : 3
What do you want to perform?(permutation[p]/combination[c]/factorial[f) : p
Please provide the upper index: 5
Please provide the lower index: 2
20.0

What do you want to perform?(permutation[p]/combination[c]/factorial[f) : f
Please provide the number for which you desire to find the factorial: 4
24

What do you want to perform?(permutation[p]/combination[c]/factorial[f) : c
Please provide the upper index: 6
Please provide the lower index: 2
15.0
