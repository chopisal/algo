
def find_computer(sub_index, computers, network):
    coms = computers[sub_index]
    for idx, val in enumerate(coms):
        if val == 1 and idx > sub_index:
            network.append(idx)
            find_computer(idx, computers, network)


def solution(n, computers):
    network_list = []
    for index, value in enumerate(computers):
        network = []
        isExist = False
        for ex in network_list:
            print("ex==>", ex)
            if index in ex:
                isExist = True
        if isExist:
            continue
        network.append(index)
        find_computer(index, computers, network)
        if len(network) > 0:
            network_list.append(network)

    print("network_list==>", network_list)
    return len(network_list)


print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]]))
