string = input()
if len(string) >= 3:
    print(string + "ing")
elif string == (string + "ing"):
    print((string + "ing") + "ly")
elif len(string) < 3:
    print(string)
  
    
