import copy

from fractions import Fraction

def gomory_cut_algo():

    def performOperationsDual(T,pivotRow, pivotCol):
        
        pivotElement = T[pivotRow][pivotCol]

        for i in range(1,len(T)):

            if(i==pivotRow):

                continue

            u=T[i][pivotCol]/pivotElement

            for j in range(1,len(T[0])):

                T[i][j]-=u*T[pivotRow][j]

        for j in range(1,len(T[0])):

            T[pivotRow][j] = T[pivotRow][j]/pivotElement

        
        T[pivotRow][0] = T[0][pivotCol]

        return T


    def print_matrix(matrix):

        for row in matrix:

            print("    ".join(map(str, row)))

        print('\n\n')


    def checkInteger(num):

        if num.denominator  == 1:

            return "integer" 

        else:

            return "fraction"


    def solve(T):
        l = []
        for i in range(0,len(T)):
            l.append(T[i][1])
    
        fractional_var = []
        for i in range(2,len(l)):
            if(checkInteger(l[i])=="fraction"):
                fractional_var.append(T[i][0])

        if(len(fractional_var) == 0):
            return [False,-1]
        
        return [True,fractional_var[0]]


    def separate_parts(num):

        integral_part = num // 1
        fractional_part_numerator = num.numerator % num.denominator
        fractional_part_denominator = num.denominator

        integral_part = Fraction(integral_part)
        
        fractional_part = Fraction(fractional_part_numerator, fractional_part_denominator)

        return [integral_part, fractional_part]

    

    def integral_part(num):

        return separate_parts(num)[0]


    def fractional_part(num):

        return separate_parts(num)[1]


    def addGomoryConstraint(index,T,myDict):

        temp_row = []

        for i in range(2,len(T)):

            if(T[i][0] == index):

                for j in range(len(T[0])):

                    temp_row.append(T[i][j])



        lastVarIndex = T[0][len(T[0])-1]



        myDict[lastVarIndex+1]= "gomory_var"



        new_row = []

        new_row.append(lastVarIndex+1)

        new_row.append(-fractional_part(temp_row[1]))



        for i in range(2,len(temp_row)):

            if(checkInteger(temp_row[i])=="integer"):

                new_row.append(Fraction(0))

            else:

                new_row.append(-fractional_part(temp_row[i]))



        new_row.append(Fraction(1))


        T[0].append(lastVarIndex+1)  #indexing row

        T[1].append(Fraction(0)) # reduced cost row

        for i in range(2,len(T)):

            T[i].append(Fraction(0))

        T.append(new_row) 

        

        return T,myDict


    def simplex_algo():



        def drop_rows_and_columns(matrix):

            matrix = [row[1:] for row in matrix]

            matrix = matrix[2:]

            return matrix



        def sumColumn(A,col_index):

            sum = Fraction(0)

            for i in range(len(A)):

                sum += A[i][col_index]

            return sum



        def phase2firstrow(A,col_index,c):    

            sum=Fraction(0)

            for i in range(len(A)):

                sum += A[i][col_index]*c[int(A[i][0])]

            return c[col_index-2]-sum

        

        def performOperations(T,pivotRow, pivotCol):

            pivotElement = T[pivotRow][pivotCol]

            for i in range(1,len(T)):

                if(i==pivotRow):

                    continue

                u=T[i][pivotCol]/pivotElement

                for j in range(1,len(T[0])):

                    T[i][j]-=u*T[pivotRow][j]

            for j in range(1,len(T[0])):

                T[pivotRow][j] = T[pivotRow][j]/pivotElement

                T[pivotRow][j] = T[pivotRow][j]

            T[pivotRow][0] = T[0][pivotCol]

            return T



        def read_input(filename):    

            with open(filename, 'r') as f:

                lines = f.readlines()

            objective = None 

            # 1 -> minimize 

            # -1 -> maximize

            A = []

            b = []

            c = []

            constraint_types = []

            neg_row = []

            cons_row = []

            num_constraints = 0

            decision_vars = 0

            slack_vars = 0

            myDict = {}

            mode = "objective"

            for line in lines:

                line = line.strip()

                if not line :

                    continue

                if line == "[objective]" :

                    mode = "objective"

                    continue

                elif (line == "[A]"):

                    mode = "A"

                    continue

                elif line == "[b]":

                    mode = "b"

                    continue

                elif line == '[c]':

                    mode = 'c'

                    continue

                elif line == '[constraint_types]':

                    mode = 'constraint_types'

                    continue

                elif mode == "objective":

                    if(line.lower() == "maximize"):

                        objective = -1

                    else:

                        objective = 1

                elif mode == "A":

                    row_entries = line.split(',')

                    decision_vars = len(row_entries)



                    row_entries = [Fraction(x) for x in row_entries]

                

                    A.append(row_entries)

                elif mode == "b":

                    b.append(Fraction(line))

                    if (Fraction(line) < 0):

                        neg_row.append(1)

                    else:

                        neg_row.append(0)

                elif mode == "c":

                    row_entries = line.split(',')

                    c = [Fraction(x) for x in row_entries]

                elif mode == "constraint_types":

                    if (line == ">="):

                        cons_row.append(-1)

                    elif (line == "="):

                        cons_row.append(0)

                    else:

                        cons_row.append(1)

            



            decision_vars = len(A[0])

            num_constraints = len(neg_row)



            for i in range(len(neg_row)):

                if neg_row[i]:

                    A[i] = [-x for x in A[i]]

                    b[i] = - b[i]

                    cons_row[i] = -cons_row[i]

            

            c = [x*objective for x in c]



            for i in range(num_constraints):

                if (cons_row[i] != 0):



                    slack_vars += 1

                    for j in range (num_constraints):

                        if j == i:

                            A[j].append(Fraction(cons_row[i]))

                        else:

                            A[j].append(Fraction(0))

            



            for i in range(slack_vars):

                c.append(Fraction(0))

            

            for i in range(decision_vars):

                myDict[i] = "decision_vars"

            

            for i in range(decision_vars,decision_vars + slack_vars):

                myDict[i] = "slack_vars"

            

            return A,b,c,myDict,objective



        def phase_I(A, b, myDict):



            valid = 0 # valid = 1, if LP is infesaible, valid = 0 otherwise;

            num_vars = len(A[0])

            num_constraint = len(b)

            aux_vars = num_constraint



            c = [Fraction(0) for i in range(num_vars)]



            for i in range(aux_vars):

                c.append(Fraction(1))

            

            for i in range(num_vars, aux_vars + num_vars):

                myDict[i] = "auxillary_vars"



            for i in range(num_constraint):

                for j in range(num_constraint):

                    if (i == j):

                        A[j].append(Fraction(1))

                    else:

                        A[j].append(Fraction(0))





            row1 = [Fraction(0), Fraction(0)] 

            for i in range(aux_vars + num_vars):

                row1.append(Fraction(i))

            

            ctx = Fraction(0)

            for value in b:

                ctx += value



            row2 = [Fraction(0),-ctx]

            



            for i in range(num_vars):

                row2.append(-sumColumn(A,i))



            for i in range(num_vars, num_vars + aux_vars):

                row2.append(Fraction(0))

            

            T = [[(f'x_{i}_{j}') for i in range(aux_vars + num_vars + 2)] for j in range(num_constraint + 2)]

            T[0] = row1

            T[1] = row2



            for i in range(2,num_constraint + 2):

                T[i][0] = Fraction(num_vars + i - 2)

                T[i][1] = (b[i-2])

                    



            for j in range(2, num_vars + aux_vars + 2):

                for i in range(2, num_constraint+2):

                    T[i][j] = A[i-2][j-2]





            iteration_max = 100000

            i = 0

            # 0 --> fes  1 --> unfes 

            status = 0



            while(True and i < iteration_max):

                i+=1



                pivotColList = []

                for col in range(2, num_vars+ aux_vars + 2):

                    if(T[1][col] < 0):

                        pivotColList.append(col)

                

                if(len(pivotColList) == 0):

                    #all reduced costs were postive:

                    break

                

                pivotCol = -1

                postiveFound = False

                

                for colIndex in pivotColList:

                

                    for i in range(2,num_constraint+2):

                        if(T[i][colIndex]>0):

                            pivotCol = colIndex

                            postiveFound = True

                

                

                if(postiveFound == False):

                    status =1 

                    break

            

                minValue = 1e10

                minIndex = -1



                for row in range(2,num_constraint + 2):



                    if(T[row][pivotCol] <= 0):

                        continue

                    

                    ratio = T[row][1]/T[row][pivotCol]

                    ratio = ratio

                    if(ratio < minValue):

                        minValue = ratio

                        minIndex = row





                if(minIndex == -1):

                    # all were non postive, and infes

                    status = 1

                    break

                

                pivotRow = minIndex

                

                T = performOperations(T,pivotRow,pivotCol)



            if(status == 1):

                pass

                # print("LP is infeasible status 1")



            elif(status == 0 and T[1][1] == 0):

                valid=1

                pass

                # print("basic feasible solution found , drive out aux vars")



            elif(status == 0 and T[1][1] < 0):

                pass

                # print("LP is infeasible status 0 cost > 0")



            else:

                pass





            #driving out auxillary vairables:

            i=2

            while(i<num_constraint+2):



                if(myDict[T[i][0]]=="auxillary_vars"):

                    operation_performed=False

                    for j in range(2,num_vars+2):

                        if(T[i][j]!=0):

                            performOperations(T,i,j)

                            operation_performed=True

                            break

                    if(operation_performed==False):

                        T.pop(i)

                        i-=1

                        num_constraint-=1

                i+=1

            result = [row[:num_vars+2] for row in T[2:]]



            return result,valid



        #//PHASE2 



        A,b,c,myDict,objective = read_input("input_ilp.txt")

        base_matrix,valid = phase_I(A,b,myDict)

        

        first_row=[Fraction(0)]

        for  i in range(1,len(base_matrix[0])):

            first_row.append(Fraction(phase2firstrow(base_matrix, i, c)))

        base_matrix.insert(0,first_row)



        second_row=[Fraction(0),Fraction(0)]

        for i in range(2, len(base_matrix[0])):

            second_row.append(Fraction(i-2))

        base_matrix.insert(0,second_row)



        initial_matrix = copy.deepcopy(base_matrix)



        ansDict = {}

        ansDict["initial_tableau"] = (initial_matrix)





        if(valid==1):

        

            iteration_max = 100000

            i = 0

            # 0 --> fes  1 --> unfes 

            status = 0



            while(True and i < iteration_max):



                i+=1



                pivotColList = []

        

                

                for col in range(2, len(base_matrix[0])):

                    if(base_matrix[1][col] < 0):

                        pivotColList.append(col)

                



                if(len(pivotColList) == 0):

                    #all ci >=0, optimal solution found!

                    break

                

                pivotCol = Fraction(-1)

                positiveFound = False



                for colIndex in pivotColList:

                    for i in range(2,len(base_matrix)):

                        if(base_matrix[i][colIndex]>0):

                            pivotCol = colIndex

                            positiveFound=True

                    

                if(positiveFound == False):

                    status = 1

                    break





                minValue = 1e10

                minIndex = -1



                for row in range(2,len(base_matrix)):

                        

                    if(base_matrix[row][pivotCol] <= 0):

                        continue

                        

                    ratio = base_matrix[row][1]/base_matrix[row][pivotCol]

                    if(ratio < minValue):

                        minValue = ratio

                        minIndex = row





                if(minIndex == -1):

                    # all were non postive, and unbded

                    status = 1

                    break

                

                pivotRow = minIndex

                

                base_matrix = performOperations(base_matrix,pivotRow,pivotCol)

            



            if(status == 1):

                ansDict["final_tableau"]= (base_matrix)

                ansDict["solution_status"] = "unbounded"

                ansDict["optimal_solution"]= None

                ansDict["optimal_value"] = None

                

            



            elif(status == 0):



                ansDict["final_tableau"]= (base_matrix)

                ansDict["solution_status"] = "optimal"



                solution = [Fraction(0)] * (len (base_matrix[0]) - 2)



                for i in range (len(base_matrix) - 2):

                    solution[int(base_matrix[i + 2][0])] = base_matrix[i+2][1]

                

                final_values = []

                for i in range(len(solution)):

                    if(myDict[i]=="decision_vars"):

                        final_values.append(solution[i])

                

                ansDict["optimal_solution"] = final_values

                ansDict["optimal_value"] =  -objective*base_matrix[1][1]



            else:

                pass





        elif(valid == 0):

            ansDict["final_tableau"]= (base_matrix)

            ansDict["solution_status"] = "infeasible"

            ansDict["optimal_solution"]= None

            ansDict["optimal_value"] = None



        return ansDict,myDict,A,b,c,objective


    def dual_simplex(T):

        infinity = False

        while(True):

            negative_xB = []

            for i in range(2,len(T)):

                if(T[i][1] < 0):

                    negative_xB.append(i)



            if(len(negative_xB) == 0):

                #all xB were non negative: algo terminates , we have found an optimal solution:

                break



            else:

                pivotRow = Fraction(-1)

                for i in negative_xB:

                    for j in range(2,len(T[0])):

                        if(T[i][j] < 0):

                            pivotRow = i

                            break    



                if(pivotRow == -1):

                    print("all vi were postive optimal cost +infinity")

                    infinity = True

                    break

                

                else:

                    ##pivotRow Found 

                    #now find pivot column:

                    pivotCol = Fraction(-1)

                    minIndex = Fraction(-1)

                    minValue = 1e10



                    neg_vi = []

                    for col in range(2,len(T[0])):

                        if(T[pivotRow][col] < 0):

                            neg_vi.append(col)

                    

                    for col in neg_vi:

                        ratio = (T[1][col])/(abs(T[pivotRow][col]))

                        if(ratio < minValue):

                            minValue = ratio

                            minIndex = col



                    pivotCol = minIndex

                    ##now pivot Element Is Read with pivotRow and pivotCol

                    T = performOperationsDual(T,pivotRow,pivotCol)

        

        return T,infinity
       

    def displayAnswer(T,initial_solution,myDict,status, cuts,obj):

        print("initial_solution:",end = " ")
        for i in range(len(initial_solution)-1):
            print(float(initial_solution[i]), end = ",")
        print(float(initial_solution[len(initial_solution)-1]))
    
        all_solution = [0]*len(myDict)
        final_solution = []

        for i in range(2,len(T)):
            all_solution[int(T[i][0])] = int(T[i][1])

        for key in myDict:
            if(myDict[key] == "decision_vars"):
                final_solution.append(all_solution[key])
        
        print("final_solution:",end= " ")
        for i in range(len(final_solution)-1):
            print(final_solution[i], end = ",")
        print(final_solution[len(final_solution)-1])
        
        print("solution_status:",status)

        print("number_of_cuts:", cuts)  

        print("optimal_value:",-obj*float(T[1][1]))
        

    def gomory_algo():

        ansDict,myDict,A,b,c,objective = simplex_algo()
        
        keys_to_remove = [key for key, value in myDict.items() if value == 'auxillary_vars']

        for key in keys_to_remove:
            del myDict[key]


        initial_solution = ansDict["optimal_solution"]

        solution_status = ansDict["solution_status"]

        if(solution_status == "infeasible" or solution_status == "unbounded"):
            print("initial_solution:",None)
            print("final_solution:",None)
            print("solution_status:",solution_status)
            print("number_of_cuts:",None)
            print("optimal_value",None)
            return

        T =  ansDict["final_tableau"]

        number_of_cuts = 0

        while(solve(T)[0]):
            T,myDict = addGomoryConstraint(solve(T)[1],T,myDict)
            number_of_cuts += 1
            T,inf = dual_simplex(T)

        displayAnswer(T,initial_solution,myDict,solution_status, number_of_cuts,objective)

    #function call
    gomory_algo()
    return

gomory_cut_algo()