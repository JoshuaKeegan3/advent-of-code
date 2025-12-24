# with open("7/in.txt") as f:
#     _in = f.readlines()

# _in = _in[::2]

# beam_positions = [_in.pop(0).index("S")]

# splits = 0
# for line in _in:
#     new_beam_positions = []
#     indices = set(i for i, x in enumerate(line) if x == "^")
#     for beam in beam_positions:
#         if beam in indices:
#             new_beam_positions.append(beam + 1)
#             new_beam_positions.append(beam - 1)
#         else:
#             new_beam_positions.append(beam)
#     beam_positions = new_beam_positions

# print(len(beam_positions))


with open("7/in.txt") as f:
    _in = f.readlines()

_in = _in[::2]
one = _in.pop(0)
beam_positions = [1 if i == "S" else 0 for i in one]

splits = 0
for line in _in:
    new_beam_positions = [0 for i in line]
    indices = set(i for i, x in enumerate(line) if x == "^")
    for i, beam in enumerate(beam_positions):
        if beam == 0:
            continue
        if i in indices:
            new_beam_positions[i + 1] += beam
            new_beam_positions[i - 1] += beam
        else:
            new_beam_positions[i] += beam
    beam_positions = new_beam_positions
    print(beam_positions)

print(sum(beam_positions))
