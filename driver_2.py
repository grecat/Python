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
import argparse, time, psutil
from sys import getsizeof
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
      
    
    def isEmpty(self):
        if self.initial_state == deque():
            return True
        else:
            return False
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
            p_mov = ("Down", "Right")
                    
        elif pos == 1:
            p_mov = ("Down", "Left", "Right")
           
        elif pos == 2:
            p_mov = ("Down", "Left")
           
        elif pos == 3:
            p_mov = ("Up", "Down", "Right")
            
        elif pos == 5:
            p_mov = ("Up", "Down", "Left")
            
        elif pos == 6:
            p_mov = ("Up", "Right")
           
        elif pos == 7:
            p_mov = ("Up", "Left", "Right")
           
        elif pos == 8:
            p_mov = ("Up", "Left")
           
        else:
            p_mov = ("Up", "Down", "Left", "Right")
            
        return p_mov
        
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
        self.algorithm_name = algoname
        self.path = deque()
        self.running_time = ""
        self.explored = set()
        self.goal_state =  "012345678"
        self.node = 0
        self.path_to_goal = []
        self.max_ram_usage = 0
        self.max_search_depth = 0
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
        path = deque()

#        tree = dict()#        final_path = deque()
        kos = []
        while not frontier.isEmpty():
            
            state = frontier.dequeue()
            if len(path) > 0:
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
                self.max_ram_usage = psutil.Process().memory_info().rss/1000000
                return self.success(state)
           
            for neighbor, mov in zip(frontier.neighbors(state), frontier.moves(state)):
                if neighbor not in frontier.set_init_state and neighbor not in self.explored:
                    frontier.enqueue(neighbor)

                    if len(path) > 0:
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
#        path = deque()
#        to_goal = deque()
#        nodes = deque()
#        final_path = deque()
        lengths = deque()
        lengths.append(0)
#        max_len = 0
	
        
        kos = []
        queue = ""
#        path_g = []
#        new_set = set()
        while not frontier.isEmpty():
            state = frontier.stack_pop()
            length = lengths.pop()
            self.tree[state] = set()
#            if len(path) > 0:
#                queue = path.pop()
#                final_path.append(queue)
#                
                #print(queue)
#                to_goal.append(queue)
                
                
#                
#                print(getsizeof(path))
                #new_set.remove(queue)
#                if self.node < 180002:
#                    print(len(self.explored), getsizeof(path))
#                    if self.node == 180000:
#                        print(len(self.explored), len(path), len(queue),getsizeof(path))
#                        #, queue, path, 
#                        return None
            self.explored.add(state)
            
#            if len(self.explored) - 1 == 51015:
#                print(state)
#                return None
            if self.goal_test(state):
                if self.max_search_depth < length:
                    self.max_search_depth = length
                #print(max_len)
#                self.path_to_goal += queue.split(",")
#                self.max_search_depth += len(self.path_to_goal)
                #queue.split(","), 
                self.max_ram_usage = psutil.Process().memory_info().rss/1000000
#                print(self.tree, len(self.path_to_goal), self.runtime(), len(self.explored)-1, self.max_ram_usage)
                #return None
                return self.success(state)
                #print(len(self.explored)-1)
                #return self.success(state)
            #no_path = 0
            
#            tree_nodes = set()
            
            #print(frontier.neighbors(state), state)
            for neighbor, mov in zip(reversed(frontier.neighbors(state)), reversed(frontier.moves(state))):
                if neighbor not in frontier.set_init_state and neighbor not in self.explored:
                    frontier.enqueue(neighbor)
                    self.tree[state].add(neighbor)
                    self.paths[mov].add(neighbor)
                    lengths.append(length + 1)
                        
                        
            if self.tree[state] == set():
                if self.max_search_depth < length:
                    self.max_search_depth = length
#                self.path = deque([state])
#                while self.path[-1] != self.initial_state:
#                    self.goal(self.path[-1])
#                print(len(self.path))
#                if len(self.path) > self.max_search_depth:
#                    self.max_search_depth = len(self.path)
                del self.tree[state]
#                    tree_nodes.add(mov)
#                    #path.append(mov)
#                    #print(neighbor)
#                    if len(path) > 0:
#                        path.append(mov)
#
#                    if self.node == 0:
#                        kos.append(mov)
#            if tree_nodes == {}:
#                tree[self.node-1].remove(queue)
#                final_path.pop()
#                x = 1
##                if len(tree[self.node-1]) > 0:
##                    while len(tree[self.node - x]) <= 1:
#                        
#                        
#            print(tree_nodes)              
#            else:
#            if tree_nodes != set():            
#                tree[self.node]=tree_nodes
#
#            if self.node == 0:                
#                path.extend(kos)
#
#
#            self.node += 1
        return "Failure"
    def ast_alg(self):
        pass
        
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        else:
            return False
    def goal(self, path):
#        while path != self.initial_state:
        for key, neighbors in self.tree.items():
            if path in neighbors:
                self.path.append(key)
                del self.tree[key]
#                    self.goal(self.path[-1])
                break
#        return None
        
            
            
        
    def success(self, state):
        self.path = deque([state])
        #self.path.append(state)
#        count = 0
        while self.path[-1] != self.initial_state:
#            count+=1
#            print(count)
            self.goal(self.path[-1])
#        self.goal(self.path[-1])
        while len(self.path) > 0:
            last = self.path.pop()
            if last in self.paths["Left"]:
                self.path_to_goal.append("Left")
            if last in self.paths["Right"]:
                self.path_to_goal.append("Right")
            if last in self.paths["Up"]:
                self.path_to_goal.append("Up")
            if last in self.paths["Down"]:
                self.path_to_goal.append("Down")
#        print(self.path, self.path_to_goal)
        print(self.path_to_goal[-4:])
        return self.write_to_file()
    
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


    
        