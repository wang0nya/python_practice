# Complete this function to return either
# "Hello, [name]!" or "Hello there!"
# based on the input

def say_hello(name):
  # you can print to STDOUT to debug if you need to:
    if len(name) is not 0:
        return "Hello, {}!".format(name)
    else:
        return "Hello there!"
    
    return name
  
  # but to complete the challenge you need to return a value
if __name__ == '__main__':
    name = input()
    print(say_hello(name)) # TODO: return correct value