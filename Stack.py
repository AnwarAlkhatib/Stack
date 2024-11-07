stack = [None] * 5
top = -1

# Funktion zum Hinzufügen eines Elements zum Stack 
def push(value):
    global top
    
    # Überprüfen, ob 'top' die letzte Position im Stack erreicht hat
    if len(stack)-1 == top:
        print("stack ist überfüllt")
    else:
        top +=1
        stack[top] = value
        print(f"Element {value} wurde erfolgreich zum stack hinzugefügt")

def pop():
    global top

    if top == -1:
        print("stack underflow")
    else:
        # Gibt das aberste Element des Stacks zurück und verringert 'top'
        value = stack[top]
        top -= 1
        return value

def peek():
    global top

    if top == -1:
        print("stack underflow")
    else:
        # Gibt das aberste Element des Stacks zurück und verringert 'top'
        value = stack[top]
        return value

def display():
    if top == -1:
        print("stack underflow")
    else:
        for i in range(top, -1, -1):
            print(stack[i])



push(1)
push(2)
push(3)




print(stack)

print(f"pop Funktion {pop()}")

print(f"Peek Funktion {peek()}")
print(f"{display()}")