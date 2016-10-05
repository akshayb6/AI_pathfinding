# - added moving diagonally
# - added path cost
# - added reading matrix from file
# - added scanMatrix to check cells

import heapq
import math
import sys
import time
from Tkinter import *
#The basic object here is a cell so we write a class for it. We store the coordinates x and y, the values of G and H plus the sum F.
class Cell(object):
    def __init__(self, x, y, reachable):
        """Initialize new cell.
        @param reachable is cell reachable? not a wall?
        @param x cell x coordinate
        @param y cell y coordinate
        @param g cost to move from the starting cell to this cell.
        @param h estimation of the cost to move from this cell
                 to the ending cell.
        @param f f = g + h
        """
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

#Next is our main class named AStar. Attributes are the open list heapified (keep cell with lowest F at the top), the closed list which is a set for 
#fast lookup, the cells list (grid definition) and the size of the grid.
class AStar(object):
    def __init__(self):
        # open list
        self.opened = []
        heapq.heapify(self.opened)
        # visited cells list
        self.closed = set()
        # grid cells
        self.cells = []
        self.grid_height = None
        self.grid_width = None
        self.heu = 0
        self.alg = 0

    #We create a simple method initializing the list of cells to match our example with the walls at the same locations.    
    def init_grid(self, width, height, walls, start, end, heu, alg):
        """Prepare grid cells, walls.
        @param width grid's width.
        @param height grid's height.
        @param walls list of wall x,y tuples.
        @param start grid starting point x,y tuple.
        @param end grid ending point x,y tuple.
        """
        self.grid_height = height
        self.grid_width = width

        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x, y) in walls:
                    reachable = False
                else:
                    reachable = True
                self.cells.append(Cell(x, y, reachable))
        self.start = self.get_cell(*start)
        self.end = self.get_cell(*end)
        self.heu = heu
        self.alg = alg

    #Our heuristic compute method:    
    def get_heuristic(self, cell):
        """Compute the heuristic value H for a cell.
        Distance between this cell and the ending cell multiply by 10.
        @returns heuristic value H
        """
        if self.heu == 1:
        #chebyshev
            return max(abs(cell.x - self.end.x),abs(cell.y - self.end.y))
        elif self.heu == 2:
        #manhattan
            return abs(cell.x - self.end.x)+abs(cell.y - self.end.y)
        elif self.heu == 3:
        #Euclidean
            return math.sqrt(abs(cell.x - self.end.x)*abs(cell.x - self.end.x)+abs(cell.y - self.end.y)*abs(cell.y - self.end.y))
        elif self.heu == 4:
        #canberra
            return (abs(cell.x-self.end.x)/(abs(cell.x)+abs(self.end.x)))+(abs(cell.y - self.end.y)/(abs(cell.y)+abs(self.end.y)))
        elif self.heu == 5:
        #Manhattan / 4
            return (abs(cell.x - self.end.x)+abs(cell.y - self.end.y))/4
        else:
            sys.exit(0)


    #We need a method to return a particular cell based on x and y coordinates.
    def get_cell(self, x, y):
        """Returns a cell from the cells list.
        @param x cell x coordinate
        @param y cell y coordinate
        @returns cell
        """
        return self.cells[x * self.grid_height + y]

    #Next is a method to retrieve the list of adjacent cells to a specific cell.    
    def get_adjacent_cells(self, cell):
        """Returns adjacent cells to a cell.
        Clockwise starting from the one on the right.
        @param cell get adjacent cells for this cell
        @returns adjacent cells list.
        """
        cells = []
        if cell.x < self.grid_width-1:
            cells.append(self.get_cell(cell.x+1, cell.y))
        if cell.y > 0:
            cells.append(self.get_cell(cell.x, cell.y-1))
        if cell.x > 0:
            cells.append(self.get_cell(cell.x-1, cell.y))
        if cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x, cell.y+1))

        if cell.x < self.grid_width-1 and cell.y > 0:
            cells.append(self.get_cell(cell.x+1, cell.y-1))
        if cell.x < self.grid_width-1 and cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x+1, cell.y+1))
        if cell.x > 0 and cell.y > 0:
            cells.append(self.get_cell(cell.x-1, cell.y-1))
        if cell.x > 0 and cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x-1, cell.y+1))
        
        return cells

    def get_fgh(self, x, y):
        fgh_cell = self.get_cell(x,y)
        return fgh_cell.f, fgh_cell.g, fgh_cell.h

    #Simple method to print the path found. It follows the parent pointers to go from the ending cell to the starting cell.
    def get_path(self):
        path_cost = 0
        cell = self.end
        path = [(cell.x, cell.y)]
        while cell.parent is not self.start:
            cell = cell.parent
            #path_cost = path_cost + cell.g
            #print path_cost
            path.append((cell.x, cell.y))

        path.append((self.start.x, self.start.y))
        path.reverse()
        return path

    #We need a method to calculate G and H and set the parent cell.
    def update_cell(self, adj, cell):
        """Update adjacent cell.
        @param adj adjacent cell to current cell
        @param cell current cell being processed
        """
        
        direction= ""
        adjacent_xy = [(adj.x,adj.y)]
        cell_xy = [(cell.x,cell.y)]

        if adj.x == cell.x+1 and adj.y == cell.y+1:
            direction = "d"
        elif adj.x == cell.x-1 and adj.y == cell.y+1:
            direction = "d"
        elif adj.x == cell.x+1 and adj.y == cell.y-1:
            direction = "d"
        elif adj.x == cell.x-1 and adj.y == cell.y-1:
            direction = "d"
        else:
            direction = "hv"

        if cell_xy[0] in normal and adjacent_xy[0] in normal and direction == "hv":
            adj.g = cell.g + 1
        if cell_xy[0] in normal and adjacent_xy[0] in normal and direction == "d":
            adj.g = cell.g + math.sqrt(2)

        if cell_xy[0] in hard and adjacent_xy[0] in hard and direction == "hv":
            adj.g = cell.g + 1.5
        if cell_xy[0] in hard and adjacent_xy[0] in hard and direction == "d":
            adj.g = cell.g + (math.sqrt(2)+math.sqrt(8))/2

        if cell_xy[0] in normal and adjacent_xy[0] in hard and direction == "hv":
            adj.g = cell.g + 2
        if cell_xy[0] in hard and adjacent_xy[0] in normal and direction == "hv":
            adj.g = cell.g + 2
        if cell_xy[0] in normal and adjacent_xy[0] in hard and direction == "d":
            adj.g = cell.g + math.sqrt(8)
        if cell_xy[0] in hard and adjacent_xy[0] in normal and direction == "d":
            adj.g = cell.g + math.sqrt(8)

        if cell_xy[0] in highway and adjacent_xy[0] in normal and direction == "hv":
            adj.g = cell.g + 1
        if cell_xy[0] in normal and adjacent_xy[0] in highway and direction == "hv":
            adj.g = cell.g + 1
        if cell_xy[0] in normal and adjacent_xy[0] in highway and direction == "d":
            adj.g = cell.g + math.sqrt(2)
        if cell_xy[0] in highway and adjacent_xy[0] in normal and direction == "d":
            adj.g = cell.g + math.sqrt(2)

        if cell_xy[0] in hard_highway and adjacent_xy[0] in normal and direction == "hv":
            adj.g = cell.g + 1.5
        if cell_xy[0] in normal and adjacent_xy[0] in hard_highway and direction == "hv":
            adj.g = cell.g + 1.5
        if cell_xy[0] in normal and adjacent_xy[0] in hard_highway and direction == "d":
            adj.g = cell.g + (math.sqrt(2)+math.sqrt(8))/2
        if cell_xy[0] in hard_highway and adjacent_xy[0] in normal and direction == "d":
            adj.g = cell.g + (math.sqrt(2)+math.sqrt(8))/2

        if cell_xy[0] in hard_highway and adjacent_xy[0] in hard and direction == "hv":
            adj.g = cell.g + 2
        if cell_xy[0] in hard and adjacent_xy[0] in hard_highway and direction == "hv":
            adj.g = cell.g + 2
        if cell_xy[0] in hard and adjacent_xy[0] in hard_highway and direction == "d":
            adj.g = cell.g + math.sqrt(8)
        if cell_xy[0] in hard_highway and adjacent_xy[0] in hard and direction == "d":
            adj.g = cell.g + math.sqrt(8)

        if cell_xy[0] in highway and adjacent_xy[0] in hard and direction == "hv":
            adj.g = cell.g + 1.5
        if cell_xy[0] in hard and adjacent_xy[0] in highway and direction == "hv":
            adj.g = cell.g + 1.5
        if cell_xy[0] in hard and adjacent_xy[0] in highway and direction == "d":
            adj.g = cell.g + (math.sqrt(2)+math.sqrt(8))/2
        if cell_xy[0] in highway and adjacent_xy[0] in hard and direction == "d":
            adj.g = cell.g + (math.sqrt(2)+math.sqrt(8))/2

        if cell_xy[0] in highway and adjacent_xy[0] in highway and direction == "hv":
            adj.g = cell.g + 0.25
        if cell_xy[0] in hard_highway and adjacent_xy[0] in hard_highway and direction == "hv":
            adj.g = cell.g + 0.5

        if cell_xy[0] in highway and adjacent_xy[0] in hard_highway and direction == "hv":
            adj.g = cell.g + 0.375
        if cell_xy[0] in hard_highway and adjacent_xy[0] in highway and direction == "hv":
            adj.g = cell.g + 0.375

        if cell_xy[0] in highway and adjacent_xy[0] in highway and direction == "d":
            adj.g = cell.g + math.sqrt(2)
        if cell_xy[0] in hard_highway and adjacent_xy[0] in hard_highway and direction == "d":
            adj.g = cell.g + math.sqrt(8)

        if cell_xy[0] in highway and adjacent_xy[0] in hard_highway and direction == "d":
            adj.g = cell.g + (math.sqrt(2)+math.sqrt(8))/2
        if cell_xy[0] in hard_highway and adjacent_xy[0] in highway and direction == "d":
            adj.g = cell.g + (math.sqrt(2)+math.sqrt(8))/2

        #adj.g = cell.g + 1
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        if self.alg == 1:
            w = 0
        if self.alg == 2:
            w = 1
        if self.alg == 3:
            w = 1.5

        adj.f = (w*adj.h) + adj.g
        #print adj.f

        del cell_xy[:]
        del adjacent_xy[:]

    #The main method implements the algorithm itself.    
    def solve(self):
        """Solve maze, find path to ending cell.
        @returns path or None if not found.
        """
        # add starting cell to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            # pop cell from heap queue
            f, cell = heapq.heappop(self.opened)
            # add cell to closed list so we don't process it twice
            self.closed.add(cell)
            # if ending cell, return found path
            if cell is self.end:
                return self.get_path(), self.end.g, len(self.closed)
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)
            for adj in adj_cells:
                if adj.reachable and adj not in self.closed:
                    if (adj.f, adj) in self.opened:
                        # if adj cell in open list, check if current path is
                        # better than the one previously found
                        # for this adj cell.
                        #if adj_cell.g > cell.g + 1:
                        direction= ""
                        adjacent_xy = [(adj.x,adj.y)]
                        cell_xy = [(cell.x,cell.y)]

                        if adj.x == cell.x+1 and adj.y == cell.y+1:
                            direction = "d"
                        elif adj.x == cell.x-1 and adj.y == cell.y+1:
                            direction = "d"
                        elif adj.x == cell.x+1 and adj.y == cell.y-1:
                            direction = "d"
                        elif adj.x == cell.x-1 and adj.y == cell.y-1:
                            direction = "d"
                        else:
                            direction = "hv"

                        if cell_xy[0] in normal and adjacent_xy[0] in normal and direction == "hv" and adj.g > cell.g + 1:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in normal and adjacent_xy[0] in normal and direction == "d" and adj.g > cell.g + math.sqrt(2):
                            self.update_cell(adj, cell)

                        if cell_xy[0] in hard and adjacent_xy[0] in hard and direction == "hv" and adj.g > cell.g + 1.5:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard and adjacent_xy[0] in hard and direction == "d" and adj.g > cell.g + (math.sqrt(2)+math.sqrt(8))/2:
                            self.update_cell(adj, cell)

                        if cell_xy[0] in normal and adjacent_xy[0] in hard and direction == "hv" and adj.g > cell.g + 2:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard and adjacent_xy[0] in normal and direction == "hv" and adj.g > cell.g + 2:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in normal and adjacent_xy[0] in hard and direction == "d" and adj.g > cell.g + math.sqrt(8):
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard and adjacent_xy[0] in normal and direction == "d" and adj.g > cell.g + math.sqrt(8):
                            self.update_cell(adj, cell)

                        if cell_xy[0] in highway and adjacent_xy[0] in normal and direction == "hv" and adj.g > cell.g + 1:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in normal and adjacent_xy[0] in highway and direction == "hv" and adj.g > cell.g + 1:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in normal and adjacent_xy[0] in highway and direction == "d" and adj.g > cell.g + math.sqrt(2):
                            self.update_cell(adj, cell)
                        if cell_xy[0] in highway and adjacent_xy[0] in normal and direction == "d" and adj.g > cell.g + math.sqrt(2):
                            self.update_cell(adj, cell)

                        if cell_xy[0] in hard_highway and adjacent_xy[0] in normal and direction == "hv" and adj.g > cell.g + 1.5:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in normal and adjacent_xy[0] in hard_highway and direction == "hv" and adj.g > cell.g + 1.5:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in normal and adjacent_xy[0] in hard_highway and direction == "d" and adj.g > cell.g + (math.sqrt(2)+math.sqrt(8))/2:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard_highway and adjacent_xy[0] in normal and direction == "d" and adj.g > cell.g + (math.sqrt(2)+math.sqrt(8))/2:
                            self.update_cell(adj, cell)

                        if cell_xy[0] in hard_highway and adjacent_xy[0] in hard and direction == "hv" and adj.g > cell.g + 2:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard and adjacent_xy[0] in hard_highway and direction == "hv" and adj.g > cell.g + 2:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard and adjacent_xy[0] in hard_highway and direction == "d" and adj.g > cell.g + math.sqrt(8):
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard_highway and adjacent_xy[0] in hard and direction == "d" and adj.g > cell.g + math.sqrt(8):
                            self.update_cell(adj, cell)

                        if cell_xy[0] in highway and adjacent_xy[0] in hard and direction == "hv" and adj.g > cell.g + 1.5:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard and adjacent_xy[0] in highway and direction == "hv" and adj.g > cell.g + 1.5:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard and adjacent_xy[0] in highway and direction == "d" and adj.g > cell.g + (math.sqrt(2)+math.sqrt(8))/2:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in highway and adjacent_xy[0] in hard and direction == "d" and adj.g > cell.g + (math.sqrt(2)+math.sqrt(8))/2:
                            self.update_cell(adj, cell)

                        if cell_xy[0] in highway and adjacent_xy[0] in highway and direction == "hv" and adj.g > cell.g + 0.25:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard_highway and adjacent_xy[0] in hard_highway and direction == "hv" and adj.g > cell.g + 0.5:
                            self.update_cell(adj, cell)

                        if cell_xy[0] in highway and adjacent_xy[0] in hard_highway and direction == "hv" and adj.g > cell.g + 0.375:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard_highway and adjacent_xy[0] in highway and direction == "hv" and adj.g > cell.g + 0.375:
                            self.update_cell(adj, cell)

                        if cell_xy[0] in highway and adjacent_xy[0] in highway and direction == "d" and adj.g > cell.g + math.sqrt(2):
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard_highway and adjacent_xy[0] in hard_highway and direction == "d" and adj.g > cell.g + math.sqrt(8):
                            self.update_cell(adj, cell)

                        if cell_xy[0] in highway and adjacent_xy[0] in hard_highway and direction == "d" and adj.g > cell.g + (math.sqrt(2)+math.sqrt(8))/2:
                            self.update_cell(adj, cell)
                        if cell_xy[0] in hard_highway and adjacent_xy[0] in highway and direction == "d" and adj.g > cell.g + (math.sqrt(2)+math.sqrt(8))/2:
                            self.update_cell(adj, cell)

                    else:
                        self.update_cell(adj, cell)
                        # add adj cell to open list
                        heapq.heappush(self.opened, (adj.f, adj))

