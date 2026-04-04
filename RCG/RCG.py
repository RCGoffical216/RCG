import subprocess

# Utility to run scripts
def run_script(script_name):
    """Run a Python script in a new process."""
    try:
        subprocess.run(["python3", script_name])
    except FileNotFoundError:
        print(f"[-] Script {script_name} not found.")

# ------------------ Network Tools ------------------
def network_tools():
    while True:
        print("\n=== Network Tools ===")
        print("1. Network Scanner")
        print("2. Port Scanner")
        print("3. ARP Scanner")
        print("4. Ping Sweep")
        print("5. Traceroute")
        print("6. Banner Grabber")
        print("7. IP Info")
        print("8. DNS Lookup")
        print("9. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1": run_script("networkscanner.py")
        elif choice == "2": run_script("portscanner.py")
        elif choice == "3": run_script("arp_scanner.py")
        elif choice == "4": run_script("ping_sweep.py")
        elif choice == "5": run_script("traceroute.py")
        elif choice == "6": run_script("bannergrabber.py")
        elif choice == "7": run_script("ipinfo.py")
        elif choice == "8": run_script("dns.py")
        elif choice == "9": break
        else: print("[-] Invalid choice.")

# ------------------ Web Tools ------------------
def web_tools():
    while True:
        print("\n=== Web Tools ===")
        print("1. Subdomain Finder")
        print("2. Directory Finder")
        print("3. API Finder")
        print("4. Email Scraper")
        print("5. Link Extractor")
        print("6. Banner Grabber")
        print("7. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1": run_script("subfinder.py")
        elif choice == "2": run_script("directoryfinder.py")
        elif choice == "3": run_script("api_finder.py")
        elif choice == "4": run_script("emailscraper.py")
        elif choice == "5": run_script("linkextractor.py")
        elif choice == "6": run_script("bannergrabber.py")
        elif choice == "7": break
        else: print("[-] Invalid choice.")

# ------------------ Pentesting Tools ------------------
def pentesting_tools():
    while True:
        print("\n=== Pentesting Tools ===")
        print("1. SSH Weak Password Tester")
        print("2. FTP Anonymous Login Checker")
        print("3. CVE Checker")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1": run_script("ssh_weak_tester.py")
        elif choice == "2": run_script("ftp_anonymous.py")
        elif choice == "3": run_script("cve_checker.py")
        elif choice == "4": break
        else: print("[-] Invalid choice.")

# ------------------ Main Menu ------------------
def main():
    while True:
        print("\n=====================================")
        print("█████╗   ██████╗    ██████╗ ")
        print("██╔══██╗ ██╔═══      ██╔════╝ ")
        print("██████╔╝ ██║         ██║  ███╗")
        print("██╔══██╗ ██║         ██║  ██║")
        print("██║  ██║ ╚██████╔╝  ╚██████╔╝")
        print("╚═╝  ╚═╝  ╚═════╝    ╚══════╝")
        print("       Made by definitelynotaRussianspy V1")
        print("=====================================")
        print("1. Network Tools")
        print("2. Web Tools")
        print("3. Pentesting Tools")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1": network_tools()
        elif choice == "2": web_tools()
        elif choice == "3": pentesting_tools()
        elif choice == "4":
            print("Exiting RCG... Goodbye!")
            break
        else:
            print("[-] Invalid choice.")

if __name__ == "__main__":
    main()