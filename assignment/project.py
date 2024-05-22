class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        """Pop the top item off the stack."""
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack is empty, cannot pop.")
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def peek(self):
        """Get the top item of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty, nothing to peek.")
            return None

    def size(self):
        """Get the number of items in the stack."""
        return len(self.stack)

    def display(self):
        """Display the stack."""
        print(f"Stack: {self.stack}")

# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    stack.display()
    
    stack.pop()
    stack.pop()
    
    stack.display()
    
    stack.pop()
    stack.pop()  # Attempt to pop from an empty stack
