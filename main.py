from tasks_1 import get_max_value_node, get_min_value_node, get_sum_nodes_values, insert


if __name__ == '__main__':
    root = None
    keys = [8, 17, 28, 24, 26, 25, 3]

    print("Вставка ключів у AVL-дерево:")
    for key in keys:
        root = insert(root, key)
   
    print("AVL-Дерево:")
    print(root)

    print("Мінімальне значення у дереві:", get_min_value_node(root).key)

    print("Максимальне значення у дереві:", get_max_value_node(root).key)

    print("Сума всіх значень у дереві:", get_sum_nodes_values(root))