#-------------------------------------------------------------------------------                        
w= 160
h= 120
Matrix = [['x' for x in range(w)] for y in range(h)]

i=0
j=0
blocked=list()
hard=list()
highway=list()
hard_highway=list()
normal=list()

temp=""

#reading matrix from txt file
with open('C:/Users/aksha/Documents/Zone/520/ass1/Maps/AI_Map1_1.txt') as f1:
    start=f1.readline().strip().split(',')
    end=f1.readline().strip().split(',')
    lines = f1.readlines()
count=0
open('AI.txt', 'w').writelines(lines[9:])
with open("AI.txt") as f:
  while True:
    c = f.read(1)
    count+=1
    if j>119:
        break
    elif c==' ' or c==',' or c=='\t' :
        pass
    elif i>159: # or c=='\n':
        j=j+1
        i=0
    elif c=='a' or c=='b':
        temp=c
    else:
        #print i
        Matrix[j][i]=temp+c
        i=i+1
        temp=""

def printMatrix(testMatrix):
        print '\t',
        for i in range(len(testMatrix[1])):
              print i,
        print
        for i, element in enumerate(testMatrix):
              print i, '\t'.join(element)


#scanning the matrix for different types of cells
def scanMatrix(testMatrix):
    #printMatrix(Matrix)
    for i in range(0,120):
        for j in range(0,160):
            if testMatrix[i][j]=='0':
                blocked.append((j,i))
            if testMatrix[i][j]=='a1'or testMatrix[i][j]=='a2'or testMatrix[i][j]=='a3'or testMatrix[i][j]=='a4':
                highway.append((j,i))
            if testMatrix[i][j]=='b1'or testMatrix[i][j]=='b2'or testMatrix[i][j]=='b3'or testMatrix[i][j]=='b4':
               hard_highway.append((j,i))
            if testMatrix[i][j]=='2':
               hard.append((j,i))
            if testMatrix[i][j]=='1':
               normal.append((j,i))

    #print tuple(highway)

