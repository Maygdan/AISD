import sys

data = sys.stdin.buffer.read().split()
string_count = int(data[0])
words = data[1:1 + string_count]

children = [{}]
prefix_counts = [0]

for word in words:
    node = 0
    for character in word:
        next_node = children[node].get(character)
        if next_node is None:
            next_node = len(children)
            children[node][character] = next_node
            children.append({})
            prefix_counts.append(0)
        node = next_node
        prefix_counts[node] += 1

answers = []
for word in words:
    node = 0
    for length, character in enumerate(word, 1):
        node = children[node][character]
        if prefix_counts[node] == 1:
            answers.append(word[:length].decode())
            break
    else:
        answers.append("-")

sys.stdout.write("\n".join(answers))