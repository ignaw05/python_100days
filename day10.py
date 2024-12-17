def sum(n, m):
    return n + m
def mult(n,m):
    return n*m
def div(n,m):
    return n/m
def rest(n,m):
    return n - m

operations = {
    "+" : sum,
    "-" : rest,
    "*" : mult,
    "/" : div
}
def calculator(n=None):
    while True:
        if n == None:
            n = float(input("What's the first number? "))
        print("+\n-\n*\n/\n")
        operation = input("Pick an operation: ")
        m = float(input("What's the next number? "))

        r = operations[operation](n,m)
        print(f"({n} {operation} {m} = {r})")

        ask = input(f"Type 'y' to continue with {r}, or 'n' to start a new")
        if ask == 'y': another = True
        elif ask == 'n': another = False
        else: break
        while another: 
            calculator(r)


calculator()