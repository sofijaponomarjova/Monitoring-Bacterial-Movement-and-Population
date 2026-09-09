from math import sqrt #imports sqrt function from math library

def calculate_momentum(x,y,z): #defines the function to calculate momentum
    sqrd_values=x**2+y**2+z**2 #saves into a variable sum of squared momentum components
    try: 
        p=sqrt(sqrd_values) #tries to calculate the final momentum
        return p #returns the momentum
    except ValueError: #if a value error occurs (e.g. number inside sqrt is negative warns the user about error)
        print("Can't compute the square root of negative number")
    except: #if another error occurs warns the user about error
        print("An error occured")
    

print("--The momentum of each bacteria--\n") #prints the title
with open("output-Set0.txt", "r") as file: #opens the file for reading
    for i, line in enumerate(file): #iterates over each line in file, saves line index as "i" and line content as "line"
        if i==0: 
            continue #skips the first line
        values=line.split() #splits the line string into separate values
        x=float(values[0]) #saves x component as separate variable
        y=float(values[1]) #saves y component as separate variable
        z=float(values[2]) #saves z component as separate variable
        momentum=calculate_momentum(x, y, z) #calls the function to calculate the momentum and saves the result in a variable
        print(f"Bacteria No. {i} Momentum: {momentum}") #prints the calculated momentum & explains what's printed