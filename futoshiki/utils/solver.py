import subprocess
def ijk_to_num_case (a,b,c,n) :
    v = 1
    for i in range (1,n+1) :
        for j in range (1,n+1) :
            for k in range (1, n + 1) :
                if (a == i and b == j and k == c) :
                    return v 
                else :
                    v += 1

#=====================        main       =============================== 

n = 5

#=======================================================================

#======================================================================= 


#======================================================================= 

#======================================================================= 

def constraints_01 (n) :
    constraints = []
    
    for i in range (1,n+1) :
        for j in range (1,n+1) :
            constraint = []
            for k in range (1, n + 1) :
                constraint.append(f"{ijk_to_num_case (i,j,k,n)} " )
            constraint.append (" 0 ")
            constraints.append(constraint )
    return constraints
#======================================================================= 

def generate_clauses_5(n):
    clauses = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                for l in range(k+1, n+1):
                    clauses.append([str(-ijk_to_num_case(i,j,k,n))]+["  "] +[ str(-ijk_to_num_case(i,j,l,n))] + ["  0 "])
                for p in range(1, k):
                    clauses.append([str(-ijk_to_num_case(i,j,k,n))]+ ["  "]+[str(-ijk_to_num_case(i,j,p,n))]+ [" 0 "])
            for p in range(1, n+1):
                if p != k:
                    clauses.append([str(-ijk_to_num_case(i,j,k,n))]+["  "]+[ str(-ijk_to_num_case(i,j,p,n))]+ [" 0 "])
    return clauses


clauses = generate_clauses_5(n)
for clause in clauses:
    print(clause)

















#======================================================================= 
def constraints_02 (n) :
    constraints = []

    clauses = []
    clause = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                clause = []
                for p in range(1, n + 1):
                    if (i != p) :
                        clause.append(f"-{ijk_to_num_case (i,j,k,n)}  -{ijk_to_num_case (p,j,k,n)} " )
                        clause.append (" 0 ")
                        clauses.append(clause)
                        clause = []

    return clauses
#======================================================================= 

#======================================================================= 
def constraints_03 (n) :
    constraints = []

    clauses = []
    clause = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                
                for p in range(1, n + 1):
                    if (j != p) :
                        clause.append(f"-{ijk_to_num_case (i,j,k,n)}  -{ijk_to_num_case (i,p,k,n)} " )
                        clause.append (" 0 ")
                        clauses.append(clause)
                        clause = []

    return clauses
#======================================================================= 


#=======================================================================
ma_liste = constraints_01(n) + constraints_02(n) + constraints_03(n) + generate_clauses_5(n)

#=======================================================================

#=======================================================================
with open('f.cnf', 'w') as fichier:
    fichier.write("p  cnf "  +str (n*n*n) +" "+ str(len (ma_liste))  + '\n')
    for element in ma_liste:
        cc =""
        for p in element :
            cc += p
        fichier.write(cc + '\n')
#=======================================================================



#=======================================================================
resCmd = subprocess.run(["z3",  "f.cnf"], capture_output=True, text=True).stdout
# Ecrit le resultat de la commande dans un fichier
file = open("s.cnf", "w")
file.write(str(resCmd))

solution = resCmd.split("v")[0].split()
#=======================================================================




#=======================================================================
def delNegNumbers(number: str):
    return not list(number)[0] == '-'
solution = list(filter(delNegNumbers, solution))
solution.pop(0)
print (solution)
sss = solution
#=======================================================================
print (sss)
#=======================================================================



#=======================================================================
def to_tuple (a,n) :
    v = 1
    for i in range (1,n+1) :
        for j in range (1,n+1) :
            for k in range (1, n + 1) :
                if (a == v) :
                    return  (i,j,k)
                else :
                    v += 1
print ("\n")
es = 1 
for p in sss :
    if es <= n :
        print(to_tuple (int (p),n), end= "  ")
        es += 1
    else :
        print ("\n")
        print(to_tuple (int (p),n), end= "  ")
        es = 2
#=======================================================================
print ("\n")
#=======================================================================



#=======================================================================
def creer_puzzle(coord_list, n):
    if n > 9:
        return "La taille du puzzle doit être inférieure à 9."

    # Créer un puzzle vide de taille n x n
    puzzle = [[0 for _ in range(1,n+1)] for _ in range(1,n+1)]

    # Remplir le puzzle avec les coordonnées fournies
    for coord in coord_list:
        i, j, k = coord
        
        puzzle[i][j] = k
     

    return puzzle
# print (creer_puzzle(puzz, 4))







# def constraints_04 (n) :
#     constraints = []

#     clauses = []

#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             for k in range(1, n + 1):
#                 clause = []
#                 for p in range(1, n + 1):
#                     if (p != i or (f"-{(p,j,k)} " not in clause) ):
#                         clause.append(f"-{ (p,j,k)} " )
#                 clause.append (" 0 ")
#                 clauses.append(clause)

#     return clauses


# lll = constraints_04 (n)
# print (constraints_04 (3))

# with open('test.txt', 'w') as fichier:
#     fichier.write("p  cnf "  +str (n*n*n) +" "+ str(len (lll))  + '\n')
#     for element in lll:
#         cc =""
#         for p in element :
#             cc += p
#         fichier.write(cc + '\n')

# print (constraints_03(3))
# print (ijk_to_num_case (3,3,3,3)  )


