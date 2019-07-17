import re

sub_txt = open("triangles.txt", mode="r", encoding="utf-8").read()
lines = sub_txt.split("\n")


def is_triangle(input_str):
    input_digit = re.split(r'\W+', input_str)
    if int(input_digit[0]) < int(input_digit[1]) + int(input_digit[2])\
            and int(input_digit[1]) < int(input_digit[0]) + int(input_digit[2])\
            and int(input_digit[2]) < int(input_digit[1]) + int(input_digit[0]):
        alert = "these make a triangle!"
        validation = True
    else:
        alert ="these dont make a triangle!"
        validation = False
    return alert,validation

def triangle_type(input_str):
    input_digit = re.split(r'\W+', input_str)
    if int(input_digit[0]) == int(input_digit[1]) \
            and int(input_digit[1]) == int(input_digit[2]):
        validation = "this is a equilateral triangle!"
    elif (int(input_digit[0]) == int(input_digit[1]) and int(input_digit[1]) != int(input_digit[2]))\
            or (int(input_digit[0]) == int(input_digit[2])and int(input_digit[1]) != int(input_digit[2]))\
            or (int(input_digit[1]) == int(input_digit[2]) and int(input_digit[0]) != int(input_digit[2])):
        validation = "this is a isosceles triangle!"
    elif int(input_digit[0])**2 == int(input_digit[1])**2 + int(input_digit[2])**2 \
            or int(input_digit[1])**2 == int(input_digit[0])**2 + int(input_digit[2])**2 \
            or int(input_digit[2])**2 == int(input_digit[1])**2 + int(input_digit[0])**2:
        validation = "this is a right angled triangle!"
    else:
        validation = "this is a scalene triangle"

    return validation


for i in range(len(lines)):
    valid = is_triangle(lines[i])
    print(lines[i], "==>", valid[0],"\n")
    if valid[1]==True :
        tr_type = triangle_type(lines[i])
        print(tr_type,"\n\n")






