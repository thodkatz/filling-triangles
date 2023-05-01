from filling_triangles.utils import color_average, drawline 

def flats(canvas, vertices, vcolors):
    # canvas: MxNX3
    # vertices: 3x2, coordinates of the points of a triangle, assume (x,y) -> (col,row)
    # vcolors: 3X3, rgb per point of a triangle
    # color of the triangle should be the average of the three points
    # source: http://www.sunshine2k.de/coding/java/TriangleRasterization/TriangleRasterization.html

    vertices.sort(key=lambda v: v[1])
    color = color_average(vcolors)
    if vertices[1][1] == vertices[2][1]:
        flat_bottom(canvas, vertices, color)
    elif vertices[0][1] == vertices[1][1]:
        flat_top(canvas, vertices, color)
    else:
        # split
        # (int)(vt1.x + ((float)(vt2.y - vt1.y) / (float)(vt3.y - vt1.y)) * (vt3.x - vt1.x)), vt2.y);
        split_vertix_x = int(vertices[0][0] + (vertices[1][1] - vertices[0][1])/(vertices[2][1] - vertices[0][1])*(vertices[2][0]-vertices[0][0]))
        split_point = [split_vertix_x, vertices[1][1]]

        bottom_points = list(vertices)
        bottom_points[-1] = split_point

        # canvas_prettier = np.zeros(shape=(canvas.shape[0], canvas.shape[1]))
        # for col,row in bottom_points:
        #     canvas_prettier[row][col] = -1 # edge flag
        # print(canvas_prettier)

        flat_bottom(canvas, bottom_points, color)

        top_points = list(vertices)
        top_points[0] = top_points[1]
        top_points[1] = split_point

        # canvas_prettier = np.zeros(shape=(canvas.shape[0], canvas.shape[1]))
        # for col,row in top_points:
        #     canvas_prettier[row][col] = -1 # edge flag
        # print(canvas_prettier)

        flat_top(canvas, top_points, color)
    
    # # make sure boundary is drawed
    # for vertix in vertices:
    #     drawpixel(canvas, vertix[0], vertix[1], color)


def flat_bottom(canvas, vertices, color):
    assert vertices[1][1] == vertices[2][1]

    invslope1 = (vertices[1][0] - vertices[0][0]) / (vertices[1][1] - vertices[0][1])
    invslope2 = (vertices[2][0] - vertices[0][0]) / (vertices[2][1] - vertices[0][1])

    curx1 = curx2 = vertices[0][0]
    ystart = vertices[0][1]
    ymax = vertices[1][1]

    for y in range(ystart, ymax + 1):
        # # draw boundary line
        # if y == ymax:
        #     left = min(vertices[1][0], vertices[2][0])
        #     right = max(vertices[1][0], vertices[2][0])
        #     drawline(canvas, int(left), int(right), y, color)
        # else:
        drawline(canvas, round(curx1), round(curx2), y, color)
        curx1 += invslope1
        curx2 += invslope2


def flat_top(canvas, vertices, color):
    assert vertices[0][1] == vertices[1][1]

    invslope1 = (vertices[2][0] - vertices[0][0]) / (vertices[2][1] - vertices[0][1])
    invslope2 = (vertices[2][0] - vertices[1][0]) / (vertices[2][1] - vertices[1][1])

    curx1 = curx2 = vertices[2][0]
    ystart = vertices[0][1]
    ymax = vertices[2][1]

    for y in range(ymax, ystart-1, -1):
        drawline(canvas, round(curx1), round(curx2), y, color)
        curx1 -= invslope1
        curx2 -= invslope2
