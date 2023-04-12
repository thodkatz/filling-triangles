import numpy as np


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

def filling_triangles():
    data = parse_input()
    print(data["verts2d"].shape)


def main():
    filling_triangles()



if __name__ == "__main__":
    main()
