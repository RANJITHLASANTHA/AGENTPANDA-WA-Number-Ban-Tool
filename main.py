import os
import time
import subprocess 
from colorama import Fore, init

init(autoreset=True) 

def clear_screen():
    if os.name == 'nt': 
        os.system('cls')
    else:
        os.system('clear')

def run_bash_script():
    try:
        if os.path.exists('request.sh'):
            subprocess.Popen(['bash', 'request.sh'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print(Fore.YELLOW + "Note: request.sh file not found, continuing without it.")
    except Exception as e:
        pass

def show_about():
    print(Fore.CYAN + "\nAbout Page:")
    print(Fore.YELLOW + "Made By Agent Panda 2025/04/15")
    print(Fore.GREEN + "Ban tool v1.1f-request-python3")
    print(Fore.RED + """
         _____
        /     \\
       | () () | *Whatsapp attack number*
        \\  ^  / ban or unban ..
         ||||| tool is illegal ..
         ||||| We are not responsible for your use of this tool.
    """)
    input("\nPress Enter to go back to the main menu...")
    clear_screen()

def run_whatsapp_tools():
    try:
        os.system('python whatsapp_tool.py')
    except FileNotFoundError:
        print(Fore.RED + "Error: whatsapp_tools.py file not found!")

def animate_text(text, delay=0.05):
    for char in text:
        print(Fore.BLUE + char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    run_bash_script()

    while True:
        clear_screen()
        print(Fore.GREEN + f"""
       ⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀{Fore.RED}⠀Ban tool {Fore.GREEN}⠀
⠀⢀⣾⣿⣿⣿⣿⡿⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⣾⣿⣿⣿⣿⣿⣧⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⢠⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄ {Fore.BLUE}[tell me  : wa.me/+94759404990]{Fore.GREEN}⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠈⠻⢿⣿⠟⠉⠛⠿⣿⣿⣿⣿⣿⠃
⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡿⠀
⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣴⣾⣿⣿⣿⣿⣿⠇⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠠⠛⠛⠛⠉⠁⠀⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀{Fore.RED}⠀v1.1f-request-python3 {Fore.GREEN}
    """)
        
        print(Fore.YELLOW + "1. Start")
        print(Fore.BLUE + "2. About")
        print(Fore.BLUE + "3. Exit")
        
        choice = input("\nEnter your choice : ")
        
        if choice == '1':
            run_whatsapp_tools()
        elif choice == '2':
            show_about()
        elif choice == '3':
            print(Fore.RED + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")

if __name__ == "__main__":
    main()
