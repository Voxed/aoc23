from numpy import *

# Parse input
chunks = [r.strip().split('\n')
          for r in open('input.txt').read().split('\n\n')]
objects_p1 = [('seed', p, p + 1)
              for p in array(chunks[0][0].split()[1:], int64)]
objects_p2 = [('seed', p[0], p[0] + p[1])
              for p in array(reshape(chunks[0][0].split()[1:], (-1, 2)), int64)]

# Decode convertors and name progression
convertors = []
name_progression = {}
for raw_name, *raw_convertors in chunks[1:]:
    c_from, _, c_to = raw_name.split()[0].split('-')
    name_progression[c_from] = c_to
    for r in raw_convertors:
        c_dest, c_source, c_length = map(int, r.split())
        convertors.append(
            (c_from, c_to, c_source, c_source+c_length, c_dest-c_source))

def intersect_range(a_start, a_end, b_start, b_end):
    intersection = (max(a_start, b_start), min(a_end, b_end))
    if intersection[0] >= intersection[1]:
        return None
    slices = []
    if a_start < intersection[0]:
        slices.append((a_start, b_start))
    if a_end > intersection[1]:
        slices.append((b_end, a_end))
    return (intersection, slices)

def get_min_location(objects):
    '''Calculate the minimum location of an object in objects'''
    min_location = float('inf')
    for o_state, o_start, o_end in objects:
        while o_state != 'location':
            for c_from, c_to, c_start, c_end, c_shift in convertors:
                if c_from == o_state:
                    intersection = intersect_range(o_start, o_end, c_start, c_end)
                    if intersection is not None:
                        o_start, o_end = intersection[0]
                        o_start += c_shift
                        o_end += c_shift
                        for slice in intersection[1]:
                            objects.append((o_state, slice[0], slice[1]))
                        o_state = c_to
                        break
            else:
                o_state = name_progression[o_state]
        min_location = min(o_start, min_location)
    return min_location


# Print answers
print(get_min_location(objects_p1), get_min_location(objects_p2))


print(intersect_range(5, 10, 30, 100))