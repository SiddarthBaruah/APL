#%%
def problem1(N):
    res=1
    for i in range(1,N+1):
        res *= i
    return res

#%%
def Row_reduce(A,b):

    matrix_size= len(A)

    for row in range(matrix_size):

        for iter in range(row, matrix_size):
            
            norm= A[iter][row]
            if norm !=0:
                for column in range(row,matrix_size):
                    A[iter][column]=round(A[iter][column]/norm,2)
                b[iter]= round(b[iter]/norm)
        
        for iter in range(row+1, matrix_size):
            if A[iter][row]:
                for column in range(row, matrix_size):
                    A[iter][column] -= A[row][column]
                b[iter]-= b[row]
    
    return [A,b]
#%%
def Row_reduce_bet(A,b):
    lenrow= len(A[0])
    lencolumn= len(A)
    if lencolumn>=lenrow:
        for iter in range(lenrow):

            for row_num in range(iter,lencolumn):

                norm = A[row_num][iter]

                if norm!=0:
                    for column_num in range(iter, lenrow):
                        A[row_num][column_num] /= norm
                    b[row_num] /= norm
            
            for row_num in range(iter+1, lencolumn):

                if A[row_num][iter]:
                    for column in range(iter, lenrow):
                        A[row_num][column] -= A[iter][column]
                    b[row_num] -= b[iter]
    for row in range(lencolumn):
        for column in range(lenrow):
            A[row][column]= round(A[row][column],3) 
    for value in range(lencolumn):
        b[value]= round(b[value],3)
    return [A,b]
#%%
def check_solvability(A,b):
    len_row= len(A[0])
    len_column= len(A)
    prod=1
    if len_column> len_row:
        for row in range(len_row):
            prod *= A[row][row]
            if prod ==0:
                print("No solution")
                return 0
            for column in range(len_row):
                if A[row][column] != 0:
                    break
                if  A[row][column] != 0 and column== len_row:
                    if b[row]==0:
                        print("Infinite solution")
                        return 0
                    else:
                        print("No solution")
                        return 0
        if b[len_row]!= 0:
            print("It is unsolvable!")
            return 0
        return 1
    else:
        print("Infinite solution")
        return 0
            
        

        
#%%
def transpose(A):
    len_= len(A)
    newA=[]
    for row in reversed(A):
        new_row=[]
        for num in reversed(row):
            new_row.append(num)
        newA.append(new_row)
    return newA
#%%
def return_required_matrix(A,b):
    len_row= len(A[0])
    mat= []
    res= []
    for row in range(len_row):
        mat.append(A[row])
        res.append(b[row])
    return mat, res
#%%
def reversed_(b):
    c=[]
    for i in reversed(range(len(b))):
        c.append(b[i])
    return c
#%%
def solve(A,b):
    if check_solvability(A,b):
        sol=[]
        A, b= return_required_matrix(A,b)
        A= transpose(A)
        b= reversed_(b)
        sol.append(b[0])
        len_= len(A[0])
        check=1
        for row in range(len_):
            check *= A[row][row]
        if check:
            for row in range(1,len_):
                sum=0
                for column in range(0, row):
                    sum += A[row][column]*sol[column]
                sol.append(b[row]- sum)
        else:
            print("No solution")
            return -1
        return reversed_(sol)
