
import random
import math
import os
import sys

#Function to print the Matrix
def printMatrix(testMatrix):
        #print '\t',
        #for i in range(len(testMatrix[1])):
        #      print i,
        #print
        for i, element in enumerate(testMatrix):
              print  ',\t'.join(element)

#Fucntion for random sampling with replacement(if sample is greater than population)
def sample_wr(population, k):
    n = len(population)
    _random, _int = random.random, int  # speed hack 
    result = [None] * k
    for i in xrange(k):
        j = _int(_random() * n)
        result[i] = population[j]
    return result


def highway_continuation(Matrix,Current_Matrix,movement_direction,x_start_prob,y_start_prob,highway_num):
	#highway_num = str(int(highway_num)+1)
	x_fordist_start, y_fordist_start, x_fordist_end, y_fordist_end = 0, 0, 0, 0
	x_fordist_start = x_start_prob
	y_fordist_start = y_start_prob
	
	while x_start_prob > -1 and x_start_prob < w and y_start_prob > -1 and y_start_prob < h:
		#print x_start_prob,y_start_prob

		if movement_direction == "down":

				random_number_dir = random.randint(1,5)				
				#random_number_dir = 1
	
				#move in the same dir
				if 1 <= random_number_dir <=3:
					i=0
					while i<20:
						y_start_prob+=1
						x_start_prob=x_start_prob
						#make the change in the matrix
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break
						

				#move right	
				elif random_number_dir == 4:
					i=0
					while i<20:
						y_start_prob=y_start_prob
						x_start_prob-=1
						movement_direction = "left"
						#make the change in the matrix
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break



				#move left
				else:
					i=0
					while i<20:	
						y_start_prob=y_start_prob
						x_start_prob+=1
						movement_direction = "right"
						#make the change in the matrix
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

				

				
					
		elif movement_direction == "left":
		
			
				random_number_dir = random.randint(1,5)
				#move in the same dir
				if 1 <= random_number_dir <=3:
					i=0
					while i<20:
						x_start_prob-=1
						y_start_prob=y_start_prob
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

				#move right	
				elif random_number_dir == 4:
					i=0
					while i<20:
						x_start_prob=x_start_prob
						y_start_prob-=1
						movement_direction = "top"
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

				#move left
				else:
					i=0
					while i<20:

						x_start_prob=x_start_prob
						y_start_prob+=1
						movement_direction = "down"
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

				

					


	

		elif movement_direction == "top":
		
			
				random_number_dir = random.randint(1,5)
				#move in the same dir
				if 1 <= random_number_dir <=3:
					i=0
					while i<20:
						y_start_prob-=1
						x_start_prob=x_start_prob
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

				#move right	
				elif random_number_dir == 4:
					i=0
					while i<20:
						y_start_prob=y_start_prob
						x_start_prob+=1
						movement_direction = "right"
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

				#move left
				else:
					i=0
					while i<20:
						y_start_prob=y_start_prob
						x_start_prob-=1
						movement_direction = "left"
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

			

	

		else:
		
			
				random_number_dir = random.randint(1,5)
				#move in the same dir
				if 1 <= random_number_dir <=3:
					i=0
					while i<20:
						x_start_prob+=1
						y_start_prob=y_start_prob
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

				#move right	
				elif random_number_dir == 4:
					i=0
					while i<20:
						x_start_prob=x_start_prob
						y_start_prob+=1
						movement_direction = "down"
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

				#move left
				else:	
					i=0
					while i<20:
						x_start_prob=x_start_prob
						y_start_prob-=1
						movement_direction = "top"
						if x_start_prob != -1 and x_start_prob != w and y_start_prob != -1 and y_start_prob != h:
							if Matrix[y_start_prob][x_start_prob] == '1':
								Matrix[y_start_prob][x_start_prob] = 'a'+highway_num
								i+=1
							elif Matrix[y_start_prob][x_start_prob] == '2':
								Matrix[y_start_prob][x_start_prob] = 'b'+highway_num
								i+=1
							else:
								#collision with either a or b, build again
								#try:
									Matrix = Current_Matrix
									#movement_direction = "down"
									#x_start_prob , y_start_prob = 0, 0
									#print "hi"
									generate_highways(Matrix,highway_num)
									break
								#except RuntimeError as r:
								#	os.system("python grid3.py")
						else:
							break

				
	x_fordist_end = x_start_prob
	y_fordist_end = y_start_prob						
	
	distance = math.sqrt(abs(x_fordist_start - x_fordist_end)*abs(x_fordist_start - x_fordist_end) + abs(y_fordist_start - y_fordist_end)*abs(y_fordist_start - y_fordist_end))

	#if distance < 100:
	#	Matrix = Current_Matrix
	#	generate_highways(Matrix,highway_num)
		#os.system()

	#print x_start_prob, y_start_prob
	#print distance
	Current_Matrix = Matrix		


