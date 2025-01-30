import subprocess
import whois
import sys

#Save the ouput to a file of your choice
def save_to_file(data):
    with open("scan_results.txt", "a") as f:  # "a" to append to the file instead of overwriting the file
        f.write(data + "\n")

#Scanning the target with Nmap, ouput in terminal and text file
def nmap_scan(target):
    print(f"Scanning {target} with Nmap...")
    save_to_file(f"Scanning {target} with Nmap...")
    result = subprocess.run(["nmap", "-A", "-T4", target], capture_output=True, text=True) #Adjust settings to Nmap as needed
    print(result.stdout)
    save_to_file(result.stdout)

#Whois lookup on the target, writes out error-msg if needed, output in the terminal and text file
def whois_lookup(target):
    print(f"Whois-run for {target}...")
    save_to_file(f"Whois-run for {target}...")
    try:
        domain_info = whois.whois(target)
        print(str(domain_info))
        save_to_file(str(domain_info))
    except Exception as e:
        error_msg = f"Error with Whois: {e}"
        print(error_msg)
        save_to_file(error_msg)

#Using Gobuster to look trough the target for directories, output in termminal and text file
def gobuster_scan(target):
    print(f"Looking through {target} with Gobuster...")
    save_to_file(f"Looking through {target} with Gobuster...")
    wordlist = "/usr/share/wordlists/dirb/common.txt"  # Adjust the wordlist if needed
    result = subprocess.run(["gobuster", "dir", "-u", target, "-w", wordlist], capture_output=True, text=True)
    print(result.stdout)
    save_to_file(result.stdout)

#Syntax for running this python script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use the following syntax: python3 scanning.py <ip or domain>")
        sys.exit(1)

    target = sys.argv[1]

    with open("scan_results.txt", "w") as f:  #Clean the file before a new run
        f.write(f"Scan results for {target}\n")
        f.write("="*50 + "\n")

    nmap_scan(target)
    whois_lookup(target)
    gobuster_scan(target)

