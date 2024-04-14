name = "Dave"
count = 1

# greeting()

def another():
    color = "blue"
    global count 
    count += 2
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dave")

another()