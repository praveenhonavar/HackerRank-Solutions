class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:

    def __init__(self):
        self.head=None

    def insertFront(self,data):
        node=Node(data,self.head)
        self.head=node


    def insertEnd(self,data):

        # node=Node(data,None)

        temp=self.head
        while(temp.next != None):
            temp=temp.next
        temp.next=Node(data,None)


    def delete(self,index):

        temp=self.head
        c=0

        while(c!=(index-1)):
            c+=1
            temp=temp.next
        temp.next=temp.next.next


    def insertAt(self,data,index):

        temp=self.head
        c=0

        while(c!=(index-1)):
            c+=1
            temp=temp.next
        temp.next=Node(data,temp.next)


    def reverse(self):
        prev=None
        curnt=self.head
        # print('gigjir')
        while(curnt != None):
            # print('llel')
            fwd=curnt.next
            curnt.next=prev
            prev=curnt
            curnt=fwd
        self.head=prev

        


    def print(self):
        temp=self.head
        while(temp.next != None):
            print(temp.data)
            temp=temp.next
        print(temp.data)

    def printMid(self):

        f=self.head 
        s=self.head

        while(f.next != None):
            f=f.next.next
            s=s.next
        s.next=s.next.next

        # print(s.next.data) 



l=LinkedList()


l.insertFront(50)
l.insertFront(40)
l.insertFront(70)
l.insertFront(10)
l.insertFront(20)


l.insertEnd(11)
l.insertEnd(12)
l.insertEnd(13)


l.delete(3)
l.delete(5)

l.insertAt(99,1)
l.insertAt(606,2)
l.insertAt(5,1)

l.print()
print('____________________________--')
# l.reverse()

l.printMid()

print('____________________________--')


l.print()
