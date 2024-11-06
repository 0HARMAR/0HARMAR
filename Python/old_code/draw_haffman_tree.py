import matplotlib.pyplot as plt
import networkx as nx


class TreeNode:
    def __init__(self, key, name, is_leaf):
        self.left = None
        self.right = None
        self.val = key
        self.name = name
        self.is_leaf = is_leaf


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val, root_name, is_leaf = preorder[0]
    root_index = inorder.index((root_val, root_name, is_leaf))

    root = TreeNode(root_val, root_name, is_leaf)

    root.left = build_tree(preorder[1:1 + root_index], inorder[:root_index])
    root.right = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root


def add_edges(G, node, pos, x=0, y=0, layer=1):
    if node is not None:
        node_id = f"{node.val}{node.name}"
        G.add_node(node_id, pos=(x, y), label=f"{node.val} {node.name}")
        pos[node_id] = (x, y)

        if node.left:
            left_id = f"{node.left.val}{node.left.name}"
            G.add_edge(node_id, left_id)
            l = x - 2 / layer  # Increase the gap between children
            while any(abs(pos[child][0] - l) < 0.1 for child in pos):
                l -= 0.1
            add_edges(G, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            right_id = f"{node.right.val}{node.right.name}"
            G.add_edge(node_id, right_id)
            r = x + 2 / layer  # Increase the gap between children
            while any(abs(pos[child][0] - r) < 0.1 for child in pos):
                r += 0.1
            add_edges(G, node.right, pos, x=r, y=y - 1, layer=layer + 1)


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
    return pos


def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)

    children = list(G.neighbors(root))
    if not isinstance(G, nx.DiGraph) and parent is not None:
        children.remove(parent)

    if len(children) != 0:
        dx = width / len(children)
        nextx = xcenter - width / 2 - dx / 2
        for child in children:
            nextx += dx
            pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                 pos=pos, parent=root, parsed=parsed)

    return pos


def draw_huffman_tree(preorder, inorder):
    root = build_tree(preorder, inorder)
    G = nx.DiGraph()
    pos = {}
    add_edges(G, root, pos)

    root_id = f"{root.val}{root.name}"
    pos = hierarchy_pos(G, root=root_id)
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(15, 10))
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=500, node_color="lightblue", font_size=8,
            font_weight="bold", arrowsize=10)
    plt.title("Huffman Tree")
    plt.show()


# 提供的先序和中序遍历结果
preorder = [(814, '#', False), (347, '#', False), (156, '#', False), (76, '#', False), (35, '#', False),
            (17, '#', False),
            (8, 'V', True), (9, '#', False), (4, '#', False), (2, '#', False), (1, 'X', True), (1, 'Z', True),
            (2, '#', False), (1, 'J', True), (1, 'Q', True), (5, 'K', True), (18, 'W', True), (41, '#', False),
            (20, 'M', True), (21, 'F', True), (80, 'T', True), (191, '#', False), (92, '#', False), (45, '#', False),
            (22, 'C', True), (23, 'U', True), (47, 'H', True), (99, '#', False), (48, 'R', True), (51, 'S', True),
            (467, '#', False), (217, '#', False), (103, 'E', True), (114, '#', False), (57, 'N', True), (57, 'I', True),
            (250, '#', False), (122, '#', False), (59, '#', False), (28, '#', False), (13, 'B', True), (15, 'P', True),
            (31, '#', False), (15, 'G', True), (16, 'Y', True), (63, 'O', True), (128, '#', False), (64, '#', False),
            (32, 'L', True), (32, 'D', True), (64, 'A', True)]

inorder = [(8, 'V', True), (17, '#', False), (1, 'X', True), (2, '#', False), (1, 'Z', True), (4, '#', False),
           (1, 'J', True), (2, '#', False), (1, 'Q', True), (9, '#', False), (5, 'K', True), (35, '#', False),
           (18, 'W', True), (76, '#', False), (20, 'M', True), (41, '#', False), (21, 'F', True), (156, '#', False),
           (80, 'T', True), (347, '#', False), (22, 'C', True), (45, '#', False), (23, 'U', True), (92, '#', False),
           (47, 'H', True), (191, '#', False), (48, 'R', True), (99, '#', False), (51, 'S', True), (814, '#', False),
           (103, 'E', True), (217, '#', False), (57, 'N', True), (114, '#', False), (57, 'I', True), (467, '#', False),
           (13, 'B', True), (28, '#', False), (15, 'P', True), (59, '#', False), (15, 'G', True), (31, '#', False),
           (16, 'Y', True), (122, '#', False), (63, 'O', True), (250, '#', False), (32, 'L', True), (64, '#', False),
           (32, 'D', True), (128, '#', False), (64, 'A', True)]

draw_huffman_tree(preorder, inorder)
