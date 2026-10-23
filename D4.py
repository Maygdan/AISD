import sys
from collections import deque

data = sys.stdin.buffer.read().split()
text = data[0]
word_count = int(data[1])
words = data[2:2 + word_count]

children = [{}]
failure = [0]
terminal_word = [-1]
output_link = [-1]

for word_index, word in enumerate(words):
    node = 0
    for character in word:
        next_node = children[node].get(character)
        if next_node is None:
            next_node = len(children)
            children[node][character] = next_node
            children.append({})
            failure.append(0)
            terminal_word.append(-1)
            output_link.append(-1)
        node = next_node
    terminal_word[node] = word_index

queue = deque()
for node in children[0].values():
    queue.append(node)

while queue:
    node = queue.popleft()
    fallback = failure[node]
    output_link[node] = (
        fallback if terminal_word[fallback] != -1 else output_link[fallback]
    )

    for character, next_node in children[node].items():
        fallback = failure[node]
        while fallback and character not in children[fallback]:
            fallback = failure[fallback]
        failure[next_node] = children[fallback].get(character, 0)
        queue.append(next_node)

sentinel = len(children)
next_unfound = [sentinel] * (sentinel + 1)
for node, word_index in enumerate(terminal_word):
    if word_index != -1:
        next_unfound[node] = node


def find_unfound(node):
    root = node
    while next_unfound[root] != root:
        root = next_unfound[root]

    while next_unfound[node] != node:
        following = next_unfound[node]
        next_unfound[node] = root
        node = following

    return root


found = [False] * word_count
state = 0

for character in text:
    while state and character not in children[state]:
        state = failure[state]
    state = children[state].get(character, 0)

    node = state if terminal_word[state] != -1 else output_link[state]
    node = find_unfound(node) if node != -1 else sentinel

    while node != sentinel:
        found[terminal_word[node]] = True
        next_unfound[node] = find_unfound(
            output_link[node] if output_link[node] != -1 else sentinel
        )
        node = next_unfound[node]

sys.stdout.write("\n".join("Yes" if exists else "No" for exists in found))