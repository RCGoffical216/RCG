import requests
import socket

def get_ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data["status"] != "success":
            print("[-] Failed to retrieve IP info.")
            return

        print("\n=== IP Information ===\n")
        print(f"IP: {data.get('query')}")
        print(f"Country: {data.get('country')}")
        print(f"Region: {data.get('regionName')}")
        print(f"City: {data.get('city')}")
        print(f"ISP: {data.get('isp')}")
        print(f"Organization: {data.get('org')}")
        print(f"Timezone: {data.get('timezone')}")
        print(f"Latitude/Longitude: {data.get('lat')}, {data.get('lon')}")

    except Exception as e:
        print(f"[-] Error: {e}")


def main():
    print("=== IP Info Tool ===\n")

    target = input("Enter IP or domain: ").strip()

    if not target:
        print("[-] No input provided.")
        return

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[-] Could not resolve target.")
        return

    print(f"\n[*] Looking up: {target} ({ip})")

    get_ip_info(ip)


if __name__ == "__main__":
    main()