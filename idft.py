from math import pi,e
import matplotlib.pyplot as plt

def Line(a,b):
	x = [b, b]
	y = [0, a]
	plt.plot(x, y, marker = 'o')

def Graph(t_n, xlab, ylab, heading):

	mxv= max([abs(t_n[x]) for x in range(len(t_n))])
	plt.axhline(0, color = 'black')
	plt.axvline(0, color = 'black')
	plt.axis([-1, len(t_n)+1, -5, mxv +2])

	plt.title(heading)
	plt.xlabel(xlab)
	plt.ylabel(ylab)


	for i in range(len(t_n)):
		Line(abs(t_n[i]), i)
	plt.show()


print("Enter N")
n = int(input())
print("Enter the input signal:")
x = [complex(i) for i in input().split()]
w = e** complex (0, 2*pi/n)
D = []
for i in range(n):
	temp= [w** (i*j) for j in range(n)]
	D.append(temp)
output=[]
for i in range(n):
	sum_temp=0j
	for j in range(n):
		sum_temp += D[i][j] * x[j]
	output.append(sum_temp)

#print(output)
ans =[]


for i in range(n):
	ans.append(round(output[i].real, 2) + round(output[i].imag, 2)*1j)

Graph(x,'n--->', 'x[n]---->', 'Input Signal')
Graph(ans,'n--->', 'X[n]---->', 'Inverse Fourier Transform')
print("Output:")
print(ans)

	
#print(x)

