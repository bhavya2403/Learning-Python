# https://www.youtube.com/watch?v=rw4s4M3hFfs

def minFarthestDistance(blocks, req):
    n = len(req)
    indices = {req[i]: i for i in range(n)}
    answer = [{i: 0 for i in range(n)} for _ in range(len(blocks))]

    minDistAbove = [-1] * n
    for idx, block in enumerate(blocks):
        for build, exists in enumerate(block):
            if exists:
                if block[build]:
                    minDistAbove[indices[build]] = 1
                else:
                    if minDistAbove[indices[build]] == -1:
                        answer[idx][indices[build]] = -1
                    else:
                        answer[idx][indices[build]] = minDistAbove[indices[build]]
                        minDistAbove[indices[build]] += 1

    minDistBelow = [-1] * n
    for idx in range(len(blocks)-1, -1, -1):
        block = blocks[idx]
        for build, exists in enumerate(block):
            if exists:
                if block[build]:
                    minDistBelow[indices[build]] = 1
                else:
                    if minDistBelow[indices[build]] == -1:
                        pass
                    else:
                        if answer[idx][indices[build]] == -1:
                            answer[idx][indices[build]] = minDistBelow[indices[build]]
                        else:
                            answer[idx][indices[build]] = min(answer[idx][indices[build]], minDistBelow[indices[build]])
                        minDistBelow[indices[build]] += 1

    optimalBlock = 0
    minFarthest = 10000
    for idx, block in enumerate(answer):
        farthest = 0
        for build, dist in enumerate(block):
            if dist > farthest:
                farthest = dist

        if farthest < minFarthest:
            optimalBlock = idx


    return optimalBlock

blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
]
requirements = ["gym", "school"]

print(minFarthestDistance(blocks, requirements))