scanMatrix(Matrix)
#print count
#printMatrix(Matrix)
#---------------------------------------------------------------------------------------------------
#print blocked
algo = input("Enter the Algo you want to use: \n1)Uniform Cost Search\n2)A*\n3)Weighted A*\n")
get_heu = input("Enter the heuristic you want to use: \n1)chebyshev\n2)Manhattan\n3)Euclidean\n4)Canberra\n5)manhattan/4\n")

start_time = time.time()

AStar_obj = AStar()
start_map = [int(start[0])-1,int(start[1])-1]
end_map = [int(end[0])-1,int(end[1])-1]
#walls_map = ((0, 5), (1, 0), (1, 1), (2, 3), (3, 1), (3, 2), (4, 4), (5, 1))
#hard_map = ((3, 5), (4, 1))
#highway_map = ((1, 5), (5,3))
#start_map = ((0,0))
#end_map = ((119,1))
AStar_obj.init_grid(160,120,blocked,start_map,end_map,get_heu,algo)
path_map, path_cost, nodes_expanded = AStar_obj.solve()

print("--- %s seconds ---" % (time.time() - start_time))



#visualization code

#drawing using tkinter

root= Tk()
x=0
y=0
w1=160
h1=120
h_max=h1*5
w_max=w1*5
w= Canvas(root, width=w_max , height=h_max)

