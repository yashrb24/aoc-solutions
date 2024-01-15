def dfs(rule_id):
    if rule_id == "R":
        return False
    elif rule_id == "A":
        return True
    
    for rule, node in graph[rule_id][:-1]:
        if eval(rule):
            return dfs(node)
        
    return dfs(graph[rule_id][-1][0])

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

        if dfs("in"):
            total += x + a + m + s


    print(total)

        


    return


def part2(data):
    pass


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
    part1(data)
    part2(data)