#%%
class matrix_solver():
    def __init__(self, A, b):
        self.A= A
        self.b=b
        self.rowreduce=0
    
    def Row_reduce(self):
        lenrow= len(self.A[0])
        lencolumn= len(self.A)
        if lencolumn>=lenrow and self.rowreduce==0:
            for iter in range(lenrow):

                for row_num in range(iter,lencolumn):

                    norm = self.A[row_num][iter]

                    if norm!=0:
                        for column_num in range(iter, lenrow):
                            self.A[row_num][column_num] /= norm
                        self.b[row_num] /= norm
                
                for row_num in range(iter+1, lencolumn):

                    if self.A[row_num][iter]:
                        for column in range(iter, lenrow):
                            self.A[row_num][column] -= self.A[iter][column]
                        self.b[row_num] -= self.b[iter]
                self.rowreduce=1
        for row in range(lencolumn):
            for column in range(lenrow):
                self.A[row][column]= round(self.A[row][column],3) 
        for value in range(lencolumn):
            self.b[value]= round(self.b[value],3)
        
        return [self.A,self.b]


    def transpose(self):
        len_= len(self.A)
        newA=[]
        for row in reversed(self.A):
            new_row=[]
            for num in reversed(row):
                new_row.append(num)
            newA.append(new_row)
        return newA


    def reversed_(self):
        c=[]
        for i in reversed(range(len(self.b))):
            c.append(self.b[i])
        return c

    def check_solvability(self):
        len_row= len(self.A[0])
        len_column= len(self.A)
        prod=1
        if len_column> len_row:
            for row in range(len_row):
                prod *= self.A[row][row]
                if prod ==0:
                    print("No solution")
                    return 0
                for column in range(len_row):
                    if self.A[row][column] != 0:
                        break
                    if  self.A[row][column] != 0 and column== len_row:
                        if b[row]==0:
                            print("Infinite solution")
                            return 0
                        else:
                            print("No solution")
                            return 0
            if self.b[len_row]!= 0:
                print("It is unsolvable!")
                return 0
            return 1
        else:
            print("Infinite solution")
            return 0
            
    def return_required_matrix(self):
        len_row= len(self.A[0])
        mat= []
        res= []
        for row in range(len_row):
            mat.append(self.A[row])
            res.append(self.b[row])
        return mat, res 

    def solve(self):
        if self.rowreduce==0:
            self.A, self.b= self.rowreduce()
        if self.check_solvability(self.A,self.b):
            sol=[]
            self.A, self.b= return_required_matrix(self.A,self.b)
            self.A= self.transpose(self.A)
            self.b= self.reversed_(self.b)
            sol.append(self.b[0])
            len_= len(self.A[0])
            check=1
            return reversed_(sol)


# %%
inp= [[1,2,3,4],[3,1,1,2],[4,1,3,2],[5,6,1,1]]
sl= [40,23,33,26]
A,b=Row_reduce(inp, sl)
print(A)
print(b)
#%%
inp= [[1,2,3,4],[3,1,1,2],[4,1,3,2],[5,6,1,1],[9,7,4,3]]
sl= [40,23,33,26,59]
#%%
inp= [[0,0,0,2],[0,1,2,0],[1,0,0,0],[0,0,1,4]]
sl=[12,9,2,28]
A,b=Row_reduce(inp, sl)
print(A)
print(b)
#%%
solve(A,b)
#%%
with open("circuit.txt") as f:
    a= f.readlines()
    print(a)
# %%

def give_nodes(circuit):
    nodes= []
    start=0
    num_vol=0
    for line in circuit:
        line= line.split()
        if line[0]== ".circuit":
            start=1
            continue
        elif line[0]== '.end':
            start=0
            break
        if start:
            try:
                check1= nodes.index(line[1])
            except:
                nodes.append(line[1])
            try:
                check1= nodes.index(line[2])
            except:
                nodes.append(line[2])
    for line in circuit:
        line=line.split()
        try:
            if line[3]== 'dc':
                nodes.append("I"+line[0])
        except:
            pass
    return nodes
        
#%%
def make_equations(circuit, nodes):
    coefficient_matrix= []
    const_vector= []
    #for the KCL
    for node in nodes:
        tempequation= [0]*len(nodes)
        tempsol=[0]
        for line in circuit:
            line= line.split()
            if node in line:
                if line[0][0] == "R":
                    Register= float(line[3])
                    tempequation[nodes.index(line[1])] += 1/Register
                    tempequation[nodes.index(line[2])] -= 1/Register
                if line[0][0]== "V":
                    if line.index(node)==1:
                        tempequation[nodes.index("I"+line[0])] += 1
                    else:
                        tempequation[nodes.index("I"+line[0])] -= 1        
        coefficient_matrix.append(tempequation)
        const_vector.append(tempsol[0])
    
    #for the voltages
    for line in circuit:
        tempequation= [0]*len(nodes)
        tempsol=[0]
        line= line.split()
        if line[0][0]=="V":
            tempequation[nodes.index(line[2])] +=1
            tempequation[nodes.index(line[1])] +=-1
            tempsol[0] += float(line[4])
        coefficient_matrix.append(tempequation)
        const_vector.append(tempsol[0])
    
    return coefficient_matrix, const_vector
#%%

solver= matrix_solver(A,B)
#%%
sol= solver.solve()

#%%
import numpy as np

                

                
                


# %%
