import subprocess


def ijk_to_num_case(a, b, c, n):
    v = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n + 1):
                if (a == i and b == j and k == c):
                    return v
                else:
                    v += 1


def creer_puzzle(coord_list, n):
    if n > 9:
        return "La taille du puzzle doit être inférieure à 9."

    # Créer un puzzle vide de taille n x n
    puzzle = [[0 for _ in range(1, n+1)] for _ in range(1, n+1)]

    # Remplir le puzzle avec les coordonnées fournies
    for coord in coord_list:
        i, j, k = coord

        puzzle[i][j] = k

    return puzzle


def constraints_01(n):
    constraints = []

    for i in range(1, n+1):
        for j in range(1, n+1):
            constraint = []
            for k in range(1, n + 1):
                constraint.append(f"{ijk_to_num_case (i,j,k,n)} ")
            constraint.append(" 0 ")
            constraints.append(constraint)
    return constraints


def delNegNumbers(number: str):
    return not list(number)[0] == '-'


def to_tuple(a, n):
    v = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n + 1):
                if (a == v):
                    return (i, j, k)
                else:
                    v += 1


def constraints_02(n):

    clauses = []
    clause = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                clause = []
                for p in range(1, n + 1):
                    if (i != p):
                        clause.append(
                            f"-{ijk_to_num_case (i,j,k,n)}  -{ijk_to_num_case (p,j,k,n)} ")
                        clause.append(" 0 ")
                        clauses.append(clause)
                        clause = []

    return clauses


def constraints_03(n):

    clauses = []
    clause = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):

                for p in range(1, n + 1):
                    if (j != p):
                        clause.append(
                            f"-{ijk_to_num_case (i,j,k,n)}  -{ijk_to_num_case (i,p,k,n)} ")
                        clause.append(" 0 ")
                        clauses.append(clause)
                        clause = []

    return clauses


def solve(n: int):

    constraints = constraints_01(n) + constraints_02(n) + constraints_03(n)

    with open('f.cnf', 'w') as fichier:
        fichier.write("p  cnf " + str(n*n*n) + " " +
                      str(len(constraints)) + '\n')
        for element in constraints:
            cc = ""
            for p in element:
                cc += p
            fichier.write(cc + '\n')

    resCmd = subprocess.run(
        ["z3",  "f.cnf"], capture_output=True, text=True).stdout
    # Ecrit le resultat de la commande dans un fichier
    file = open("s.cnf", "w")
    file.write(str(resCmd))

    solution = resCmd.split("v")[1].split()

    solution.pop(-1)

    solution = list(filter(delNegNumbers, solution))

    formattedSolution = []

    es = 1
    for p in solution:
        if es <= n:
            # print(to_tuple (int (p),n), end= "  ")
            formattedSolution.append(to_tuple(int(p), n))
            es += 1
        else:
            # print ("\n")
            # print(to_tuple (int (p),n), end= "  ")
            formattedSolution.append(to_tuple(int(p), n))
            es = 2

    # print(formattedSolution)
    # print('\n')

    return formattedSolution


def printSolution(solution):

    n = int(len(solution) ** 0.5)

    for i in range(n):
        for j in range(n) :
          print(solution[i*n+j][2], end=' ')
        print('\n')


# printSolution(solve(4))
