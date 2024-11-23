parent = {}
height = {}


def main():
    n = int(input())
    for i in range(n-1):
        child, ancestor = input().split()
        parent[child] = ancestor

    all_people = set(parent.keys()) | set(parent.values())
    root = all_people - set(parent.keys())
    height[root.pop()] = 0

    for i in all_people:
        compute_height(i)

    for i in sorted(all_people):
        print(i, height[i])


def compute_height(name):
    if name not in height:
        height[name] = compute_height(parent[name]) + 1
    return height[name]


main()