message = StringVar()
cell_x, cell_y = 0,0
def onObjectClick(event):                  
    #print('Got object click', (event.x/5), (event.y/5))
    #print(event.widget.find_closest(event.x, event.y))
    cell_x, cell_y = event.x/5, event.y/5
    f,g,h = AStar_obj.get_fgh(cell_x,cell_y)
    ans = "("+str(cell_x+1)+","+str(cell_y+1)+")"+"\t"+"--->"+"\t"+"f="+str(f)+"\t"+"g="+str(g)+"\t"+"h="+str(h)
    message.set(ans)



for x in range(0,w_max,5):
    for y in range(0,h_max,5):
        if (x/5,y/5) in path_map:
            ##print x/5,y/5
            oid=w.create_rectangle(x, y, x+5, y+5, fill='blue')
            w.tag_bind(oid, '<ButtonPress-1>', onObjectClick)
        elif Matrix[y/5][x/5]=='1':
            oid=w.create_rectangle(x, y, x+5, y+5, fill='white')
            w.tag_bind(oid, '<ButtonPress-1>', onObjectClick)
        elif Matrix[y/5][x/5]=='0':
            oid=w.create_rectangle(x,y,x+5,y+5,fill='black')
        elif Matrix[y/5][x/5]=='2':
            oid=w.create_rectangle(x,y,x+5,y+5,fill='grey')
            w.tag_bind(oid, '<ButtonPress-1>', onObjectClick)
        elif Matrix[y/5][x/5]=='a1' or Matrix[y/5][x/5]=='a2' or Matrix[y/5][x/5]=='a3' or Matrix[y/5][x/5]=='a4':
            oid=w.create_rectangle(x,y,x+5,y+5,fill='green')
            w.tag_bind(oid, '<ButtonPress-1>', onObjectClick)
        elif Matrix[y/5][x/5]=='b1' or Matrix[y/5][x/5]=='b2' or Matrix[y/5][x/5]=='b3' or Matrix[y/5][x/5]=='b4':
            oid=w.create_rectangle(x,y,x+5,y+5,fill='dark green')
            w.tag_bind(oid, '<ButtonPress-1>', onObjectClick)
        else:
            oid=w.create_rectangle(x,y,x+5,y+5,fill='yellow')
            w.tag_bind(oid, '<ButtonPress-1>', onObjectClick)


        #w.create_rectangle(x, y, x+5, y+5, fill='white', outline= 'black', )
        #w.pack()

lal = Label(root, textvariable=message)

lal.pack()
#w.create_rectangle(x,y,x+5,y+5, fill='red', outline= 'black')
#w.tag_bind(oid, '<ButtonPress-1>', onObjectClick) 
w.pack()
root.mainloop()


print path_cost
print len(path_map)
print nodes_expanded
for i in path_map:
    print "("+str(i[0]+1)+","+str(i[1]+1)+")"

#Output the matrix to a file
orig_stdout = sys.stdout
f = file('final_path.txt', 'w')
sys.stdout = f

print path_cost
for i in path_map:
    print "("+str(i[0]+1)+","+str(i[1]+1)+")"
    

sys.stdout = orig_stdout
f.close()


