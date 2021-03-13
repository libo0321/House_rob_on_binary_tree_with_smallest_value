import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


m, n = map(int, input().split(' '))
nodes = list(map(lambda x: TreeNode(int(x)), input().split(' ')))
connection = []
for _ in range(n):
    connection.append(list(map(int, input().split(' '))))

# 重建二叉树
tree_root = nodes[0]
for row in range(len(connection)):
    if not nodes[connection[row][0] - 1].left:
        nodes[connection[row][0] - 1].left = nodes[connection[row][1] - 1]
    else:
        nodes[connection[row][0] - 1].right = nodes[connection[row][1] - 1]


def rob(root):
    if not root:
        return 0, 0, 50000, 50000  # 偷，不偷

    left = rob(root.left)
    right = rob(root.right)
    # 偷当前节点, 则左右子树都不能偷
    v1 = root.val + left[1] + right[1]
    min1 = min(root.val, left[3], right[3])
    # 不偷当前节点, 则取左右子树中最大的值
    v2 = max(left[0], left[1]) + max(right[0], right[1])
    min2 = min(left[2], right[2])

    # if v1 == v2:
    #     min1 = max(min1, min2)
    #     min2 = min1
    # print((v1, v2, min1, min2))
    return v1, v2, min1, min2


head_result = rob(tree_root)
if head_result[0] == head_result[1]:
    min_value = max(head_result[2], head_result[3])
    sys.stdout.write(str(head_result[0]) + ' ' + str(min_value))

else:
    max_sum_value = max(head_result[0], head_result[1])
    if max_sum_value == head_result[0]:
        min_value = head_result[2]
    else:
        min_value = head_result[3]
    sys.stdout.write(str(max_sum_value) + ' ' + str(min_value))
