# def push(value):
#     top =-1
#     if (top==4):
#         return "stack is full"
#     else:
#         top=top+1
#         return stack.append(value)
# def pop():
#     top=5
#     if(top!=1):
#         return stack.pop()
#     else:
#         return "stack is empty" 
# def peek():

# top=-1
# size=5
# stack=[None]*size
# push(20)
# push(30)
# push(40)
# push(50)
# push(60)
# pop_element()

# print(stack)
    

stack=[]
top= -1

def push(value):
    global top
    stack.append(value)
    top+=1
def pop():
    global top
    if top ==-1:
        print("stack is empty.nothing to pop")
        return
    else:
        stack.pop()
        top-=1
def peek():
    if top==-1:
        return "stack is rmpty.no top element"
    else:
        return f"top element={stack[top]}"
def display():
    if(top==-1):
        print("empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])
while True:
    while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter element to push: "))
        push(value)
    elif choice==2:
        pop()
    elif choice==3:
        print(peek())
    elif choice==4:
        display()
    else:
        print("Exit")
        break
push(10)
push(20)
push(30)
push(40)
push(50)
push(60)
push(70)
pop()
pop()
print(peek())
display()

     