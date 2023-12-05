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


def get_min_location(objects):
    '''Calculate the minimum location of an object in objects'''
    min_location = float('inf')
    for o_state, o_start, o_end in objects:
        while o_state != 'location':
            for c_from, c_to, c_start, c_end, c_shift in convertors:
                if c_from == o_state and c_start <= o_start < c_end:
                    if o_end > c_end:
                        objects.append((o_state, c_end, o_end))
                    o_state, o_start, o_end = c_to, o_start + \
                        c_shift, min(o_end, c_end) + c_shift
                    break
            else:
                o_state = name_progression[o_state]
        min_location = min(o_start, min_location)
    return min_location


# Print answers
print(get_min_location(objects_p1), get_min_location(objects_p2))