#Function to generate highways
def generate_highways(Matrix,highway_num):
	#for choosing the side of the grid
	#1 = top , 2 = right , 3 = bottom , 4 = left
	x_start_prob , y_start_prob , x_end_prob , y_end_prob = 0, 0, 0, 0
	flag=0
	random_number = random.randint(1,4)
	#random_number = 1
	if random_number == 1:
		x_high = random.randint(0,w-1)
		for i in range(0,20):
			if Matrix[i][x_high] != '1' and Matrix != '2':
				flag=1
				i=0
				x_high = random.randint(0,w-1)
				
			else:
				flag=0

		if flag == 0:
			for i in range(0,20):
				if Matrix[i][x_high] == '1':
					Matrix[i][x_high] = 'a'+highway_num
				else:
					Matrix[i][x_high] = 'b'+highway_num

		x_start_prob = x_high
		y_start_prob = 19

		movement_direction = "down" 
		#print random_number_dir
		highway_continuation(Matrix,Current_Matrix,movement_direction,x_start_prob,y_start_prob,highway_num)
		
	elif random_number == 2:
		y_high = random.randint(0,h-1)
		for i in range(w-1,w-21,-1):
			if Matrix[y_high][i] != '1' and Matrix != '2':
				flag=1
				i=0
				y_high = random.randint(0,h-1)
				
			else:
				flag=0

		if flag == 0:
			for i in range(w-1,w-21,-1):
				if Matrix[y_high][i] == '1':
					Matrix[y_high][i] = 'a'+highway_num
				else:
					Matrix[y_high][i] = 'b'+highway_num
			

		x_start_prob = w-20
		y_start_prob = y_high

		random_number_dir = random.randint(1,5)
		movement_direction = "left" 
		#print random_number_dir
		highway_continuation(Matrix,Current_Matrix,movement_direction,x_start_prob,y_start_prob,highway_num)

	elif random_number == 3:
		x_high = random.randint(0,w-1)
		for i in range(h-1,h-21,-1):
			if Matrix[i][x_high] != '1' and Matrix != '2':
				flag=1
				i=0
				x_high = random.randint(0,w-1)
				
			else:
				flag=0

		if flag == 0:
			for i in range(h-1,h-21,-1):
				if Matrix[i][x_high] == '1':
					Matrix[i][x_high] = 'a'+highway_num
				else:
					Matrix[i][x_high] = 'b'+highway_num
			

		x_start_prob = x_high
		y_start_prob = h-20

		random_number_dir = random.randint(1,5)
		movement_direction = "top" 
		#print random_number_dir
		highway_continuation(Matrix,Current_Matrix,movement_direction,x_start_prob,y_start_prob,highway_num)

	else:
		y_high = random.randint(0,h-1)
		for i in range(0,20):
			if Matrix[y_high][i] != '1' and Matrix != '2':
				flag=1
				i=0
				y_high = random.randint(0,h-1)
				
			else:
				flag=0

		if flag == 0:
			for i in range(0,20):
				if Matrix[y_high][i] == '1':
					Matrix[y_high][i] = 'a'+highway_num
				else:
					Matrix[y_high][i] = 'b'+highway_num
			

		x_start_prob = 19
		y_start_prob = y_high

		random_number_dir = random.randint(1,5)
		movement_direction = "right" 
		#print random_number_dir
		highway_continuation(Matrix,Current_Matrix,movement_direction,x_start_prob,y_start_prob,highway_num)


