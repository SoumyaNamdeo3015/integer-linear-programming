
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
