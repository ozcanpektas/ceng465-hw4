# Ozcan Pektas 2237782

import sys

degree = dict()
adjacency_list = dict()

def readInput():
    file_name = sys.argv[1]
    graph = open(file_name, 'r')

    lines = graph.readlines()
    for line in lines:
        
        p1 = line.split("\t")[0]
        p2 = line.split("\t")[1]
        p2 = p2.rstrip()

        if p1 in adjacency_list:
            adjacency_list[p1][p2] = 1
            degree[p1] += 1

        else:
            adjacency_list[p1] = dict()
            adjacency_list[p1][p2] = 1
            degree[p1] = 1

        if p2 in adjacency_list:
            adjacency_list[p2][p1] = 1
            degree[p2] += 1

        else:
            adjacency_list[p2] = dict()
            adjacency_list[p2][p1] = 1
            degree[p2] = 1

def find_K_core():
    k = 1
    while len(adjacency_list):
        count = 0
        left = 1
        while left:
            left = 0
            for pro, D in degree.items():
                if D <= k:
                    count += 1
                    left = 1
                    degree[pro] = 99999
                    adjacency_list.pop(pro)
                    for n_pro, n_dict in adjacency_list.items():
                        if pro in n_dict:
                            n_dict.pop(pro)
                            degree[n_pro] -= 1

        if(count != 0):
            print(f"For k = {k} there are {count} proteins.")
        k += 1

if __name__ == '__main__':
    readInput()
    find_K_core()