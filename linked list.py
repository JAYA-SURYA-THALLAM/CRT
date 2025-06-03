class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
    def add_ll(self):
        temp=self.head
        sum=0
        while temp:
            sum=sum+temp.data
            temp=temp.next
        return sum
        
    def getCount(self):
        count=0
        temp=head
        while temp:
            count=count+1
            temp=temp.next
        return count
        
    def insert_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_position(self,pos,data):
        if(pos==0):
            self.insert_begining(data)
        else:
            new_node=Node(data)
            temp=self.head
            for i in range(pos-1):
                if temp is None:
                    print("position out of bounds")
                    return
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def delete_position(self,pos,data):
        if(pos==0):
            self.delete_position(data)
        else:
            new_node=Node(data)
            temp=self.head
            for i in range(pos-1):
                if temp is None:
                    print("position out of bounds")
                    return
                temp=temp.next
            new_node.next=temp.next
            temp.next=temp.next.next  

def delete_value(self,value):
    if self.head.data == value:
        self.head = self.head.next
        return
    temp =self.head
    while temp.next and temp.next.data!=value:
        temp =temp.next
    if temp.next is None:
        print("value not found")
        return
    temp.next =temp.next.next                          
            
ll = LinkedList()
ll.insert_end(10)
ll.insert_begining(2222)
ll.insert_end(20)
ll.delete_value(20)
ll.insert_end(30)
ll.insert_end(40)
ll.insert_position(3,69)
ll.display()
print("sum of element in linked list")
ans=ll.add_ll()
print(ans)