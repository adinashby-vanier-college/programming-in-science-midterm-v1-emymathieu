import math

# Q1: Calculate the area of a circle

def area_of_circle(radius):

    area_of_circle = round(math.pi * radius ** 2, 2)
  
    return(area_of_circle)
print(area_of_circle(5))


# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    return ""

    if(n >= 4):
        for i in range(n):
            for j in range(n + i):
                if(i == 1 or j == 1 or i == 2 and j == 3 or i == 3 and j == 4):
                    result += "*"

            else:
                result += " "

        result += "\n"

    return result.rstrip()

print(hollow_right_triangle(4))
   

# Q3: Inverted Pyramid 
def inverted_pyramid(n):
    return ""
    if(n >= 3):
        for i in range(n):
            for j in range(((n + i) / 2) - 1):
                result += "*"

        else:
            result += " "

        result += "/n"
    return result.rstrip()
print(inverted_pyramid(3))
             
        


   

# # ----------------------------------------------------------------
# print(area_of_circle(5))
# print()

# print(hollow_right_triangle(3))
# print()

# print(hollow_right_triangle(4))
# print()

# print(hollow_right_triangle(5))
# print()

# print(inverted_pyramid(3))
# print()

# print(inverted_pyramid(4))
# print()

# print(inverted_pyramid(5))
# print()
