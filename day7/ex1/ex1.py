import re

# read input

INPUT_PATH = './day7/input.txt'

with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()
    # remove line endings
    lines = [line[:-1] for line in lines]

# solution

MAX_SIZE = 100000


valid_folders = set()

class TreeNode:

    def __init__(self, parent = None):
        self.parent = parent
        self.subfolders = {}
        self.files = set()
        self.space_taken = 0
        valid_folders.add(self)

    def create_subfolder_if_not_exists(self, name):
        if name not in self.subfolders:
            self.subfolders[name] = TreeNode(self)
        
        return self.subfolders[name]
    
    def add_file(self, name, space_taken):
        # ls may be run more than once on the same dir
        if name in self.files:
            return
        
        self.files.add(name)
        self.increment_space_taken(space_taken)

        curr = self.parent
        
        while curr is not None:
            curr.increment_space_taken(space_taken)

            curr = curr.parent


    def increment_space_taken(self, amount):
        self.space_taken += amount

    def get_root(self):
        curr = self
        
        while curr.parent is not None:
            curr = curr.parent
        
        return curr
    
    
    def print(self, path = '/', depth = 0):
        prefix = '.' * depth

        print(prefix + path)
        print(prefix + str(list(self.subfolders.keys())))
        print(prefix + str(self.files))
        print(prefix + str(self.space_taken))

        for k, v in self.subfolders.items():
           v.print(path + k + '/', depth + 1)




# ignore last empty line
lines = lines[:-1]

current_node = TreeNode()
ls_mode = False
for line in lines:

    #current_node.get_root().print()
    #print('#################################')

    tokens = line.split(' ')

    if ls_mode:
        # end file size parse(this will propagate below and get parsed as a command)
        if tokens[0] == '$':
            ls_mode = False
        
        # file
        elif tokens[0] != 'dir':
            current_node.add_file(tokens[1], int(tokens[0]))
            continue

    # command
    if tokens[0] == '$':
        if tokens[1] == 'ls':
            ls_mode = True
            continue
        elif tokens[1] == 'cd':
            path = tokens[2]

            if path.startswith('/'):
                current_node = current_node.get_root()
                path = path[1:]
                
                if not path:
                    continue
            
            path_parts = path.split('/')

            for path_part in path_parts:
                if path_part == '.':
                    continue
                elif path_part == '..':
                    current_node = current_node.parent
                else:
                    current_node = current_node.create_subfolder_if_not_exists(path_part)

print(sum([folder.space_taken for folder in valid_folders if folder.space_taken <= MAX_SIZE]))

