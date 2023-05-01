import numpy as np

def color_average(vcolors):
    # average of rgb colors source: 
    # https://stackoverflow.com/questions/649454/what-is-the-best-way-to-average-two-colors-that-define-a-linear-gradient
    rgb_count = 3
    return [np.sum(np.sqrt(vcolors[:,i]))/rgb_count for i in range(rgb_count)]
    
def drawline(canvas, x1, x2, y, color):
    xleft = min(x1,x2)
    if x1 <= x2:
        xleft = x1
        xright = x2
    else:
        xleft = x2
        xright = x1
    for x in range(xleft, xright+1):
        drawpixel(canvas,x,y,color)


def drawpixel(canvas, x, y, color):
    canvas[y][x] = color


def interpolate_vectors(p1, p2, v1, v2, xy, dim):
    is_rank1 = dim == 1
    is_rank2 = dim == 2

    if is_rank1:
        assert p1 <= xy <= p2, "Linear interpolation rule"
        return v1 + (xy - p1) * ((v2-v1)/(p2-p1))
    elif is_rank2:
        assert v1 <= xy <= v2, "Linear interpolation rule"
        return p1 + (p2-p1) * ((xy-v1)/(v2-v1))
    else:
        raise ValueError(f"Unsopported dimension {dim}. Expected 1 or 2.")

def parse_input():
    return np.load("h1.npy", allow_pickle=True).tolist()