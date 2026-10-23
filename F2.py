import sys

s = sys.stdin.buffer.readline().strip()

lengths = [0]
links = [-1]
transitions = [{}]
last = 0

for character in s:
    current = len(lengths)
    lengths.append(lengths[last] + 1)
    links.append(0)
    transitions.append({})

    state = last
    while state != -1 and character not in transitions[state]:
        transitions[state][character] = current
        state = links[state]

    if state == -1:
        links[current] = 0
    else:
        target = transitions[state][character]
        if lengths[state] + 1 == lengths[target]:
            links[current] = target
        else:
            clone = len(lengths)
            lengths.append(lengths[state] + 1)
            links.append(links[target])
            transitions.append(transitions[target].copy())

            while state != -1 and transitions[state].get(character) == target:
                transitions[state][character] = clone
                state = links[state]

            links[target] = clone
            links[current] = clone

    last = current

print(sum(lengths[state] - lengths[links[state]] for state in range(1, len(lengths))))