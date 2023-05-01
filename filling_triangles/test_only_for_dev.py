import numpy as np
from filling_triangles.render import flats


def test_flats(points):
    m = 5
    n = 5
    draw_boundaries(m,n,points)
    canvas = np.zeros(shape=(m,n,3))
    
    vcolors = np.ones(shape=(3,3))
    flats(canvas, points, vcolors)

    canvas_prettier = np.zeros(shape=(m,n))
    for y in range(m):
        for x in range(n):
            if not np.array_equal(canvas[y][x],[0,0,0]):
                canvas_prettier[y][x] = 1

    print(canvas_prettier)
    print()

def draw_boundaries(m,n,points):
    array = np.zeros(shape=(m,n))
    for col,row in points:
        array[row][col] = -1 # edge flag
    print(array)



if __name__ == "__main__":
    # define points of a triangle
    p1 = [2,2]
    p2 = [4,0]
    p3 = [3,4]
    points = [p1,p2,p3]
    test_flats(points)


    p1 = [2,2]
    p2 = [4,0]
    p3 = [4,4]
    points = [p1,p2,p3]
    test_flats(points)

    p1 = [2,2]
    p2 = [2,4]
    p3 = [4,0]
    points = [p1,p2,p3]
    test_flats(points)

    # good one
    p1 = [0,0]
    p2 = [1,4]
    p3 = [4,1]
    points = [p1,p2,p3]
    test_flats(points)

    p1 = [0,0]
    p2 = [4,0]
    p3 = [0,4]
    points = [p1,p2,p3]
    test_flats(points)

    p1 = [0,0]
    p2 = [0,4]
    p3 = [2,2]
    points = [p1,p2,p3]
    test_flats(points)

    p1 = [1,2]
    p2 = [1,4]
    p3 = [4,4]
    points = [p1,p2,p3]
    test_flats(points)

    p1 = [0,0]
    p2 = [0,4]
    p3 = [4,4]
    points = [p1,p2,p3]
    test_flats(points)
