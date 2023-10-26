# Define a function tri to calculate the area of a triangle given three sets of coordinates.
def tri(x1, y1, x2, y2, x3, y3):
    # Calculate the area using the provided coordinates.
    area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return area

# Start an infinite loop for user input and area calculation.
while True:
    # Prompt the user to enter the first set of coordinates in x,y format.
    print("Enter the first coordinates in x,y:")
    one = input()
    one = one.split(",")  # Split the input into x and y components.
    
    # Parse the x and y components as integers.
    x1 = int(one[0])
    y1 = int(one[1])
    
    # Prompt the user to enter the second set of coordinates in x,y format.
    print("Enter the second coordinates in x,y:")
    two = input()
    two = two.split(",")  # Split the input into x and y components.
    
    # Parse the x and y components of the second coordinate.
    x2 = int(two[0])
    y2 = int(two[1])
    
    # Prompt the user to enter the third set of coordinates in x,y format.
    print("Enter the third coordinates in x,y:")
    third = input()
    third = third.split(",")  # Split the input into x and y components.
    
    # Parse the x and y components of the third coordinate.
    x3 = int(third[0])
    y3 = int(third[1])
    
    # Call the tri function to calculate the area and store it in the 'var' variable.
    var = tri(x1, y1, x2, y2, x3, y3)
    
    # Display the calculated area to the user.
    print(f"The area is:")
    print(var) # comments thanks to chatgpt 