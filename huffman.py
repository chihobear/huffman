import sys
class Node:
    def __init__(self, value):
        """Iniate class 'Node' by setting 'self._value' to 'value'
                                  setting 'self._lc' to None
                                  setting 'self._rc' to None
        """
        self._value = value
        self._lc = None
        self._rc = None

    def __str__(self):
        """Print out this tree"""
        val = self._value
        Tleft = self._lc
        Tright = self._rc
        return "({} {} {})".format( val, str(Tleft), str(Tright))
        if self._lc == None:
            return "None"
        elif self._rc == None:
            return "None"

def build_tree(preorder, inorder):
    """Create the tree by 'preorder' and 'inorder' using recursion
       Parameters: 'preorder' is a list, 'inorder' is a list
    """
    if preorder == []:
        return None
    elif len(preorder) == 1:
        node = Node(preorder[0]) 
        return node
    else:
        T = Node(preorder[0])
        #find the position of root in inorder sequence
        node_pos = inorder.index(preorder[0])
        #if left child is empty
        if node_pos == 0:
            T._lc = build_tree([], [])
            T._rc = build_tree(preorder[1:], inorder[1:])
        else:
            #find the position of last node of left tree in preorder sequence
            position = -1
            for i in inorder[:node_pos]:
                if position < preorder.index(i):
                    position = preorder.index(i)
            #position = preorder.index(inorder[node_pos - 1])
            T._lc = build_tree(preorder[1:position + 1], inorder[:node_pos])
            T._rc = build_tree(preorder[position + 1:], inorder[node_pos + 1:])
        return T

def postorder(T, root):
    """Print out the postorder sequence of this tree
       Parameters: 'T' is the first node of the tree
                   'root' is the fist node of the tree used to judge the root, constant
    """
    if T == None:
        return
    else:
        postorder(T._lc, root)
        postorder(T._rc, root)
        if T != root:
            print(T._value, end=' ')
        else:
            print(T._value, end='')

def translate(T, string):
    """Translate huffman code to real elements in the tree using loop
       Parameters: 'string' is a string
    """
    list = []
    node = T
    for i in string:
        if i == '0' and node._lc != None:
            #go left
            node = node._lc
            if node._lc == None and node._rc == None:
                #reach the leaf node
                list.append(node._value)
                node = T
        #if the sequence is not llegal, ignore it and put 'node' back to root
        elif i == '0' and node._lc == None:
            node = T
        elif i == '1' and node._rc != None:
            #go right
            node = node._rc
            if node._lc == None and node._rc == None:
                #reach the leaf node
                list.append(node._value)
                node = T
        #if the sequence is not llegal, ignore it and put 'node' back to root
        elif i == '1' and node._rc == None:
            node = T
    return list

def main():
    filename = input('Input file: ')
    try:
        file = open(filename)
    except IOError:
        print('ERROR: Could not open file ' + filename)
        exit(1)
    n = 0
    for line in file:
        if n == 0:
            preorder_list = line.split()
        elif n == 1:
            inorder_list = line.split()
        elif n == 2:
            string = line.strip()
        n += 1
    file.close()
    tree = build_tree(preorder_list, inorder_list)
    root = tree
    postorder(tree, root)
    print('')
    for i in translate(tree, string):
        print(i, end='')
    print('')

main()



        
    
