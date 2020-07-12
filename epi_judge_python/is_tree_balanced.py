from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeigh', ('balanced', 'height'))

    def check_balandced(tree: BinaryTreeNode):
        if not tree:
            return BalancedStatusWithHeight(True, -1)
        left_result = check_balandced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        right_result = check_balandced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        is_balanced = abs(left_result.height-right_result.height) <= 1
        height = max(left_result.height, right_result.height)+1
        return BalancedStatusWithHeight(is_balanced, height)
    return check_balandced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
