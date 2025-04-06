![image](https://github.com/user-attachments/assets/870ef65c-0e06-4388-b891-7be04b09d627)

Search the world's largest dataset of leaked passwords

In February 2021, a colossal collection of compromised credentials, known as COMB (short for Combination Of Many Breaches), was made publicly accessible. This unprecedented leak consisted of more than 3.2 billion records, including emails, usernames, and passwords gathered from numerous past breaches involving platforms like Netflix, LinkedIn, and several others. The goal of this tool is to simplify the process of searching through this extensive archive of exposed login details, helping individuals determine if their accounts have been compromised and promoting stronger cybersecurity habits.

**This simple Python script utilizes https://www.proxynova.com/tools/comb to query and retrieve leaked passwords.
It is designed for responsible use only — the intended purpose is to run this tool from the terminal to check whether your credentials have been exposed in data breaches.**

## 🚀 Usage

You can run this script using:

```bash
python pwned.py
python pwned.py QUERY -s

QUERY is the username or password you want to search for.

The -s flag enables saving — it will store any discovered credentials in a .txt file located at /tmp/pwned/.
