def lca(root, v1, v2):
    max_val = max(v1, v2)
    min_val = min(v1, v2)

    def has_both_child(node):
        if node.info < min_val:
            return has_both_child(node.right)
        elif node.info > max_val:
            return has_both_child(node.left)
        return node.info

    return has_both_child(root)
