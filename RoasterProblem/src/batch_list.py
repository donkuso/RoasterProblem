

class BatchNode:
    def __init__(self, blend_name, next=None):
        self.blend_name = blend_name
        self.next = next


class BatchList:
    def __init__(self):
        self.head = None

    def add_batch(self, blend_name):
        """Add a new batch at the start of the list"""
        new_node = BatchNode(blend_name)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """Print the sequence of batches"""
        current = self.head
        print("Batch history:")
        while current:
            print(f" - {current.blend_name}")
            current = current.next
