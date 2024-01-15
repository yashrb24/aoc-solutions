def dfs1(rule_id):
    if rule_id == "R":
        return False
    elif rule_id == "A":
        return True
    
    for rule, node in graph[rule_id][:-1]:
        if eval(rule):
            return dfs(node)
        
    return dfs(graph[rule_id][-1][0])


args_dict = {"x": 0, "a": 1, "m": 2, "s": 3}

def dfs2(rule_id, args_list):
    if rule_id == "R":
        return 0
    elif rule_id == "A":
        return len(args_list[0]) * len(args_list[1]) * len(args_list[2]) * len(args_list[3])
    
    answer = 0

    curr_lists = args_list.copy()
    for rule, node in graph[rule_id][:-1]:
        letter, operator, threshold = rule[0], rule[1], int(rule[2:])
        
        curr_list = curr_lists[args_dict[letter]].copy()
        curr_tmp_list = [x for x in curr_list if eval(f"{x} {operator} {threshold}")]
        curr_not_tmp_list = [x for x in curr_list if not eval(f"{x} {operator} {threshold}")]

        tmp1_list = curr_lists.copy()
        tmp1_list[args_dict[letter]] = curr_tmp_list
        answer += dfs2(node, tmp1_list)

        curr_lists[args_dict[letter]] = curr_not_tmp_list


    answer += dfs2(graph[rule_id][-1][0], curr_lists)
    return answer

graph = {}
def part1(data):

    last_idx = -1

    for i, line in enumerate(data):
        if line == '':
            last_idx = i
            break
        rule_id, edges = line.split('{') 
        edges = edges[:-1].split(',')
        edges = [edge.split(":") for edge in edges]

        graph[rule_id] = edges

    total = 0

    for j in range(last_idx+1, len(data)):
        curr = data[j][1:-1]
        curr = curr.split(',')
        for var_assgn in curr:
            exec(var_assgn, globals())

        if dfs1("in"):
            total += x + a + m + s


    print(total)

        


    return


def part2(data):
    for i, line in enumerate(data):
        if line == '':
            break
        rule_id, edges = line.split('{') 
        edges = edges[:-1].split(',')
        edges = [edge.split(":") for edge in edges]

        graph[rule_id] = edges

    x = list(range(1, 4001))
    a = list(range(1, 4001))
    m = list(range(1, 4001))
    s = list(range(1, 4001))
    args_list = [x, a, m, s]

    total = dfs2("in", args_list)
    print(total)

    return 

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
    # part1(data)
    # graph = {}
    part2(data)