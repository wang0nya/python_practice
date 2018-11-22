def find_shortest(graph, start, end, path=[]):
    path = path + [start] # concat?
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None

    for node in graph[start]:
        if node in path:
            newpath = find_shortest(graph, node, end, path)

            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    print(find_shortest(graph, 'A', 'D'))

    return shortest

# if __name__ == '__main__':
