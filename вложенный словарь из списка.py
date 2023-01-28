a = list(map(int, input().split()))
tree_dict = a[-1]
print(tree_dict)

for key in reversed(a[:-1]):
    print(key)
    tree_dict = {key: tree_dict}
    print(tree_dict)
# print(tree_dict)
