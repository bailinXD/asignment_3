from os import system, name

def routers_analysis(numRouters, numLinks, links):
    impRouter = []
    for breakRouter in range(numRouters):
        breakLink = []
        for linksLoop in range(numLinks):
            if links[linksLoop][0] != breakRouter + 1 and links[linksLoop][1] != breakRouter + 1:
                breakLink.append(links[linksLoop])
        link = []
        link.append(breakLink[0][0])
        link.append(breakLink[0][1])
        for i in range(len(breakLink)):
            for j in range(len(breakLink)):
                if link.count(breakLink[j][0]) > 0 or link.count(breakLink[j][1]) > 0:
                    link.append(breakLink[j][0])
                    link.append(breakLink[j][1])
        num = 0
        for routersloop in range(numRouters):
            if link.count(routersloop + 1) > 0:
                num += 1
        if num != numRouters - 1:
            impRouter.append(breakRouter + 1)
    print(impRouter)
    return impRouter

routers_analysis(7, 7, [[1,2],[1,3],[2,4],[3,4],[3,6],[6,7],[4,5]])
