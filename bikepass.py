import sys
import matplotlib.pyplot as plt
import matplotlib.colors as col

def closest_neighbour(Vdist, Vqueue):
    for i in range(len(Vdist)):
        if not i in Vqueue:
            Vdist[i] = sys.maxsize

    return Vdist.index(min(Vdist))

def dijkstra(graph, start):
    Vn = len(graph)
    Vqueue = list(range(Vn))
    Vpath = [[start]]*Vn

    Vdist = [sys.maxsize]*Vn
    Vdist[start] = 0

    while len(Vqueue) > 0:
        v = closest_neighbour(Vdist[:], Vqueue[:])
        del Vqueue[Vqueue.index(v)]

        Uadj = [i for i, e in enumerate(graph[v]) if e != 0]

        for u in Uadj:
            alt = Vdist[v] + graph[v][u]
            if alt < Vdist[u]:
                Vdist[u] = alt
                Vpath[u] = Vpath[v] + [u]

    return Vpath

def minp(l):
    minel = sys.maxsize
    for e in l:
        if e > 0 and e < minel:
            minel = e

    return minel

if __name__ == "__main__":
    Vn = 26

    sweights = [1, 1.5, 2, 3]

    scary = []
    dists = []
    costs = []
    traffic = []
    colmap = []

    for i in range(Vn):
        scary.append([0]*Vn)
        dists.append([0]*Vn)
        costs.append([0]*Vn)
        traffic.append([0]*Vn)
        colmap.append([0]*Vn)

    # bike stress ratings
    scary[0][1], dists[0][1] = 3, 305
    scary[0][6], dists[0][6] = 3, 497
    scary[1][2], dists[1][2] = 3, 356
    scary[1][7], dists[1][7] = 3, 436
    scary[2][21], dists[2][21] = 4, 1960
    scary[2][3], dists[2][3] = 3, 684
    scary[3][4], dists[3][4] = 3, 474
    scary[3][9], dists[3][9] = 3, 635
    scary[4][10], dists[4][10] = 3, 632
    scary[4][5], dists[4][5] = 4, 792
    scary[5][12], dists[5][12] = 3, 654
    scary[6][7], dists[6][7] = 2, 268
    scary[6][13], dists[6][13] = 3, 504
    scary[7][8], dists[7][8] = 2, 335
    scary[7][14], dists[7][14] = 2, 668
    scary[9][15], dists[9][15] = 2, 1130
    scary[9][10], dists[9][10] = 3, 399
    scary[10][15], dists[10][15] = 3, 232
    scary[10][11], dists[10][11] = 3, 767
    scary[11][24], dists[11][24] = 1, 717
    scary[11][12], dists[11][12] = 3, 396
    scary[12][25], dists[12][25] = 3, 684
    scary[13][14], dists[13][14] = 2, 516
    scary[13][16], dists[13][16] = 3, 444
    scary[14][20], dists[14][20] = 3, 947
    scary[15][17], dists[15][17] = 2, 533
    scary[15][18], dists[15][18] = 3, 362
    scary[16][19], dists[16][19] = 3, 557
    scary[16][20], dists[16][20] = 3, 742
    scary[17][22], dists[17][22] = 3, 937
    scary[17][18], dists[17][18] = 3, 360
    scary[18][23], dists[18][23] = 3, 600
    scary[19][20], dists[19][20] = 3, 493
    scary[20][21], dists[20][21] = 3, 406
    scary[21][22], dists[21][22] = 3, 322
    scary[22][23], dists[22][23] = 3, 523
    scary[23][24], dists[23][24] = 3, 406
    scary[24][25], dists[24][25] = 3, 379

    for i in range(Vn):
        for j in range(i, Vn):
            scary[j][i] = scary[i][j]
            dists[j][i] = dists[i][j]

    # initialize cost matrix
    for i in range(Vn):
        for j in range(Vn):
            costs[i][j] = sweights[scary[i][j] - 1]*dists[i][j]

    #costs = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
    #        [4, 0, 8, 0, 0, 0, 0, 11, 0],
    #        [0, 8, 0, 7, 0, 4, 0, 0, 2],
    #        [0, 0, 7, 0, 9, 14, 0, 0, 0],
    #        [0, 0, 0, 9, 0, 10, 0, 0, 0],
    #        [0, 0, 4, 14, 10, 0, 2, 0, 0],
    #        [0, 0, 0, 0, 0, 2, 0, 1, 6],
    #        [8, 11, 0, 0, 0, 0, 1, 0, 7],
    #        [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    popdens = [2, 2, 1, 2, 2, 2, 3, 3, 3, 3, 3, 2, 1, 3, 3, 3, 3, 3, 3, 2, 2, 1, 2, 2, 1, 1]
    loc = [[0, 4],
            [1, 4],
            [2, 4],
            [3, 4],
            [4, 3.7],
            [6, 3],
            [0, 3],
            [1, 3],
            [2, 3],
            [3, 2.5],
            [4, 2.5],
            [5, 1.5],
            [6, 1.5],
            [0, 2],
            [1.5, 2],
            [4, 2],
            [0, 1],
            [3, 1],
            [4, 1],
            [0, 0],
            [1.5, 0],
            [2.5, 0],
            [3, 0],
            [4, 0],
            [5, 0],
            [6, 0]]

    for i in range(Vn):
        paths = dijkstra(costs, i)

        for path in paths:
            for j in range(len(path) - 1):
                traffic[path[j]][path[j+1]] += popdens[path[j]] * popdens[path[j+1]]

    for i in range(Vn):
        for j in range(Vn):
            colmap[i][j] = costs[i][j]*traffic[i][j]

    mincol = minp(map(minp, colmap))
    maxcol = max(map(max, colmap))
    cmap = plt.cm.RdYlGn_r
    norm = col.Normalize(vmin = mincol, vmax = maxcol)

    for i in range(Vn):
        for j in range(i, Vn):
            if costs[i][j] > 0:
                weight = cmap(norm(colmap[i][j]))
                plt.plot([loc[i][0], loc[j][0]], [loc[i][1], loc[j][1]], color=weight, linewidth=4, marker='o')

    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.axis('equal')
    plt.show()
