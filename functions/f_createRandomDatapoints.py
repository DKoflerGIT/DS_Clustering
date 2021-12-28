def createDatapoints(num, dim):
    import random

    E = []
    pt = []

    for n in range(num):
        pt.clear()
        for d in range(dim):
            pt.append(random.randint(0,100))
        E.append(tuple(pt))
    
    return E