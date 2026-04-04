import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def scan_ip(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        # Try common port (80) to check if host is alive
        result = sock.connect_ex((str(ip), 80))
        sock.close()

        if result == 0:
            try:
                hostname = socket.gethostbyaddr(str(ip))[0]
            except:
                hostname = "Unknown"

            print(f"[+] {ip} is UP ({hostname})")
            return str(ip)

    except:
        pass

    return None


def main():
    print("=== Network Scanner ===\n")

    network = input("Enter network (e.g. 192.168.1.0/24): ").strip()

    if not network:
        print("[-] No network entered.")
        return

    try:
        net = ipaddress.ip_network(network, strict=False)
    except ValueError:
        print("[-] Invalid network format.")
        return

    print(f"\n[*] Scanning network: {network}\n")

    active_hosts = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_ip, ip) for ip in net.hosts()]

        for future in futures:
            result = future.result()
            if result:
                active_hosts.append(result)

    print("\n[*] Scan complete!")

    if active_hosts:
        print(f"[+] Active devices: {len(active_hosts)}")
    else:
        print("[-] No active devices found.")


if __name__ == "__main__":
    main()