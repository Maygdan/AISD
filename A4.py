import sys

input_data = sys.stdin.buffer
string_count = int(input_data.readline())
children = [{}]
prefix_counts = [0]

for _ in range(string_count):
    word = input_data.readline().strip()
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

query_count = int(input_data.readline())
answers = []

for _ in range(query_count):
    prefix = input_data.readline().strip()
    node = 0

    for character in prefix:
        next_node = children[node].get(character)
        if next_node is None:
            node = -1
            break
        node = next_node

    answers.append(str(prefix_counts[node] if node != -1 else 0))

sys.stdout.write("\n".join(answers))