#Function to genereate start and end cell
def generate_start_end():
	#-----------------------------------------Choosing Start cell
	#for choosing the side of the grid
	#1 = top , 2 = right , 3 = bottom , 4 = left
	generate_start_end.x_start = 0
	generate_start_end.y_start = 0
	generate_start_end.x_end = 0
	generate_start_end.y_end = 0
	random_number = random.randint(1,4)
	if random_number == 0:
		generate_start_end.x_start = random.randint(0,w-1)
		generate_start_end.y_start = random.randint(0,1)
	elif random_number == 1:
		generate_start_end.x_start = random.randint(w-2,w-1)
		generate_start_end.y_start = random.randint(0,h-1)
	elif random_number == 2:
		generate_start_end.x_start = random.randint(0,w-1)
		generate_start_end.y_start = random.randint(h-2,h-1)
	else:
		generate_start_end.x_start = random.randint(0,1)
		generate_start_end.y_start = random.randint(0,h-1)

	

	#---------------------------------------Choosing End cell
	#for choosing the side of the grid
	#1 = top , 2 = right , 3 = bottom , 4 = left
	random_number = random.randint(1,4)
	if random_number == 0:
		generate_start_end.x_end = random.randint(0,w-1)
		generate_start_end.y_end = random.randint(0,1)
	elif random_number == 1:
		generate_start_end.x_end = random.randint(w-2,w-1)
		generate_start_end.y_end = random.randint(0,h-1)
	elif random_number == 2:
		generate_start_end.x_end = random.randint(0,w-1)
		generate_start_end.y_end = random.randint(h-2,h-1)
	else:
		generate_start_end.x_end = random.randint(0,1)
		generate_start_end.y_end = random.randint(0,h-1)

	
	#Manhattan distance between start cell and end cell
	distance = abs(generate_start_end.x_start - generate_start_end.x_end) + abs(generate_start_end.y_start - generate_start_end.y_end)
	
	if distance<100:
		generate_start_end()
	else:
		#adding the start cell
		#Matrix[generate_start_end.y_start][generate_start_end.x_start] = 'start'
		#adding the end cell
		#Matrix[generate_start_end.y_end][generate_start_end.x_end] = 'end'
		return




#Creating the matrix
w, h = 160, 120
Matrix = [['1' for x in range(w)] for y in range(h)]
movement_direction = ""
highway_num = "0"
#x_start_global ,y_start_global = 0,0 
#x_end_global, y_end_global =0,0
#----------------------------------Choosing 8 random points for 'hard to traverse' cells
x = random.sample(xrange(w),8)
y = random.sample(xrange(h),8)

#Adding hard to traverse cells in the Matrix
for i in range(8):

	Matrix[y[i]][x[i]] = '2'
	#checking boundary conditions for row
	if x[i]-15 < 0:
		mx = 0
	else:
		mx = x[i]-15
	if x[i]+15 > w:
		nx = w
	else:
		nx = x[i]+15
	#checking boundary conditions for column	
	if y[i]-15 < 0:
		my = 0
	else:
		my = y[i]-15
	if y[i]+15 > h:
		ny = h
	else:
		ny = y[i]+15

	#making the 31x31 region around he center as hard to traverse
	for p in range(my,ny):
		for q in range (mx,nx):
			#Applying 50% probability to make it hard
			random_number = random.randint(0,1)
			if random_number == 1:
				#print p,q
				Matrix[p][q] = '2'
Current_Matrix = Matrix
#--------------------------------------Choosing Highways
generate_highways(Matrix,'1')
generate_highways(Matrix,'2')
generate_highways(Matrix,'3')
generate_highways(Matrix,'4')	


#--------------------------------------Choosing blocked cells
total_number_blocked = (w*h)/5

x_random = sample_wr(xrange(w),total_number_blocked)
y_random = sample_wr(xrange(h),total_number_blocked)

#adding blocked cells to the matrix
for i in range(total_number_blocked):
	#blocked cell cannot be on a highway
	if Matrix[y_random[i]][x_random[i]] != 'a1' and Matrix[y_random[i]][x_random[i]] != 'b1' and Matrix[y_random[i]][x_random[i]] != 'a2' and Matrix[y_random[i]][x_random[i]] != 'b2' and Matrix[y_random[i]][x_random[i]] != 'a3' and Matrix[y_random[i]][x_random[i]] != 'b3' and Matrix[y_random[i]][x_random[i]] != 'a4' and Matrix[y_random[i]][x_random[i]] != 'b4':
		Matrix[y_random[i]][x_random[i]] = '0'




#Function call to genrate start and end cell
generate_start_end()




#Call print function(for terminal output)
printMatrix(Matrix)

#Output the matrix to a file
orig_stdout = sys.stdout
f = file('grid_output.txt', 'w')
sys.stdout = f

print str(generate_start_end.x_start+1)+","+str(generate_start_end.y_start+1)
print str(generate_start_end.x_end+1)+","+str(generate_start_end.y_end+1)
for i in range(8):
	print str(x[i]+1)+","+str(y[i]+1)
print str(h)+","+str(w)

printMatrix(Matrix)

sys.stdout = orig_stdout
f.close()
	