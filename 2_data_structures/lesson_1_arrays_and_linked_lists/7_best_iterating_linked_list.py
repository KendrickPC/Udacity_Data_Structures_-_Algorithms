class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def best_linked_list(input_list):
    head = None
    tail = None
    for value in input_list:    
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next

    return head 

### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)
        
        

input_list = [1, 2, 3, 4, 5, 6]
head = best_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = best_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = best_linked_list(input_list)
test_function(input_list, head)