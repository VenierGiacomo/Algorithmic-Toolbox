# python3
import numpy

def EditDistance(s1, s2):
    lenght_s1 = len(s1)
    lenght_s2 = len(s2)

    matrix = numpy.zeros((lenght_s1+1 , lenght_s2+1))
    for i in range(lenght_s1+1):
        matrix[i][0] = i

    for i in range(lenght_s2+1):
        matrix[0][i] = i

  

    for i in range(1, lenght_s1+1):
        for j in range(1, lenght_s2+1):
            insert    = matrix[i][j-1]   + 1
            deletion  = matrix[i-1][j]   + 1
            match     = matrix[i-1][j-1]
            notmatch  = matrix[i-1][j-1] + 1
           
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = min(insert, deletion, match)
            if s1[i-1] != s2[j-1]:
                matrix[i][j] = min(insert, deletion, notmatch)
    
    return (int(matrix[lenght_s1][lenght_s2]), matrix)

def OptimalAlignment(matrix, s1, s2, top, bottom, i, j):

    if i == 0 and j == 0:
        return (' '.join(top[::-1]), ' '.join(bottom[::-1]))

    if i>0 and matrix[i][j] == matrix[i-1][j] + 1:
        top.append(f'|{s1[i-1]}|')
        bottom.append('|-|')
        return OptimalAlignment(matrix, s1, s2, top, bottom, i-1, j)

    elif j>0 and matrix[i][j] == matrix[i][j-1] + 1:
        bottom.append(f'|{s2[j-1]}|')
        top.append('|-|')
        return OptimalAlignment(matrix, s1, s2, top, bottom, i, j-1)

    else:
        top.append(f'|{s1[i-1]}|')
        bottom.append(f'|{s2[j-1]}|')
        return OptimalAlignment(matrix, s1, s2, top, bottom, i-1, j-1)

if __name__ == '__main__':
    s1, s2 = input(), input()
    edit_distance, matrix = EditDistance(s1, s2)
    top, bottom = OptimalAlignment(matrix, s1, s2, [], [], len(s1), len(s2))

    print(f'Editing distance : {edit_distance}')
    print(f"Optimal alignment:\n{top}\n{bottom}")
