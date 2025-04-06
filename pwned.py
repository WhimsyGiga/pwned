import pyfiglet
from colorama import init
from termcolor import colored
from datetime import datetime
import sys
import os
import requests

init()

os.system('cls' if os.name == 'nt' else 'clear')

text = "PWNED"

ascii_art = pyfiglet.figlet_format(text)

rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

def rainbow_print(text):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        color = rainbow_colors[i % len(rainbow_colors)]
        print(colored(line, color))

rainbow_print(ascii_art)
print("------------------------------------------------------")
print("Search the world's largest dataset of leaked passwords")
print("------------------------------------------------------\n")

if len(sys.argv) > 1:
    user_input = sys.argv[1]
else:
    user_input = input("Enter your query: ")
    print("------------------------------------------------------\n")

url = "https://api.proxynova.com/comb"
params = {
    "query": user_input,
    "start": 0,
    "limit": 100
}

response = requests.get(url, params=params)
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = f"/tmp/pwned/{current_time}.log"
os.makedirs("/tmp/pwned", exist_ok=True)
credentials = [""]

if response.status_code == 200:
    data = response.json()

    combos = data.get('lines', [])

    if not combos:
        print("No results found.")
    else:
        for idx, combo in enumerate(combos, 1):
            print(f"[{idx}] {combo}")
            if len(sys.argv) > 2 and sys.argv[2] == "-s":
                credentials.append(combo)
else:
    print(f"Request failed with status code {response.status_code}")

if len(sys.argv) > 2 and sys.argv[2] == "-s":
    with open(file_path, "w") as file:
        for item in credentials:
            file.write(f"{item}\n")

if len(sys.argv) > 2 and sys.argv[2] == "-s":
    print(f"\nCredentials written to {file_path}")
