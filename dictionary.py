a = [(1, 2), (4, 3), (5, 1)]
b = [(1, 3), (2, 4), (5, 2)]    # Seznamy
c = [(2, 5), (4, 1), (10, 1)]

def dict(a, b, c):
    
    slovnik = {} #Vytvoření slovníku

    # Cykly
    for id, value in a:
        if id in slovnik:
            slovnik[id][0] = value
        else:
            slovnik[id] = [value, 0, 0]

    for id, value in b:
        if id in slovnik:
            slovnik[id][1] = value
        else:
            slovnik[id] = [0, value, 0]

    for id, value in c:
        if id in slovnik:
            slovnik[id][2] = value
        else:
            slovnik[id] = [0, 0, value]
            
    print(slovnik)

dict(a, b, c) #Spuštění funcke