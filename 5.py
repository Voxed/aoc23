from numpy import *

# Parse input
chunks = [r.strip().split('\n')
          for r in open('input.txt').read().split('\n\n')]
objects_p1 = [('seed', (p, p + 1))
              for p in array(chunks[0][0].split()[1:], int64)]
objects_p2 = [('seed', (p[0], p[0] + p[1]))
              for p in array(reshape(chunks[0][0].split()[1:], (-1, 2)), int64)]

# Decode convertors and name progression
convertors = []
implicit_convertors = set()
for raw_name, *raw_convertors in chunks[1:]:
    c_from, _, c_to = raw_name.split()[0].split('-')
    implicit_convertors.add((c_from, c_to, (-inf, inf), 0))
    for r in raw_convertors:
        c_dest, c_source, c_length = map(int, r.split())
        convertors.append(
            (c_from, c_to, (c_source, c_source+c_length), c_dest-c_source))
convertors += list(implicit_convertors)


def intersect_range(a, b):
    """
    Intersect two ranges.
    Returns (intersection, slices) where slices is a list of cut off parts. 
    Returns None if no intersection is found.
    """
    intersection = (max(a[0], b[0]), min(a[1], b[1]))
    if intersection[0] >= intersection[1]:
        return None
    slices = []
    if a[0] < intersection[0]:
        slices.append((a[0], b[0]))
    if a[1] > intersection[1]:
        slices.append((b[1], a[1]))
    return (intersection, slices)


def get_min_location(objects):
    """Calculate the minimum location of an object in objects"""
    min_location = inf
    for o_state, o_range in objects:
        while 1:
            for c_from, c_to, c_range, c_shift in convertors:
                if c_from == o_state:
                    if (intersection := intersect_range(o_range, c_range)) is not None:
                        objects += [(o_state, slice)
                                    for slice in intersection[1]]
                        o_state, o_range = c_to, add(intersection[0], c_shift)
                        break
            else:
                break
        min_location = min(o_range[0], min_location)
    return min_location


# Print answers
print(get_min_location(objects_p1), get_min_location(objects_p2))
