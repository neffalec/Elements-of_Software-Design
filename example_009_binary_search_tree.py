class Node():
    '''This class represents a single Node.'''

    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):
        if self.rChild != None:
            self.rChild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.data)

        if self.lChild != None:
            self.lChild.print_node(level + 1)
    
      # In-order traversal - left, center, right
    def inOrder(self, aNode):
        if (aNode != None):
            aNode.inOrder(aNode.lChild)
            print(aNode.data, end=" ")
            aNode.inOrder(aNode.rChild)

    # Pre-order traversal - center, left, right
    def preOrder(self, aNode):
        if (aNode != None):
            print(aNode.data, end=" ")
            aNode.preOrder(aNode.lChild)
            aNode.preOrder(aNode.rChild)

    # Post-order traversal - left, right, center
    def postOrder(self, aNode):
        if (aNode != None):
            aNode.postOrder(aNode.lChild)
            aNode.postOrder(aNode.rChild)
            print(aNode.data, end=" ")
            
    def bst_size(self, node):
        if node == None:
            return 0
        else:
            return 1 + self.bst_size(node.rChild) + self.bst_size(node.lChild)

class BST():
    '''This class represents a Binary Search Tree.'''

    def __init__(self):
        self.root = None

    def sort(self):
        sorted_list = []
        self.in_order_traversal(self.root, sorted_list)
        return sorted_list
    
    def in_order_traversal(self, node, sorted_list):
        if node:
            self.in_order_traversal(node.lChild,sorted_list)
            sorted_list.append(node.data)
            self.in_order_traversal(node.rChild,sorted_list)

    def bst_median(self):
        median = None
        sorted_elements = self.sort()
        length = len(sorted_elements)
        if length % 2 == 0:
            med1 = sorted_elements[length//2 + 1]
            med2 = sorted_elements[length//2 - 1]
            median = (med1 + med2) // 2
        else:
            median_index = length // 2
            median = sorted_elements[median_index]
        return median

    def height(self) -> int:
        return self.calc_height(self.root)

    def calc_height(self, node):
        if node == None:
            return 0
        else:
            l_height = self.calc_height(node.lChild)
            r_height = self.calc_height(node.rChild)
            return 1 + max(l_height, r_height)

    def is_balanced(self):
        return self.balanced(self.root)

    def balanced(self, node):
        if node == None:
            return False
        else:
            l_height = self.calc_height(node.lChild)
            r_height = self.calc_height(node.rChild)
            if l_height == r_height:
                return True
            else:
                return False

    def print(self, level):
        self.root.print_node(level)

    # Search for a node with the key
    def search(self, key):
        current = self.root
        while ((current != None) and (current.data != key)):
            if (key < current.data):
                current = current.lChild
            else:
                current = current.rChild
        return current

    # Insert a node in the tree
    def insert(self, val):
        newNode = Node(val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
# seearch 
            while (current != None):
                parent = current
                if (val < current.data):
                    current = current.lChild
                else:
                    current = current.rChild
# insert 
            if (val < parent.data):
                parent.lChild = newNode
            else:
                parent.rChild = newNode


    # Find the node with the smallest value
    def minimum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.lChild
        return parent

    # Find the node with the largest value
    def maximum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.rChild
        return parent

    # Delete a node with a given key
    def delete(self, key):
        deleteNode = self.root
        parent = self.root
        isLeft = False

        # If empty tree
        if (deleteNode == None):
            return False

        # Find the delete node
        while ((deleteNode != None) and (deleteNode.data != key)):
            parent = deleteNode
            if (key < deleteNode.data):
                deleteNode = deleteNode.lChild
                isLeft = True
            else:
                deleteNode = deleteNode.rChild
                isLeft = False

        # If node not found
        if (deleteNode == None):
            return False

        # Delete node is a leaf node
        if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
            if (deleteNode == self.root):
                self.root = None
            elif (isLeft):
                parent.lChild = None
            else:
                parent.rChild = None

        # Delete node is a node with only left child
        elif (deleteNode.rChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.lChild
            elif (isLeft):
                parent.lChild = deleteNode.lChild
            else:
                parent.rChild = deleteNode.lChild

        # Delete node is a node with only right child
        elif (deleteNode.lChild == None):
            if (deleteNode == self.root):
                self.root = deleteNode.rChild
            elif (isLeft):
                parent.lChild = deleteNode.rChild
            else:
                parent.rChild = deleteNode.rChild

        # Delete node is a node with both left and right child
        else:
            # Find delete node's successor and successor's parent nodes
            successor = deleteNode.rChild
            successorParent = deleteNode

            while (successor.lChild != None):
                successorParent = successor

                successor = successor.lChild

            # Successor node right child of delete node
            if (deleteNode == self.root):
                self.root = successor
            elif (isLeft):
                parent.lChild = successor
            else:
                parent.rChild = successor

            # Connect delete node's left child to be successor's left child
            successor.lChild = deleteNode.lChild

            # Successor node left descendant of delete node
            if (successor != deleteNode.rChild):
                successorParent.lChild = successor.rChild

                successor.rChild = deleteNode.rChild

        return True

###############################
#                             #
#   Example run of a BST run  #
#                             #
###############################

def main():
    bst = BST()

    bst.insert(10)
    bst.insert(40)
    bst.insert(5)
    bst.insert(15)
    bst.insert(22)
    bst.insert(4)

    sorted_elements = bst.sort()
    bst.bst_median()
    print("sorted elements of the BST:", sorted_elements)

    bst.print(2)
    print("##############")
    bst.print(2)
    print("##############")

    print("Print In-Order")
    bst.root.inOrder(bst.root)

    print()
    print("Print Pre-Order")
    bst.root.preOrder(bst.root)

    print()
    print("Print Post-Order")
    bst.root.postOrder(bst.root)
    
    print()
    size = bst.root.bst_size(bst.root)
    print('Size of the BST:', size)
    
    print()
    sorted_elements = bst.sort()
    print('Sorted elements of the BST:', sorted_elements)
    
    print()
    median = bst.bst_median()
    print('The median is:', median)
    
    print()
    height = bst.height()
    print('Height of the BST:', height)
    
    print()
    is_balanced = bst.is_balanced()
    if is_balanced:
        print('The BST is balanced.')
    else:
        print('The BST is not balanced.')

if __name__ == '__main__':
    main()
