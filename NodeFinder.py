import os
import time
from pystyle import Colors, Colorate, Center

# Regular Colors
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"

# Bold
bold_black = "\033[1;30m"
bold_red = "\033[1;31m"
bold_green = "\033[1;32m"
bold_yellow = "\033[1;33m"
bold_blue = "\033[1;34m"
bold_purple = "\033[1;35m"
bold_cyan = "\033[1;36m"
bold_white = "\033[1;37m"

# Underline
underline_black = "\033[4;30m"
underline_red = "\033[4;31m"
underline_green = "\033[4;32m"
underline_yellow = "\033[4;33m"
underline_blue = "\033[4;34m"
underline_purple = "\033[4;35m"
underline_cyan = "\033[4;36m"
underline_white = "\033[4;37m"

# Background
bg_black = "\033[40m"
bg_red = "\033[41m"
bg_green = "\033[42m"
bg_yellow = "\033[43m"
bg_blue = "\033[44m"
bg_purple = "\033[45m"
bg_cyan = "\033[46m"
bg_white = "\033[47m"

# High Intensity
hi_black = "\033[0;90m"
hi_red = "\033[0;91m"
hi_green = "\033[0;92m"
hi_yellow = "\033[0;93m"
hi_blue = "\033[0;94m"
hi_purple = "\033[0;95m"
hi_cyan = "\033[0;96m"
hi_white = "\033[0;97m"

# Bold High Intensity
bold_hi_black = "\033[1;90m"
bold_hi_red = "\033[1;91m"
bold_hi_green = "\033[1;92m"
bold_hi_yellow = "\033[1;93m"
bold_hi_blue = "\033[1;94m"
bold_hi_purple = "\033[1;95m"
bold_hi_cyan = "\033[1;96m"
bold_hi_white = "\033[1;97m"

# High Intensity Backgrounds
bg_hi_black = "\033[0;100m"
bg_hi_red = "\033[0;101m"
bg_hi_green = "\033[0;102m"
bg_hi_yellow = "\033[0;103m"
bg_hi_blue = "\033[0;104m"
bg_hi_purple = "\033[0;105m"
bg_hi_cyan = "\033[0;106m"
bg_hi_white = "\033[0;107m"

# Reset
reset = "\033[0m"

os.system("title Node Finder")

print_logo = """
         _____                  _            _                            
   ____ |  __ \                | |          | |                           
  / __ \| |__) |___  __ _ _   _| | __ _ _ __| |    _   _ _ __   __ _ _ __ 
 / / _` |  _  // _ \/ _` | | | | |/ _` | '__| |   | | | | '_ \ / _` | '__|
| | (_| | | \ \  __/ (_| | |_| | | (_| | |  | |___| |_| | | | | (_| | |   
 \ \__,_|_|  \_\___|\__, |\__,_|_|\__,_|_|  |______\__,_|_| |_|\__,_|_|   
  \____/             __/ |                                                
                    |___/                  https://regularlunar.pages.dev                     
"""

logo = Center.XCenter(print_logo)

def print_logo():
    print(Colorate.Horizontal(Colors.red_to_purple, logo, 1))


def six_nodes(nodes1, nodes2, num_nodes):
    matching_nodes = set(nodes1) & set(nodes2)
    return sorted(matching_nodes)[:num_nodes] if len(matching_nodes) >= num_nodes else None

def three_nodes_func(nodes1, nodes2, num_nodes):
    all_nodes = set(range(1, 10))
    used_nodes = set(nodes1) | set(nodes2)
    non_matching_nodes = sorted(all_nodes - used_nodes)
    return non_matching_nodes[:num_nodes]

def input_node_numbers(prompt, num_nodes):
    while True:
        try:
            nodes = list(map(int, input(prompt).strip().split()))
            if len(nodes) != num_nodes:
                os.system('cls')
                print(f"{hi_red}Error: Please input exactly {num_nodes} node numbers separated by spaces.{reset}")
            elif any(node < 1 or node > 9 for node in nodes):
                os.system('cls')
                print(f"{hi_red}Error: Node numbers must be between 1 and 9.{reset}")
            else:
                return nodes
        except ValueError:
            os.system('cls')
            print(f"{hi_red}Error: Please enter numbers separated by spaces.{reset}")
        os.system("pause")
        os.system('cls')

def choice():
    while True:
        os.system('cls')
        print_logo()
        print(f"{hi_green}\n=== Welcome to the Node Finder Tool ===")
        print(f"{hi_green}\nOptions:")
        print(f"{hi_purple}[ 1. ]{hi_white} 6 Nodes Method")
        print(f"{hi_cyan}[ 2. ]{hi_white} 3 Nodes Method")
        print(f"{bold_hi_red}[ 0. ] Exit ")
        user_choice = input(f"{yellow}[ >> ]{reset} ")

        if user_choice == '1':
            for _ in range(3):
                os.system('cls')
                print(Center.XCenter(f"{hi_purple}-- 6 Nodes --{reset}"))
                nodes1 = input_node_numbers(f"{hi_purple}Input your 6 node numbers: {reset}", 6)
                os.system('cls')
                print(Center.XCenter(f"{hi_purple}-- 6 Nodes --{reset}"))
                nodes2 = input_node_numbers(f"{hi_purple}Input your partner's 6 node numbers: {reset}", 6)
                os.system('cls')
                matching_nodes = six_nodes(nodes1, nodes2, 3)
                if matching_nodes:
                    print(Center.XCenter(f"{hi_purple}-- 6 Nodes --{reset}"))
                    print(f"{hi_purple}Shoot these nodes:{reset} {bold_green}{matching_nodes}{reset}")
                else:
                    os.system('cls')
                    print(Center.XCenter(f"{hi_red}Error: No matching nodes found.{reset}"))
                os.system("pause")

        elif user_choice == '2':
            for _ in range(3):
                os.system('cls')
                print(Center.XCenter(f"{hi_cyan}-- 3 Nodes --{reset}"))
                nodes1 = input_node_numbers(f"{hi_cyan}Input your 3 unlit Node numbers: {reset}", 3)
                os.system('cls')
                print(Center.XCenter(f"{hi_cyan}-- 3 Nodes --{reset}"))
                nodes2 = input_node_numbers(f"{hi_cyan}Input your partner's 3 unlit node numbers: {reset}", 3)
                os.system('cls')
                non_matching_nodes = three_nodes_func(nodes1, nodes2, 3)
                if non_matching_nodes:
                    print(Center.XCenter(f"{hi_cyan}-- 3 Nodes --{reset}"))
                    print(f"{hi_cyan}Shoot these nodes:{reset} {bold_green}{non_matching_nodes}{reset}")
                else:
                    os.system('cls')
                    print(Center.XCenter(f"{hi_red}Error: Matching nodes found.{reset}"))
                os.system("pause")

        elif user_choice == '0':
            os.system('cls')
            print(Center.XCenter(f"{hi_purple}Thank you for using my tool. Tell your friend's about me! :) Exiting..."))
            time.sleep(1)
            break

        else:
            os.system('cls')
            print(f"{hi_red}Error: Invalid choice. Please select 1, 2, or 0.{reset}")
            os.system("pause")
            os.system('cls')

if __name__ == "__main__":
    choice()
