
def ackermann(m, n):
    print(f"ackermann({m}, {n})", end=" ")
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
    
def ackermann_iterative(m, n):
    stack = []
    stack.append((m, n))
    
    while stack:
        m, n = stack.pop()
        
        if m == 0:
            if not stack:
                return n + 1
            stack[-1] = (stack[-1][0], n + 1)
        elif n == 0:
            stack.append((m - 1, 1))
        else:
            stack.append((m - 1, None))
            stack.append((m, n - 1))
    
    return n  
    
if __name__ == "__main__":
    m = 3
    n = 3
    o = 3
    p = 3
    result = ackermann(m, n)
    result_iterative = ackermann_iterative(o, p)

    print(f"Ackermann({m}, {n}) = {result}")
    print(f"Ackermann_iterative({o}, {p}) = {result_iterative}")
