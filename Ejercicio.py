class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def top(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)

def my_stack_function(arr):
    stack = Stack()
    for num in arr:
        if stack.isEmpty() or num > stack.top():
            stack.push(num)
        else:
            temp_stack = Stack()
            while not stack.isEmpty() and num < stack.top():
                temp_stack.push(stack.pop())
            stack.push(num)
            while not temp_stack.isEmpty():
                stack.push(temp_stack.pop())
				
    return stack.items

array = [7, 9, -5, 6, 10, -33, 41, 12]
print("Entrada:", array)
print("Resultado:", my_stack_function(array))