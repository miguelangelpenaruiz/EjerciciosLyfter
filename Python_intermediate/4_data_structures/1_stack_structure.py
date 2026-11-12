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
            return None
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

    print("--- Empty stack ---")
    my_stack.print_stack()
    print("pop:", my_stack.pop())

    print("--- Push 4 nodes ---")
    my_stack.push(Node("Hola"))
    my_stack.push(Node("Mundo"))
    my_stack.push(Node("third"))
    my_stack.push(Node("fourth"))
    my_stack.print_stack()

    print("--- Pop one ---")
    print("pop:", my_stack.pop())
    my_stack.print_stack()

    print("--- Pop until empty ---")
    print("pop:", my_stack.pop())
    print("pop:", my_stack.pop())
    print("pop:", my_stack.pop())
    print("pop:", my_stack.pop())  # aquí el stack ya está vacío
    my_stack.print_stack()

    print("--- Push after empty ---")
    my_stack.push(Node("new"))
    my_stack.print_stack()


