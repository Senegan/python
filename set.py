def intersection_update(A, s):
    A.intersection_update(s)
    return A

def update(A, s):
    A.update(s)
    return A

def symmetric_difference_update(A, s):
    A.symmetric_difference_update(s)
    return A

def difference_update(A, s):
    A.difference_update(s)
    return A

if __name__ == '__main__':
    try:
        # Input number of elements in set A
        n = int(input().strip())
        # Input elements of set A
        A = set(map(int, input().strip().split()))
        
        # Input number of operations
        c = int(input().strip())
        
        # Perform operations
        for _ in range(c):
            # Read the operation name
            operation_line = input().strip().split()
            operation = operation_line[0]
            t = int(operation_line[1])  # Number of elements in the set for this operation
            
            # Read the set elements
            s = set(map(int, input().strip().split()))
            
            if operation == "intersection_update":
                intersection_update(A, s)
            elif operation == "update":
                update(A, s)
            elif operation == "symmetric_difference_update":
                symmetric_difference_update(A, s)
            elif operation == "difference_update":
                difference_update(A, s)
            else:
                print("Invalid operation")
                break
        
        # Calculate and print the sum of elements in the final set A
        sum_A = sum(A)
        print(sum_A)
        
    except EOFError:
        print("Unexpected end of input. Please check the input format and try again.")
    except ValueError:
        print("Invalid input. Please enter integers as required.")

#input
#16

#1 2 3 4 5

#1

#intersection_update 10

#1 2 3 4

#output

# 15  
