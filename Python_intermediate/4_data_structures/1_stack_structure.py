class Node:
    under: "Node"
    

    def __init__(self, data, under=None):
        self.data = data
        self.under = under

class Stack:
    top: Node

    def __init__(self):
        self.top = None

    def push(self, new_node):
        current_node = self.top
        self.top = new_node
        new_node.under = current_node

    def pop(self):
        if self.top is None:
            print("Stack empty, there is nothing to pop")
            return
        current_node = self.top
        self.top = current_node.under
        return current_node.data

        

    def print_stack(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.under

if __name__ == "__main__":
    my_stack = Stack()
    first_node = Node("Hola")
    my_stack.push(first_node)

    second_node = Node("Mundo")
    my_stack.push(second_node)

    third_node = Node("third")
    my_stack.push(third_node)

    forth = Node("forth")
    my_stack.push(forth)

    my_stack.print_stack()

    my_stack.pop()

    print("-------------")

    my_stack.print_stack()

    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()

    print("-------------")

    my_stack.print_stack()


