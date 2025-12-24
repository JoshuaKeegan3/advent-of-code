with open("7/in.txt") as f:
    _in = f.readlines()

_in = _in[::2]

beam_positions = set([_in.pop(0).index("S")])

splits = 0
for line in _in:
    new_beam_positions = set()
    indices = [i for i, x in enumerate(line) if x == "^"]
    for beam in beam_positions:
        if beam in indices:
            new_beam_positions.add(beam + 1)
            new_beam_positions.add(beam - 1)
            splits += 1
        else:
            new_beam_positions.add(beam)
    beam_positions = new_beam_positions
    print("".join([x if i not in beam_positions else "|" for i, x in enumerate(line)]))

print(splits)
