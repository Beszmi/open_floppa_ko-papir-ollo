def rpsa(rep):
    import random
    statok=list()
    win=0
    draw=0
    loss=0
    for i in range(rep):
        rand=str(random.randint(1,3))
        match rand:
            case "1":
                win+=1
            case "2":
                draw+=1
            case "3":
                loss+=1
    statok.append(win)
    statok.append(draw)
    statok.append(loss)
    return statok
#print(rpsa(6))