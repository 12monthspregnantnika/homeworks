
def shedareba(x, y, n):
    if x>y and x>n:
        return("x " + "მეტია " + "y "+ "-ზე" + str(x/y) + "ჯერ " + "და " + "x " + "მეტია " + "n " + "-ზე " + str(x/n) + "ჯერ ")
    if y>x and y>n:
        return("y " + "მეტია " + "x " + "-ზე" + str(y/x) + "ჯერ " + "და " + "y " + "მეტია " + "n " + "-ზე " + str(y/n) + "ჯერ ")
    if n>x and n>y:
        return("n " + "მეტია " + "x " + "-ზე" + str(n/x) + "ჯერ " + "და " + "n " + "მეტია " + "y " + "-ზე " + str(n/y) + "ჯერ ")
print(shedareba(10, 45, 5))





        
