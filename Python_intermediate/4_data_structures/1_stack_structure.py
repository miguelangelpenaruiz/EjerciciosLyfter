class Node:
    top : Node

    def __init__(self, data):
        self.data = data
        self.under = None

class Stack:
    def __init__(self, top):
        self.top = top

    def push(self, data):
        current_node = self.top
        while current_node.under is not None:
            current_node = current_node.under
        self.top = data

    def pop(self):
        current_node = self.top
        if self.top:
            current_node.under = self.top
            

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

    my_queue.print_stack()

    # third_node = Node("third")
    # my_queue.enqueue(third_node)

    # forth = Node("forth")
    # my_queue.enqueue(forth)

    # my_queue.print_structure()

    # print("DEQUEUE")

    # my_queue.dequeue()
    # my_queue.print_structure()

    # print("DEQUEUE")

    # my_queue.dequeue()
    # my_queue.print_structure()

    # print("DEQUEUE")

    # my_queue.dequeue()
    # my_queue.print_structure()

    # print("DEQUEUE")

    # my_queue.dequeue()
    # my_queue.print_structure()


    # print("DEQUEUE")

    # my_queue.dequeue()
    # my_queue.print_structure()