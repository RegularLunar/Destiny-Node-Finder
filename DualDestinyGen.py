def find_matching_nodes(nodes1, nodes2, num_nodes):
    matching_nodes = set(nodes1) & set(nodes2)
    if len(matching_nodes) >= num_nodes:
        return sorted(matching_nodes)[:num_nodes]
    else:
        return None

def find_non_matching_nodes(nodes1, nodes2, num_nodes):
    all_nodes = set(range(1, 10))
    used_nodes = set(nodes1) | set(nodes2)
    non_matching_nodes = sorted(all_nodes - used_nodes)
    return non_matching_nodes[:num_nodes]

def input_node_numbers(prompt, num_nodes):
    while True:
        try:
            nodes = list(map(int, input(prompt).strip().split()))
            if len(nodes) != num_nodes:
                print(f"Please input exactly {num_nodes} node numbers separated by spaces.")
            elif any(node < 1 or node > 9 for node in nodes):
                print("Node numbers must be between 1 and 9.")
            else:
                return nodes
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")

def main():
    print("Welcome to the node matching script!")

    while True:
        print("\nOptions:")
        print("1. 6 Nodes")
        print("2. 3 Nodes")
        print("0. Exit")

        choice = input("Select an option (1/2/0): ")

        if choice == '1':
            print("\n=== 6 Nodes ===")
            nodes1 = input_node_numbers("Input your 6 node numbers: ", 6)
            nodes2 = input_node_numbers("Input your partner's 6 node numbers: ", 6)

            matching_nodes = find_matching_nodes(nodes1, nodes2, 3)
            if matching_nodes:
                print(f"\nMatching 3 nodes: {matching_nodes}")
            else:
                print("\nNo 3 matching nodes found.")

        elif choice == '2':
            print("\n=== 3 Nodes ===")
            nodes1 = input_node_numbers("Input your 3 node numbers: ", 3)
            nodes2 = input_node_numbers("Input your partner's 3 node numbers: ", 3)

            non_matching_nodes = find_non_matching_nodes(nodes1, nodes2, 3)
            print(f"\nNon-matching 3 nodes: {non_matching_nodes}")

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 0.")

if __name__ == "__main__":
    main()
