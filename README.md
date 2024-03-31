# integer-linear-programming

## About the algorithm : (gomory's cutting plane algorithm )

refer to this link : https://en.wikipedia.org/wiki/Cutting-plane_method#:~:text=dominates%20Gomory%20cuts.-,Gomory's%20cut,while%20respecting%20the%20linear%20constraints.

## Objective :
solving integer linear programming problems using gomory's cutting plane algorithm


## About input_ilp.txt :

The first two lines of input file contains the type of linear programming problem i.e maximizing or minimizing of the objective function.
Then it contains matirx A , followed by matrix b .
Then we have our constraint types which include >= , <= and = only.
at last matrix c (cost vector) is entered.

 The [objective] section should clearly state whether the problem is a "maximize" or "minimize" 
problem. This will dictate the direction of your optimization in solving the problem.  
+ The [A] section contains the coefficients of the variables in the linear constraints. Each row in 
this section represents a constraint, and each column corresponds to a variable.  
+ The [b] section lists the right-hand side (RHS) values for each constraint, with each row 
corresponding to a constraint in the [A] section. 
+ The [constraint_types] section specifies the type of each constraint corresponding to the rows in 
[A] and [b]. Use <= for less than or equal to, >= for greater than or equal to, and = for equality 
constraints.  
+ The [c] section contains the coefficients of the objective function's variables in one row.

note: the input file name must be input_ilp.txt

note: matrices A,b,c have integral entries


## About main.py :

main.py contains a function named “gomory_cut_algo” which reads “input_ilp.txt” and does not take any argument as 
parameter and print the following information in the given order on command line: 
+ Initial Solution (initial_solution): The initial feasible solution obtained by the simplex method. 
+ Final Solution (final_solution): The optimal integer solution after applying Gomory cuts. 
+ Solution Status (solution_status): “optimal”, “infeasible”, or “unbounded”. 
+ Number of Cuts (number_of_cuts): The total number of Gomory cuts applied to reach the final 
solution. 
+ Optimal Value (optimal_value): The value of the objective function at the optimal solution.

### Packages used : 
+ copy
+ Fractions 
