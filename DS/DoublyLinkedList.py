class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev # added this

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def  insert_at_beginning(self, data):
        node = Node(data, self.head)

        # added this
        if self.head:
            self.head.prev = node
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr:
            if itr.next:
                print (f"{itr.data} <--> ", end = "")
            else:
                print (itr.data)
            itr = itr.next

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr) # added itr to point to the current last node

    def insert_values(self, data_list):
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
            # added if statement
            if self.head:
                self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
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
                # update here to point to next & prev
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                break
            count += 1
            itr = itr.next

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(34)
    ll.insert_at_end(12)
    ll.insert_at_end(23)

    ll.insert_values([1, 2, 5, 3, 0, 42])
    print(ll.get_length())
    ll.remove_at_index(4)
    ll.insert_at_index(4, 32)
    ll.print()
