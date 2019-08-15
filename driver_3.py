# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:28:18 2018
def bfs(initialState, goalTest)
    return success or failure:
        frontier = Queue.new(initialState) # frontier = Frontier(initialState)
        explored = Set.new() # explored = []
        while not frontier.isEmpty(): #while len(frontier) != 0
            state = frontier.dequeue()  # frontier.dequeue()
            explored.add(state) # explored.append(state)
            if goalTest(state): #
                return success(state)
            for neighbor in state.neighbors(): # for neighbor, mov in zip(state.neighbors(), state.moves())
                if neighbor not in frontier or explored:
                    frontier.enqueue(neighbor)
        return failure
            
@author: suser
"""
import argparse, time, sys
#from sys import getsizeof
from collections import deque
#start = time.clock()
#INSERT INTO SCRIPT TWO STRINGS IN COMMAND PROPMT 
parser = argparse.ArgumentParser()
parser.add_argument("algname", type=str, help="Algorithm name")
parser.add_argument("listnumbers", type=str, help="List of Numbers")
args = parser.parse_args()

class Frontier(object):
    def __init__(self, initial_state):
       self.initial_state = deque([initial_state])
       self.set_init_state = set()
       self.set_init_state.add(initial_state)
       self.manhattan_distance = [0]
       self.heap = [initial_state]
       self.goal =  "012345678"
       self.depths = [0]
       self.cost_path = 0
       self.max_depth = 0
       
       
       
      
    
    def isEmpty(self):
        if self.initial_state == deque():
            return True
        else:
            return False
    def deleteMin(self):
        index_del = self.manhattan_distance.index(min(self.manhattan_distance))
        self.manhattan_distance.pop(index_del)
        self.cost_path = self.depths.pop(index_del)
        if self.cost_path > self.max_depth:
            self.max_depth = self.cost_path
        self.set_init_state.remove(self.heap[index_del])
        #print(index_del, len(self.heap), self.manhattan_distance)
        #print(self.heap[index_del])
        #return [minimal, self.heap.pop(index_del)]
        return self.heap.pop(index_del)
    def inserting(self, neighbor):
        num_mis_tiles = 0 # number of misplaced tiles
        self.set_init_state.add(neighbor)
        distance = 0
        self.heap.append(neighbor)
        
        #print(self.heap)
        count = 0
        for number, goalstate in zip(neighbor, self.goal):
            if number != goalstate:
                #print(number)
                if number == "0":
                    num_mis_tiles -= 1
#                    if count in {1, 3}:
#                        distance += 1
#                    elif count in {2, 4, 6}:
#                        distance += 2
#                    elif count in {5, 7}:
#                        distance += 3
#                    else:
#                        distance += 4
                elif number == "1":
                    if count in {0, 2, 4}:
                        distance += 1
                    elif count in {3, 5, 7}:
                        distance += 2
                    else:
                        distance += 3
                elif number == "2":
                    if count in {1, 5}:
                        distance += 1
                    elif count in {0, 4, 8}:
                        distance += 2
                    elif count in {3, 7}:
                        distance += 3
                    else:
                        distance += 4           
                elif number == "3":
                    if count in {0, 4, 6}:
                        distance += 1
                    elif count in {1, 5, 7}:
                        distance += 2
                    else:
                        distance += 3
                elif number == "4":
                    if count in {1, 3, 5, 7}:
                        distance += 1
                    else:
                        distance += 2
                elif number == "5":
                    if count in {2, 4, 8}:
                        distance += 1
                    elif count in {1, 3, 7}:
                        distance += 2
                    else:
                        distance += 3
                elif number == "6":
                    if count in {3, 7}:
                        distance += 1
                    elif count in {0, 4, 8}:
                        distance += 2
                    elif count in {1, 5}:
                        distance += 3
                    else:
                        distance += 4
                elif number == "7":
                    if count in {4, 6, 8}:
                        distance += 1
                    elif count in {1, 3, 5}:
                        distance += 2
                    else:
                        distance += 3                    
                elif number == "8":
                    if count in {5, 7}:
                        distance += 1
                    elif count in {2, 4, 6}:
                        distance += 2
                    elif count in {1, 3}:
                        distance += 3
                    else:
                        distance += 4
                num_mis_tiles += 1
            count+=1
        to_distance = distance + num_mis_tiles
        self.manhattan_distance.append(to_distance + self.cost_path)
        self.depths.append(self.cost_path + 1)
        #print("manhattan distance of neighbor " + neighbor + "  " + str(distance) + " " + str(num_mis_tiles-1))
        
        
        
        
            
    def dequeue(self):
        ext = self.initial_state.popleft()
        self.set_init_state.remove(ext)
        return ext

    def enqueue(self, neighbor):
        self.set_init_state.add(neighbor)
        self.initial_state.append(neighbor)
    
    def stack_pop(self):
        last = self.initial_state.pop()
        self.set_init_state.remove(last)
        return last
    def neighbors(self, state):
        mov = self.moves(state)
        all_neighbors = []
        child = state[:]
        zero_ind = state.index("0")
        for move in mov:
            #child = state[:]
            if zero_ind == 0:
                if move == "Down":
#                    child[0] = child[3]
#                    child[3] = 
                    chil = child[:3].replace(child[0], child[3]) + child[3:].replace(child[3], "0")
                    #print(state, move, child)
                if move == "Right":
#                    child[0] = child[1]
#                    child[1] = 0
                    chil = child[:1].replace(child[0], child[1]) + child[1:].replace(child[1], "0")
                    #print(state, move, child)
            elif zero_ind == 1:
                if move == "Down":
#                    child[1] = child[4]
#                    child[4] = 0
                    chil = child[:4].replace(child[1], child[4]) + child[4:].replace(child[4], "0")
                if move == "Left":
#                    child[1] = child[0]
#                    child[0] = 0
                    chil = child[:1].replace(child[0], "0") + child[1:].replace(child[1], child[0])
                if move == "Right":
#                    child[1] = child[2]
#                    child[2] = 0
                    chil = child[:2].replace(child[1], child[2]) + child[2:].replace(child[2], "0")
                    
            elif zero_ind == 2:
                if move == "Down":
#                    child[2] = child[5]
#                    child[5] = 0
                    chil = child[:5].replace(child[2], child[5]) + child[5:].replace(child[5], "0")
                    #print(state, move, child)
                if move == "Left":
                     #child[1] = 0
#                    child[2] = child[1]
                    chil = child[:2].replace(child[1], "0") + child[2:].replace(child[2], child[1])
            elif zero_ind == 3:
                if move == "Up":
#                    child[3] = child[0]
#                    child[0] = 0
                    chil = child[:3].replace(child[0], "0") + child[3:].replace(child[3], child[0])
                if move == "Down":
#                    child[3] = child[6]
#                    child[6] = 0
                    chil = child[:6].replace(child[3], child[6]) + child[6:].replace(child[6], "0")
                if move == "Right":
#                    child[3] = child[4]
#                    child[4] = 0
                    chil = child[:4].replace(child[3], child[4]) + child[4:].replace(child[4], "0")
                    
            elif zero_ind == 4:
                if move == "Up":
#                    child[4] = child[1]
#                    child[1] = 0
                    chil = child[:4].replace(child[1], "0") + child[4:].replace(child[4], child[1])
                    
                if move == "Down":
#                    child[4] = child[7]
#                    child[7] = 0
                    chil = child[:7].replace(child[4], child[7]) + child[7:].replace(child[7], "0")
                if move == "Left":
#                    child[4] = child[3]
#                    child[3] = 0
                    chil = child[:4].replace(child[3], "0") + child[4:].replace(child[4], child[3])
                if move == "Right":
#                    child[4] = child[5]
#                    child[5] = 0
                    chil = child[:5].replace(child[4], child[5]) + child[5:].replace(child[5], "0")
            elif zero_ind == 5:
                if move == "Up":
#                    child[5] = child[2]
#                    child[2] = 0
                    chil = child[:5].replace(child[2], "0") + child[5:].replace(child[5], child[2])
                if move == "Down":
#                    child[5] = child[8]
#                    child[8] = 0
                    chil = child[:8].replace(child[5], child[8]) + child[8:].replace(child[8], "0")
                if move == "Left":
#                    child[5] = child[4]
#                    child[4] = 0
                    chil = child[:5].replace(child[4], "0") + child[5:].replace(child[5], child[4])
            elif zero_ind == 6:
                if move == "Up":
#                    child[6] = child[3]
#                    child[3] = 0
                    chil = child[:6].replace(child[3], "0") + child[6:].replace(child[6], child[3])
                if move == "Right":
#                    child[6] = child[7]
#                    child[7] = 0
                    chil = child[:7].replace(child[6], child[7]) + child[7:].replace(child[7], "0")
            elif zero_ind == 7:
                if move == "Up":
#                    child[7] = child[4]
#                    child[4] = 0
                    chil = child[:7].replace(child[4], "0") + child[7:].replace(child[7], child[4])
                if move == "Left":
#                    child[7] = child[6]
#                    child[6] = 0
                    chil = child[:7].replace(child[6], "0") + child[7:].replace(child[7], child[6])
                if move == "Right":
#                    child[7] = child[8]
#                    child[8] = 0
                    chil = child[:8].replace(child[7], child[8]) + child[8:].replace(child[8], "0")
            elif zero_ind == 8:
                if move == "Up":
#                    child[8] = child[5]
#                    child[5] = 0
                    chil = child[:8].replace(child[5], "0") + child[8:].replace(child[8], child[5])
                if move == "Left":
#                    child[8] = child[7]
#                    child[7] = 0
                    chil = child[:8].replace(child[7], "0") + child[8:].replace(child[8], child[7])
            all_neighbors.append(chil)
        return all_neighbors
            
    def moves(self, state):
        pos = state.index("0")
        #in_nodes = self.mov_tile(parent, move)
        if pos == 0:
            #p_mov = ("Down", "Right")
            return ("Down", "Right")     
        elif pos == 1:
            #p_mov = ("Down", "Left", "Right")
            return ("Down", "Left", "Right")
        elif pos == 2:
            #p_mov = ("Down", "Left")
            return ("Down", "Left")
        elif pos == 3:
            #p_mov = ("Up", "Down", "Right")
            return ("Up", "Down", "Right")
        elif pos == 5:
            #p_mov = ("Up", "Down", "Left")
            return ("Up", "Down", "Left")
        elif pos == 6:
            #p_mov = ("Up", "Right")
            return ("Up", "Right")
        elif pos == 7:
            #p_mov = ("Up", "Left", "Right")
            return ("Up", "Left", "Right")
        elif pos == 8:
            #p_mov = ("Up", "Left")
            return ("Up", "Left")
        else:
            #p_mov = ("Up", "Down", "Left", "Right")
            return ("Up", "Down", "Left", "Right")
            
        
        
#print(Frontier([3,1,2,0,4,5,6,7,8]).neighbors([3,1,2,0,4,5,6,7,8]))
#class Path(object):
#    def __init__(self, initialize):
#        self.queue = initialize
#    def dequeue(self):
#        return self.queue.pop(0)
#    def enqueue(self, moving):
#        self.queue.append(moving)
        
class puzzlegame(object):
#def bfs(initialState, goalTest)
#    return success or failure:
#        frontier = Queue.new(initialState) # frontier = Frontier(initialState)
#        explored = Set.new() # explored = []
#        while not frontier.isEmpty(): #while len(frontier) != 0
#            state = frontier.dequeue()  # frontier.dequeue()
#            explored.add(state) # explored.append(state)
#            if goalTest(state): #
#                return success(state)
#            for neighbor in state.neighbors(): # for neighbor, mov in zip(state.neighbors(), state.moves())
#                if neighbor not in frontier or explored:
#                    frontier.enqueue(neighbor)
#        return failure
    def __init__(self, algoname, valuelist):
        self.start = time.clock()
        self.tree = dict()
        self.paths = {}
        self.paths["Up"] = set()
        self.paths["Down"] = set()
        self.paths["Right"] = set()
        self.paths["Left"] = set()
        
        #self.i_state = []
        #self.initial_state = valuelist.split(",")
        self.initial_state = valuelist.replace(",", "")
        #for value in self.initial_state:
            #self.i_state.append(int(value))
        self.queue = deque()
        self.algorithm_name = algoname
        self.path = deque()
        self.running_time = ""
        self.explored = set()
        self.goal_state =  "012345678"
        self.node = 0
        self.path_to_goal = []
        self.dec_path = ""
        self.max_ram_usage = 0
        self.max_search_depth = 0

        if sys.platform == "win32":
            import psutil
            self.max_ram_usage = psutil.Process().memory_info().rss
        else:
    # Note: if you execute Python from cygwin,
    # the sys.platform is "cygwin"
    # the grading system's sys.platform is "linux2"
            import resource
            self.max_ram_usage= resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        self.decision()
        
    def decision(self):
        if self.algorithm_name == "bfs":
            self.bfs_alg()
            #print(self.algorithm_name, self.initial_state)
        elif self.algorithm_name == "dfs":
            self.dfs_alg()
            #print(self.algorithm_name, self.initial_state)
        elif self.algorithm_name == "ast":
            self.ast_alg()
            #print(self.algorithm_name, self.initial_state)  
        else:
            print("This Algorithm not implemented yet")
    def bfs_alg(self):
        #python driver_2.py bfs 8,6,4,2,1,3,5,7,0 running_time: 53.22827783, improved 26,44
        frontier = Frontier(self.initial_state)
        path = deque([""])

#        tree = dict()#        final_path = deque()
        kos = []
        while not frontier.isEmpty():
            
            state = frontier.dequeue()
            queue = path.popleft()

                #print(len(self.explored), len(path), len(queue))
            self.explored.add(state)

            if self.goal_test(state):
                #print(time.time() - start)
                self.path_to_goal += queue.split(",")
                #print(len(path[-1].split(",")), len(self.path_to_goal))
                if len(path[-1].split(",")) > len(self.path_to_goal):
                    self.max_search_depth += len(path[-1].split(","))
                else:
                    self.max_search_depth += len(self.path_to_goal)
                    
                #print(self.path_to_goal)
                #self.max_search_depth += len(self.path_to_goal) + 1
                #self.max_ram_usage = psutil.Process().memory_info().rss/1000000
                return self.success()
           
            for neighbor, mov in zip(frontier.neighbors(state), frontier.moves(state)):
                if neighbor not in frontier.set_init_state and neighbor not in self.explored:
                    frontier.enqueue(neighbor)
                    if path != deque():
                        path.append(queue + "," + mov)

                    if self.node == 0:
                        kos.append(mov)

            if self.node == 0:                
                path.extend(kos)
            self.node += 1
            

        return "Failure"
    def dfs_alg(self):
        """function Depth-First-Search(initialState, goalTest) returns SUCCESS OR FAILURE
        frontier = Stack.new(initialState)
        explored = Set.new()
        while not frontier.isEmpty():
            state = frontier.pop()
            explored.add(state)
            
            if goalTest(state):
                return Success(state)
            for neighbor in state.neighbors():
                if neighbor not in frontier and neighbor not in explored:
                    frontier.push(neighbor)
        return Failure"""
        #python driver.py dfs 1,2,5,3,4,0,6,7,8
        frontier = Frontier(self.initial_state)

        lengths = deque()
        lengths.append(0)

        no_neighbors = False

        while not frontier.isEmpty():
            state = frontier.stack_pop()
            length = lengths.pop()
            if self.queue != deque():
                self.dec_path+=(self.queue.pop()[0])

            self.explored.add(state)
            
            if self.goal_test(state):
                if self.max_search_depth < length:
                    self.max_search_depth = length

                #self.max_ram_usage = psutil.Process().memory_info().rss/1000000
#                print(self.tree, len(self.path_to_goal), self.runtime(), len(self.explored)-1, self.max_ram_usage)
                #return None
                final = deque()
                decode = {"L":"Left", "R":"Right", "U":"Up", "D":"Down"}
                for item in self.dec_path:
                    final.append(decode[item])
                self.path_to_goal = list(final)
                return self.success()

            no_neighbors = True
            for neighbor, mov in zip(reversed(frontier.neighbors(state)), reversed(frontier.moves(state))):
                if neighbor not in frontier.set_init_state and neighbor not in self.explored:
                    frontier.enqueue(neighbor)
                    self.queue.append(mov)
                    lengths.append(length + 1)
                    no_neighbors = False
                        
                        
            if no_neighbors:
                if self.max_search_depth < length:
                    self.max_search_depth = length
                self.dec_path = self.dec_path[:lengths[-1]-1]

        return "Failure"
    def ast_alg(self):
        """function A-star-search(initialState, goalTest)
        returns SUCCESS OR FAILURE  Cost f(n) = g(n) + h(n)
        
        frontier = Heap.new(initialState)
        explored = Set.new()
        
        while not frontier.isEmpty():
            state = frontier.deleteMin()
            explored.add(state)
            if goalTest(state):
                return SUCCESS(state)
            for neighbor in state.neighbors():
                if neighbor not in frontier an neighbor not in explored:
                    frontier.insert(neighbor)
                else if neighbor in frontier:
                    frontier.decreaseKey(neighbor)
        return Failure
        h1(n) = number of misplaces tiles
        h2(n) = total manhattan distance
                """
        lengths = []
        lengths.append(0)
        all_nodes = {}
        frontier = Frontier(self.initial_state)
#        print(frontier.heap)
        
        while not frontier.heap == []:            
            state = frontier.deleteMin()
            #g_n = state[0]
            #print(len(self.explored))
#            print(frontier.neighbors(state), frontier.moves(state))
#            print(state)
            self.explored.add(state)
            if self.goal_test(state):
#                print(len(self.explored))
                #print(len(self.explored))
                self.path = [state]
                while self.path[-1] != self.initial_state:
                    for key, neighbors in all_nodes.items():
                        if self.path[-1] in neighbors:
                            self.path.append(key)
            #                    self.goal(self.path[-1])
                            break
                for item in reversed(self.path):
                    if item in self.paths["Up"]:
                        self.path_to_goal.append("Up")
                    elif item in self.paths["Down"]:
                        self.path_to_goal.append("Down")
                    elif item in self.paths["Right"]:
                        self.path_to_goal.append("Right")
                    elif item in self.paths["Left"]:
                        self.path_to_goal.append("Left")
                #print(self.path, len(self.path_to_goal), self.path_to_goal)
                self.max_search_depth = frontier.max_depth
                #self.max_ram_usage = psutil.Process().memory_info().rss/1000000
                return self.success()
#                return self.success()
            all_nodes[state] = set()
            for neighbor, mov in zip(frontier.neighbors(state), frontier.moves(state)):
                if neighbor not in frontier.set_init_state and neighbor not in self.explored:
#                    print(neighbor, mov)
                    frontier.inserting(neighbor)
                    #print()
                    self.paths[mov].add(neighbor)
                    all_nodes[state].add(neighbor)
#                elif neighbor in frontier.set_init_state:
#                    frontier.decreaseKey(neighbor)
#            print(self.node)
#            if self.node == 2:
#                break
            if all_nodes[state] == set():
                del all_nodes[state]
            #print(frontier.heap)
            #print(self.node)
#            self.node += 1
        return "Failure"
                
        pass
        
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        else:
            return False
#    def goal(self, path):
##        while path != self.initial_state:
#        for key, neighbors in self.tree.items():
#            if path in neighbors:
#                self.path.append(key)
##                    self.goal(self.path[-1])
#                break
#        return None
        
            
            
        
    def success(self):
        to_file = open("output.txt", "w")
        to_file.write("path_to_goal: " + str(self.path_to_goal) +"\n")
        to_file.write("cost_of_path: " + str(len(self.path_to_goal)) + "\n")
        to_file.write("nodes_expanded: "+ str(len(self.explored) - 1) + "\n")
        to_file.write("search_depth: " + str(len(self.path_to_goal)) + "\n")
        to_file.write("max_search_depth: " + str(self.max_search_depth) + "\n")
        to_file.write("running_time: " + self.runtime() + "\n")
        to_file.write("max_ram_usage: " + str(self.max_ram_usage) + "\n")
        to_file.close()
    
    def runtime(self):
        self.running_time += str(round(time.clock() - self.start, 8))
        return self.running_time
        
    
    def write_to_file(self):
        to_file = open("output.txt", "w")
        to_file.write("path_to_goal: " + str(self.path_to_goal) +"\n")
        to_file.write("cost_of_path: " + str(len(self.path_to_goal)) + "\n")
        to_file.write("nodes_expanded: "+ str(len(self.explored) - 1) + "\n")
        to_file.write("search_depth: " + str(len(self.path_to_goal)) + "\n")
        to_file.write("max_search_depth: " + str(self.max_search_depth) + "\n")
        to_file.write("running_time: " + self.runtime() + "\n")
        to_file.write("max_ram_usage: " + str(self.max_ram_usage) + "\n")
        to_file.close()

puzzlegame(args.algname, args.listnumbers)


    
        