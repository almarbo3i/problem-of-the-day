def pathway(distance):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    visited = set()
    
    #start point
    x = 0
    y = 0
    visited.add((x, y))

    for i in range(len(distance)):
        direction = directions[i % 4]  # Get the current direction
        for _ in range(distance[i]):
            x += direction[0]
            y += direction[1]
            if (x, y) in visited:
                return True
            visited.add((x, y))

    return False

print(pathway([2, 1, 1, 2]))  
print(pathway([1, 2, 3, 4]))  
print(pathway([1, 1, 1, 2, 1]))  


