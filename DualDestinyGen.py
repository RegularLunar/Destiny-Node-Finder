import os
import colorama
import time
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
ascii_art = """
          _____                  _            _                            
    ____ |  __ \                | |          | |                           
   / __ \| |__) |___  __ _ _   _| | __ _ _ __| |    _   _ _ __   __ _ _ __ 
  / / _` |  _  // _ \/ _` | | | | |/ _` | '__| |   | | | | '_ \ / _` | '__|
 | | (_| | | \ \  __/ (_| | |_| | | (_| | |  | |___| |_| | | | | (_| | |   
  \ \__,_|_|  \_\___|\__, |\__,_|_|\__,_|_|  |______\__,_|_| |_|\__,_|_|   
   \____/             __/ |                                                
                     |___/                           discord.gg/mFAxKpT457                     
    """


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


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
                print(
                    f"{Style.BRIGHT}{Fore.RED}Error: Please input exactly {num_nodes} node numbers separated by spaces.")
            elif any(node < 1 or node > 9 for node in nodes):
                print(f"{Style.BRIGHT}{Fore.RED}Error: Node numbers must be between 1 and 9.")
            else:
                return nodes
        except ValueError:
            print(f"{Style.BRIGHT}{Fore.RED}Error: Please enter numbers separated by spaces.")


def main():
    while True:
        clear_screen()
        print(Fore.MAGENTA + ascii_art)
        print(f"{Style.BRIGHT}{Fore.YELLOW}\n=== Welcome to the Node Finder Tool ===")
        print(f"{Style.BRIGHT}{Fore.BLUE}\nOptions:")
        print(f"{Style.BRIGHT}{Fore.GREEN}1. 6 Nodes")
        print(f"{Style.BRIGHT}{Fore.GREEN}2. 3 Nodes")
        print(f"{Style.BRIGHT}{Fore.RED}0. Exit")

        choice = input(f"{Style.BRIGHT}{Fore.CYAN}Select an option (1/2/0): ")

        # Matching
        if choice == '1':
            for _ in range(3):
                clear_screen()
                print(f"{Style.BRIGHT}{Fore.YELLOW}\n=== 6 Nodes ===")
                nodes1 = input_node_numbers(f"{Fore.CYAN}Input your 6 node numbers: ", 6)
                clear_screen()
                nodes2 = input_node_numbers(f"{Fore.CYAN}Input your partner's 6 node numbers: ", 6)
                clear_screen()
                matching_nodes = find_matching_nodes(nodes1, nodes2, 3)
                if matching_nodes:
                    print(f"{Style.BRIGHT}{Fore.CYAN}Shoot these nodes:{Fore.RESET} {Fore.GREEN}{matching_nodes}")
                else:
                    print(f"{Style.BRIGHT}{Fore.RED}Error: \nNo matching nodes found.")

                input(f"{Style.DIM}{Fore.LIGHTBLACK_EX}\nPress Enter to continue...")

        # Non Matching
        elif choice == '2':
            for _ in range(3):
                clear_screen()
                print(f"{Style.BRIGHT}{Fore.YELLOW}\n=== 3 Nodes ===")
                nodes1 = input_node_numbers(f"{Fore.CYAN}Input your 3 node numbers: ", 3)
                clear_screen()
                nodes2 = input_node_numbers(f"{Fore.CYAN}Input your partner's 3 node numbers: ", 3)
                clear_screen()
                non_matching_nodes = find_non_matching_nodes(nodes1, nodes2, 3)
                print(f"{Style.BRIGHT}{Fore.CYAN}Shoot these nodes:{Fore.RESET} {Fore.GREEN}{non_matching_nodes}")

                input(f"{Style.DIM}{Fore.LIGHTBLACK_EX}\nPress Enter to continue...")

        elif choice == '0':
            clear_screen()
            print(f"{Style.BRIGHT}{Fore.YELLOW}Thank you for using my tool. {Fore.RESET}{Fore.CYAN}See you later! :) {Fore.RESET}{Fore.RED}Exiting...")
            time.sleep(1)
            break

        else:
            print(f"{Style.BRIGHT}{Fore.RED}Error: Invalid choice. Please select 1, 2, or 0.")
        clear_screen()


if __name__ == "__main__":
    main()
