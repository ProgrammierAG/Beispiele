f = input("Lieblings Essen ")



def setEssen(n):
    global f
    f = n
 
    print("gi")

def greet(food, name = input("Name "), alter = input("Alter ")):
    print(f"Hallo {name} Sie sind {alter} jahre alt und essen {food} am liebsten.")

greet(f)
setEssen("Eis")
print(f"f = {f}")
greet(f)
