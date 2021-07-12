import sys

def lcs2(s1, s2):
	matrix = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]
	for i in range(1,len(s1)+1):
		for j in range(1,len(s2)+1):
			if s1[i-1] == s2[j-1]:
				matrix[j][i] = 1+ matrix[j-1][i-1]
			else:
				matrix[j][i] = max(matrix[j][i-1],matrix[j-1][i])
	return matrix[j][i]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    s1 = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    s2 = data[:m]

    print(lcs2(s1, s2))