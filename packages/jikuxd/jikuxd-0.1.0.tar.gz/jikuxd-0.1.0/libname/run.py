import os
import time
import subprocess

# Install necessary packages if not already installed
try:
    import requests
except ImportError:
    print("\033[34mRequests installing...\033[0m")
    subprocess.check_call(["pip", "install", "requests"])

try:
    from rich.progress import track
except ImportError:
    print("Rich installing...")
    subprocess.check_call(["pip", "install", "rich"])
    from rich.progress import track

logo = """
\033[1;31m     ██ ██ ██   ██ ██    ██ 
\033[33m     ██ ██ ██  ██  ██    ██ 
\033[1;33m     ██ ██ █████   ██    ██ 
\033[1;31m██   ██ ██ ██  ██  ██    ██ 
\033[35m █████  ██ ██   ██  ██████         
"""

def main():
    os.system("clear")

    def working(pro="</>"):
        for _ in track(range(500), description=pro):
            time.sleep(0.002)

    def tool():
        print("========================================================")
        print(logo)
        print("========================================================")
        print("[1] Casino_clone")
        print("[2] flask-app")
        print("[3] FB_DUMP")
        print("[4] text_enc")
        print("[5] fb_auto")
        a = input("CHOICE: ").strip().lower()

        if a == "1":
            os.system("git clone https://github.com/phinerx/Casino_clone")
            os.system("cd Casino_clone && python main.py")

        elif a == "2":
            subprocess.Popen(["xdg-open", "https://github.com/phinerx/flask-app"])

        elif a == "3":
            os.system("git clone https://github.com/phinerx/FB_DUMP")
            os.system("cd FB_DUMP && python main.py")

        elif a == "4":
            subprocess.Popen(["xdg-open", "https://github.com/phinerx/text_enc"])

        elif a == "5":
            os.system("git clone https://github.com/phinerx/fb_auto")
            os.system("cd fb_auto && python fb_auto_enc.py")

        else:
            print("Invalid choice!")

    def admin():
        print("========================================================")
        print(logo)
        print("========================================================")
        time.sleep(1)
        admin_info = [
            "Hi, I am Jakaria\n",
            "You can call me Jiku\n",
            "I am a simple Coder\n",
            "My Lifeline is Suha\n",
            "You can call her S7HA\nHer old name was Sneha\nSo if you love me I will love you\nThat is my rule\n"
        ]
        for line in admin_info:
            print(line)
            time.sleep(0.1)

    def social():
        print("========================================================")
        print(logo)
        print("========================================================")
        print("[A] Facebook")
        print("[B] Instagram")
        print("[C] Telegram")
        social_input = input("CHOICE: ").strip().lower()

        if social_input == "a":
            subprocess.Popen(["xdg-open", "https://www.facebook.com/mdjakaria.fiad"])

        elif social_input == "b":
            subprocess.Popen(["xdg-open", "https://www.instagram.com/jiku__81/"])

        elif social_input == "c":
            subprocess.Popen(["xdg-open", "https://t.me/@phiner7x"])

        else:
            print("Invalid choice!")

    print("========================================================")
    print(logo)
    print("========================================================")
    print("[A] Tool")
    print("[B] Admin Info")
    print("[C] Social Media")
    print("[D] Website")
    print("[X] Exit")
    user = input("CHOICE: ").strip().lower()

    if user == "a":
        working()
        os.system("clear")
        tool()

    elif user == "b":
        working()
        os.system("clear")
        admin()

    elif user == "c":
        working()
        os.system("clear")
        social()

    elif user == "d":
        working()
        os.system("clear")
        subprocess.Popen(["xdg-open", "http://jikubro.great-site.net/?i=1"])

    elif user == "x":
        exit()

    else:
        print("Invalid choice!")

main()
