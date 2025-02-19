class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
            if self.head is None:
                print("Linked list is empty")
                return

            itr = self.head
            while itr:
                if itr.next:
                    print(f"{itr.data} --> ", end = "")
                else:
                    print(itr.data)
                itr = itr.next

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next: # iterates while there is a next node
            itr = itr.next # keep going forward until it reachres the end

        itr.next = Node(data, None)

    def insert_values(self, data_list): # creates new LinkedList with multiple values
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # previous element
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            count += 1
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(34)
    ll.insert_at_end(12)
    ll.insert_at_end(23)

    ll.insert_values([1, 2, 5, 3, 0, 42])
    print(ll.get_length())
    ll.remove_at_index(4)
    ll.insert_at_index(4, 32)
    ll.print()