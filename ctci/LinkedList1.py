class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = node

    def print(self):
        if self.head is None:
            print("Emplty LL")
            return
        itr = self.head
        data = '';
        while itr:
            data += str(itr.data) + '-->'
            itr = itr.next
        print(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index >= self.get_length()-1 or index < 0:
            print("invalid position")
            return
        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr.next:
            count += 1
            if count == self.get_length()-1:
                itr.next.next = None
                return
            if count == index:
                itr.next = itr.next.next
                return

    def create_new(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(23)
    ll.insert_at_end(35)
    ll.create_new([39, 36, 37])
    ll.print()
    print(ll.get_length())

    ll.remove_at(4)
    ll.print()
