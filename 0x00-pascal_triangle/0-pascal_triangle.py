#!/usr/bin/python3

'''
    pascal triangle
'''

def pascal_triangle(n):

    """This function  returns a list
       of lists of integers representing the Pascals triangle of n
    """

    if n <= 0:
        return []
    #initialize a triangle
    triangle = [[1]]

    #building each line of the triangle
    for i in range(1, n):
        line  = [1]

        #buiding each element of a line
        for j in range(1, i):
            #calculate each element:
            elem = triangle[i-1][j-1] + triangle[i-1][j]
            #assign element to a line
            line.append(elem)
        #assign 1 at the end of the line
        line.append(1)
        #assign each eline to triangle
        triangle.append(line)
    return triangle





def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

