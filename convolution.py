import time
import matplotlib.pyplot as plt

def Line(a,b):
	x = [b, b]
	y = [0, a]
	plt.plot(x, y, marker = 'o')

def Graph(t_n, pos_t_n, xlabel, ylabel, heading):

	plt.axhline(0, color = 'black')
	plt.axis([pos_t_n[0]-1, pos_t_n[len(pos_t_n)-1]+1, min(t_n)-1, max(t_n)+1])

	plt.title(heading)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)


	for i in range(len(t_n)):
		Line(t_n[i], pos_t_n[i])
	plt.show()

def main():
	print("Enter input signal x[n]")
	x = [int(i) for i in input().split()]
	print("Enter position of input signal")
	pos_x = [int(i) for i in input().split()]
	print("Enter signal h[n]")
	h = [int(i) for i in input().split()]
	print("Enter position of signal h[n]")
	pos_h = [int(i) for i in input().split()]
	pos_y=[]
	y=[]
	for i in range(len(x)):
		for j in range(len(h)):
			if pos_x[i]+pos_h[j] not in pos_y:
				pos_y.append(pos_x[i]+pos_h[j])
				y.append(x[i]*h[j])
			else:
				idx = pos_y.index(pos_x[i]+pos_h[j])
				y[idx]+=(x[i]*h[j])

	print("Output signal:")
	print("y[n]:",end='')
	print(y)
	print("n:",end='')
	print(pos_y)
	Graph(x,pos_x,"n","x[n]","Input signal for convolution" )
	Graph(h,pos_h,"n","h[n]","Impulse response for convolution" )
	Graph(y,pos_y,"n","y[n]","Output signal for convolution" )
	

if __name__ == '__main__':
	main()
