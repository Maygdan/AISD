import sys

input_data = sys.stdin.buffer
string_count = int(input_data.readline())
children = [{}]
vertex_count = 1

for _ in range(string_count):
    word = input_data.readline().strip()
    vertex = 0

    for character in word:
        next_vertex = children[vertex].get(character)
        if next_vertex is None:
            next_vertex = len(children)
            children[vertex][character] = next_vertex
            children.append({})
            vertex_count += 1
        vertex = next_vertex

print(vertex_count)