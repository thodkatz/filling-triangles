from filling_triangles.flat import flats
import numpy as np

def render(verts2d, faces, vcolors, depth, shade_t):
    m = 512
    n = 512
    img = np.ones((m,n,3))
    if shade_t == "flat":
        for triangle in faces:
            vertices = [verts2d[triangle[0]],
                        verts2d[triangle[1]],
                        verts2d[triangle[2]]]
            triangle_colors = [vcolors[triangle[0]],
                               vcolors[triangle[1]],
                               vcolors[triangle[2]]]
            flats(img,vertices,triangle_colors)

