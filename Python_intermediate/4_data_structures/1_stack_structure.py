class Node:
    under: "Node"
    

    def __init__(self, data, under= None):
        self.data = data
        self.under = under

class Stack:
    top: Node

    def __init__(self, top):
        self.top = top

    def push(self, new_node):
        current_node = self.top
        self.top = new_node
        new_node.under = current_node

    def pop(self):
        current_node = self.top

        if current_node.under:
            self.top = current_node.under
        elif current_node:
            current_node.data = None
        

    def print_stack(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.under

if __name__ == "__main__":
    first_node = Node("Hola")
    my_queue = Stack(first_node)
    # my_queue.print_structure()

    second_node = Node("Mundo")
    my_queue.push(second_node)

    third_node = Node("third")
    my_queue.push(third_node)

    forth = Node("forth")
    my_queue.push(forth)

    my_queue.print_stack()

    my_queue.pop()

    print("-------------")

    my_queue.print_stack()

    my_queue.pop()
    my_queue.pop()
    my_queue.pop()
    my_queue.pop()
    my_queue.pop()

    print("-------------")

    my_queue.print_stack()


