class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insertatbeginning(self, data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode
    def insertatmiddle(self, data, position):
        newnode = node(data)
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode
    def insertatend(self, data):
        newnode = node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newnode
    def printlist(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
if __name__ == "__main__":
    list=linkedlist()
    list.insertatbeginning(1)
    list.insertatbeginning(2)
    list.insertatbeginning(3)
    list.insertatmiddle(4,2)
    list.insertatend(5)   
    list.printlist()
