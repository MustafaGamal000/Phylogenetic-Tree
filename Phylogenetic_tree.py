matrix = [[0 for i in range(6)] for j in range(6)]
label = ['A', 'B', 'C', 'D', 'E' , 'F']

def _IntializeMatrix(seq1, seq2, index1, index2):
    global matrix
    diff = 0
    lenOfAll = len(A)
    if(index1 == index2):
        matrix[index1][index2] = 0
    else:
        for i in range (lenOfAll):
            if(seq1[i] != seq2[i]):
                diff += 1
                matrix[index1][index2] = diff

def findLowestCell():
    global label
    x=-1
    y =-1
    min = float("inf")
    for i in range (len(matrix)):
        for j in range(len(matrix[i])):
            if(min > matrix[i][j] and matrix[i][j] != 0):
                min = matrix[i][j]
                x=i
                y=j
    label[x] = ("(" + label[x]+" "+label[y]+")")
    del label[y]
    return x,y
	

def creatNewMatrix(x, y):
    global matrix
    row =[]
    avg = -1
    for i in range (len(matrix)):
        if(matrix[x][i] == 0):
            row.append(0)			
        elif (matrix[y][i] != 0):
            avg = (matrix[x][i] + matrix[y][i]) / 2
            row.append(avg)
            
    for j in matrix: 
        del j[y]
    del matrix[x]
    del matrix[y]
    matrix.insert(x,row)
			
    

    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            if(matrix[i][j] == 0):
                break
            elif(i == j):
                matrix[i][j] = 0;
            else:
                matrix[i][j] = matrix[j][i]
			
				
    print("\n")
    for line in matrix:
        print (line)

def UPGMA():
    global label
    while (len(label) > 2):
        x, y = findLowestCell()
        creatNewMatrix(x,y)
        print(label)

    label[x] = ("(" + label[x]+" "+label[y]+")")
    del label[y]
    print ("\nFinal Tree: "+ str(label));
	


if __name__ == '__main__':
    A = "ATCGTGGTACTG"
    B = "CCGGAGAACTAG"
    C = "AACGTGCTACTG"
    D = "ATGGTGAAAGTG"
    E = "CCGGAAAACTTG"
    F = "TGGCCCTGTATC"

    arrStr = [A,B,C,D,E,F]
    for seq1 in arrStr:
        for seq2 in arrStr:
            _IntializeMatrix(seq1, seq2, arrStr.index(seq1), arrStr.index(seq2))

	
    for line in matrix:
        print (line)


    UPGMA()
	


