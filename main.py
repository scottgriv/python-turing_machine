#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
#function to perform action of states
def action(inp, rep, move):
    global tapehead
    if tape[tapehead] == inp:
        tape[tapehead] = rep
        if move == 'L':
            tapehead -= 1
        else:
            tapehead += 1
        return True
    return False

tape = ['B']*50 
string = input("Enter String: ")
i = 5
tapehead = 5
for s in string: #loop to place string in tape
    tape[i] = s
    i += 1

state = 0
a, b, X, Z, U, V, R, L, B = 'a', 'b', 'X', 'Z', 'U', 'V', 'R', 'L', 'B'
oldtapehead = -1
accept = False
while(oldtapehead != tapehead): #if tapehead not moving that means terminate Turing machine
    oldtapehead = tapehead

    if state == 0:
        if action(a, X, R):
            state = 1
        elif action(B, B, R):
            state = 10
        elif action(Z, Z, R):
            state = 7
        elif action(b, U, R):
            state = 4

    elif state == 1:
        if action(a, a, R):
            state = 1
        elif action(b, b, R):
            state = 2
        elif action(B, B, L):
            state = 11

    elif state == 2:
        if action(b, b, R) or action(Z, Z, R):
            state = 2
        elif action(a, Z, L):
            state = 3

    elif state == 3:
        if action(b, b, L) or action(Z, Z, L) or action(a, a, L):
            state = 3
        elif action(X, X, R):
            state = 0

    elif state == 4:
        if action(b, b, R):
            state = 4
        elif action(Z, Z, R):
            state = 5
        elif action(B, B, L):
            state = 15

    elif state == 5:
        if action(Z, Z, R) or action(V, V, R):
            state = 5
        elif action(b, V, L):
            state = 6

    elif state == 6:
        if action(Z, Z, L) or action(V, V, L) or action(b, b, L):
            state = 6
        elif action(U, U, R):
            state = 0

    elif state == 7:
        if action(Z, Z, R):
            state = 7
        elif action(V, V, R):
            state = 8

    elif state == 8:
        if action(V, V, R):
            state = 8
        elif action(B, B, R):
            state = 9

    elif state == 11:
        if action(a, a, L):
            state = 11
        elif action(X, X, R):
            state = 12

    elif state == 12:
        if action(a, Z, R):
            state = 13

    elif state == 13:
        if action(a, X, R):
            state = 12
        elif action(B, B, R):
            state = 14

    elif state == 15:
        if action(b, b, L):
            state = 15
        elif action(U, U, R):
            state = 16

    elif state == 16:
        if action(b, V, R):
            state = 17

    elif state == 17:
        if action(b, U, R):
            state = 16
        elif action(B, B, R):
            state = 18

    else:
        accept = True


if accept:
    print("String accepted on state = ", state)
else:
    print("String not accepted on state = ", state)