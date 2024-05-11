SSimport matplotlib.pyplot as plt
import networkx as nx

# Classe para representar um nó na árvore binária
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Classe para representar a árvore binária
class BinaryTree:
    def __init__(self):
        self.root = None

    # Adiciona um nó na árvore binária
    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._add_recursive(node.right, value)

    # Função para obter a altura da árvore
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    # Função para obter as folhas da árvore
    def leaves(self):
        leaves = []
        self._leaves_recursive(self.root, leaves)
        return leaves

    def _leaves_recursive(self, node, leaves):
        if node is None:
            return
        if node.left is None and node.right is None:
            leaves.append(node.value)
        else:
            self._leaves_recursive(node.left, leaves)
            self._leaves_recursive(node.right, leaves)

    # Função para encontrar a profundidade de um nó específico
    def depth(self, value):
        return self._depth_recursive(self.root, value)

    def _depth_recursive(self, node, value):
        if node is None:
            return -1
        elif node.value == value:
            return 0
        elif value < node.value:
            depth = self._depth_recursive(node.left, value)
        else:
            depth = self._depth_recursive(node.right, value)
        if depth == -1:
            return -1
        return 1 + depth

    # Função para obter os ancestrais de um nó específico
    def ancestors(self, value):
        path = []
        self._ancestors_recursive(self.root, value, path)
        return path[::-1]  # Reverter para manter a ordem do topo para baixo

    def _ancestors_recursive(self, node, value, path):
        if node is None:
            return False
        if node.value == value:
            return True
        path.append(node.value)
        if (value < node.value and self._ancestors_recursive(node.left, value, path)) or (
            value >= node.value and self._ancestors_recursive(node.right, value, path)):
            return True
        path.pop()
        return False

    # Plotar a árvore binária usando networkx e matplotlib
    def plot(self):
        G = nx.DiGraph()
        self._plot_recursive(self.root, G)
        pos = self._get_tree_layout(G, self.root.value)
        plt.figure(figsize=(10, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=14)
        plt.show()

    def _plot_recursive(self, node, G):
        if node is None:
            return
        if node.left:
            G.add_edge(node.value, node.left.value)
            self._plot_recursive(node.left, G)
        if node.right:
            G.add_edge(node.value, node.right.value)
            self._plot_recursive(node.right, G)

    def _get_tree_layout(self, G, root_value):
        pos = {}
        self._assign_positions(G, root_value, pos, 0, 0, 1)
        return pos

    def _assign_positions(self, G, current, pos, x, y, level_spacing):
        pos[current] = (x, y)
        neighbors = list(G.neighbors(current))
        if len(neighbors) == 0:
            return
        if len(neighbors) == 2:
            left_child, right_child = neighbors
            self._assign_positions(G, left_child, pos, x - level_spacing, y - 1, level_spacing / 2)
            self._assign_positions(G, right_child, pos, x + level_spacing, y - 1, level_spacing / 2)
        elif len(neighbors) == 1:
            self._assign_positions(G, neighbors[0], pos, x, y - 1, level_spacing / 2)

# Criar uma árvore binária com valores
tree = BinaryTree()
tree.add(10)
tree.add(5)
tree.add(15)
tree.add(3)
tree.add(7)
tree.add(12)
tree.add(18)

# Plotar a árvore binária
tree.plot()

# Exibir algumas informações sobre a árvore
print("Raiz:", tree.root.value)
print("Altura:", tree.height())
print("Folhas:", tree.leaves())
print("Profundidade do nó 7:", tree.depth(7))
print("Ancestrais do nó 7:", tree.ancestors(7))
