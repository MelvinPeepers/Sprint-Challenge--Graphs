from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.size > 0:
            return self.stack[len(self.stack)-1]
        else:
            print('Nothing to see here!')

    def size(self):
        return len(self.stack)


def dft(self, traversal_path):
    # Create a ss  LIFO
    plan_to_visit = Stack()
    # push starting room as you start in room 0
    plan_to_visit.push(0)
    # Create a set of traversed vertices
    visited_vertices = set()
    # while visited_vertices is less then the total number of rooms
    while len(visited_vertices) < len(room_graph):
        # current = to starting room
        current_vertex = plan_to_visit.stack[-1]
        # storage for rooms not visited
        unvisited_room = []
        # add the visited to stack
        visited_vertices.add(current_vertex)
        # get exits
        neighbor = room_graph[current_vertex][1]
        # loop through each heading, room of the items in neighbor return a list of tuple pairs
        for heading, room in neighbor.items():
            # if unvisited we don't want to revisit vertices that have already been checked
            if room not in visited_vertices:
                # add unvisited_rooms to visited
                unvisited_room.append((room, heading))

        # if unvisited room
        if len(unvisited_room) > 0:
            # add stack nested index
            plan_to_visit.push(unvisited_room[0][0])
            # add traversal_path nested index
            traversal_path.append(unvisited_room[0][1])

        else:
            # remove from stack
            plan_to_visit.pop()
            # loop through each heading, room of the items in neighbor return a list of tuple pairs
            for heading, room in neighbor.items():
                if room == plan_to_visit.stack[-1]:
                    # go to last room you were in
                    traversal_path.append(heading)

    # Create a ss
    # ss = Stack()
    # push starting room as you start in room 0
    # ss.push(0)
    # Create a set of traversed vertices
    # visited = set()
    # While queue is not empty:
    # while ss.size() > 0:
    #    path = ss.pop()
    #    # if not visited
    #    if room_id not in visited:
    #        # Do the Thing!!!
    #        print(path[-1])
    #        # mark as vsisitd
    #        visited.add(path[-1])
    #        # enqueue all neighbors
    #        not_visited = []
    #        for direction, room_id in neighbors.items():
    #            # if not visited
    #            if room_id not in visited:
    #                # add to visted stack
    #                not_visited.append((room_id, direction))


dft(0, traversal_path)


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


######
# UNCOMMENT TO WALK AROUND
######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
