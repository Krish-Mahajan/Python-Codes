 class ListNode(object):
     def __init__(self, x):
         self.data = x
         self.next_node = None
 
 
 
     def sortList(self, head):
             if head==None:
                 return None
             
             dummy=ListNode(0)
             dummy.next_node=head
             current=head  #LastSorted=data
             while current.next_node:
                 if(current.next_node.data< current.data):
                     temp=dummy  #tmp=dummy
                     while( temp.next_node.data<current.next_node.data):
                         temp=temp.next_node
                     nextToSort=current.next_node
                     current.next_node=nextToSort.next_node
                     nextToSort.next_node=temp.next_node
                     temp.next_node=nextToSort                 
                 else:
                     current=current.next  