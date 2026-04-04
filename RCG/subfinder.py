import requests

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subdomains = set()

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("[-] Failed to fetch data.")
            return subdomains

        data = response.json()

        for entry in data:
            names = entry.get("name_value", "")
            for name in names.split("\n"):
                if domain in name:
                    subdomains.add(name.strip())

    except Exception as e:
        print(f"[-] Error: {e}")

    return subdomains


def main():
    print("=== Simple Subdomain Finder ===\n")
    
    domain = input("Enter target domain (e.g. example.com): ").strip()

    if not domain:
        print("[-] No domain entered.")
        return

    print(f"\n[*] Finding subdomains for: {domain}...\n")

    subs = get_subdomains(domain)

    if not subs:
        print("[-] No subdomains found.")
        return

    for sub in sorted(subs):
        print(f"[+] {sub}")

    print(f"\n[*] Total found: {len(subs)}")


if __name__ == "__main__":
    main()