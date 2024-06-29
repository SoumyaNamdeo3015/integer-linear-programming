# Integer Linear Programming

## About the Algorithm
This project involves solving integer linear programming problems using Gomory's cutting plane algorithm.

For more detailed information, refer to the [Cutting-plane method](https://en.wikipedia.org/wiki/Cutting-plane_method#:~:text=dominates%20Gomory%20cuts.-,Gomory's%20cut,while%20respecting%20the%20linear%20constraints) on Wikipedia.

## Objective
The goal is to solve integer linear programming problems using Gomory's cutting plane algorithm.

## Input File (input_ilp.txt)
The input file `input_ilp.txt` should be formatted as follows:

1. The first two lines indicate the type of linear programming problem:
   - `max` for maximization problems
   - `min` for minimization problems
2. The matrix \( A \) representing the coefficients of the constraints.
3. The matrix \( b \) representing the right-hand side values of the constraints.
4. The constraint types, which can be one of `>=`, `<=`, or `=`.
5. The matrix \( c \) representing the cost vector.

### Structure of `input_ilp.txt`
- **Objective**: Clearly state whether the problem is to "maximize" or "minimize" the objective function.
- **Matrix A**: Contains the coefficients of the variables in the linear constraints. Each row represents a constraint, and each column corresponds to a variable.
- **Matrix b**: Lists the right-hand side (RHS) values for each constraint, with each row corresponding to a constraint in the [A] section.
- **Constraint Types**: Specifies the type of each constraint corresponding to the rows in [A] and [b]. Use `<=` for less than or equal to, `>=` for greater than or equal to, and `=` for equality constraints.
- **Matrix c**: Contains the coefficients of the objective function's variables in one row.


### Notes:
- The input file name must be `input_ilp.txt`.
- Matrices \( A \), \( b \), and \( c \) have integral entries.

## Main Python Script (main.py)
The main Python script `main.py` should contain a function named `gomory_cut_algo` which reads `input_ilp.txt` and does not take any argument as a parameter.

### Output Information
The `gomory_cut_algo` function should print the following information in the given order on the command line:

1. **Initial Solution (initial_solution)**: The initial feasible solution obtained by the simplex method.
2. **Final Solution (final_solution)**: The optimal integer solution after applying Gomory cuts.
3. **Solution Status (solution_status)**: The status of the solution (`"optimal"`, `"infeasible"`, or `"unbounded"`).
4. **Number of Cuts (number_of_cuts)**: The total number of Gomory cuts applied to reach the final solution.
5. **Optimal Value (optimal_value)**: The value of the objective function at the optimal solution.

### Packages Used
- `copy`
- `Fractions`

---

This markdown provides a clear and structured description of the integer linear programming problem, the required input file format, and the implementation details for the `gomory_cut_algo` function in `main.py`.

