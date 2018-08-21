def greet(name):
    if name == "Johnny":
        answer= "Hello, my love!"
    else:
        answer="Hello, {name}!".format(name=name)
    return answer
   