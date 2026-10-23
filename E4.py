import sys

data = sys.stdin.buffer.read().split()
command_count = int(data[0])

children = [{}]
subtree_sizes = [0]
is_word = [False]
answers = []
alphabet = range(ord("a"), ord("z") + 1)

for command in data[1:command_count + 1]:
    if command.isdigit():
        rank = int(command)
        node = 0
        prefix = bytearray()

        while True:
            if is_word[node]:
                if rank == 1:
                    answers.append(bytes(prefix))
                    break
                rank -= 1

            for character in alphabet:
                child = children[node].get(character)
                if child is None:
                    continue

                if rank > subtree_sizes[child]:
                    rank -= subtree_sizes[child]
                else:
                    prefix.append(character)
                    node = child
                    break

        continue

    node = 0
    path = [0]
    for character in command:
        child = children[node].get(character)
        if child is None:
            child = len(children)
            children[node][character] = child
            children.append({})
            subtree_sizes.append(0)
            is_word.append(False)
        node = child
        path.append(node)

    if not is_word[node]:
        is_word[node] = True
        for path_node in path:
            subtree_sizes[path_node] += 1

sys.stdout.write(b"\n".join(answers).decode())