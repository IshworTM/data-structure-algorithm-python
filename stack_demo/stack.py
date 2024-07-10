
#Custom Exceptions
class StackOverFlowError(Exception):
    """This exception is raised when the stack is full.

    Args:
        Exception (Exception): Base class that StackOverFlowError inherits from.
    """
    def __init__(self, message="Error: Stack Overflow"):
        """Initializes an StackOverFlowError instance.

        Args:
            message (str, optional): The error message. Defaults to "Error: Stack Overflow".
        """
        self.message = message
        super().__init__(message)

        
class StackUnderFlowError(Exception):
    """This exception is raised when the stack is empty.

    Args:
        Exception (Exception): Base class that StackOverFlowError inherits from.
    """
    def __init__(self, message="Error: Stack Underflow"):
        """Initializes an StackUnderFlowError instance.

        Args:
            message (str, optional): The error message. Defaults to "Error: Stack Underflow".
        """
        self.message = message
        super().__init__(message)

while 1:
    try:
        MAX_SIZE = int(input("Enter the max size of the stack: "))
        if( MAX_SIZE <=0 ):
            print("Error: Stack size must be positive.")
            continue
        break
    except ValueError:
        print("Error: Invalid input, size can only be a positive integer.")

top = -1
stack = [None for _ in range(MAX_SIZE)]

def is_empty() -> bool:
    """Checks if the stack is empty of not.

    Returns:
        bool: True if the stack is empty else False.
    """
    return top == -1

def is_full() -> bool:
    """Checks if the stack is full or not.

    Returns:
        bool: True if the stack is full else False.
    """
    return top == MAX_SIZE -1
    
def push(val: int) -> None:
    """Pushes an element onto the stack.

    Args:
        val (int): Takes an integer value as an argument.

    Raises:
        StackOverFlowError.
    """
    global top, stack
    if is_full():
        raise StackOverFlowError
    else:
        top += 1
        stack[top] = val
        print(f"Successfully pushed {val} onto the stack.")

def pop() -> int:
    """Pops an element from the stack.

    Raises:
        StackUnderFlowError.

    Returns:
        int: Returns the popped item, if necessary.
    """
    global top
    if is_empty():
        raise StackUnderFlowError
    else:
        val = stack[top]
        stack[top] = None
        top -=1
        print(f"Successfully popped {val} from the stack.")
        return val
    
def peek() -> int:
    """To peek on the Top Of Stack element.

    Returns:
        int: The element on the top of the stack.
    """
    if is_empty():
        print("Stack is empty, nothing to peek.")
        return None
    else:
        val = stack[top]
        print(f"Top of the stack is {val}.")
        return val