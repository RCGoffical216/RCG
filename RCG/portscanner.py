import socket
from concurrent.futures import ThreadPoolExecutor

# Common ports to scan
COMMON_PORTS = [
    21, 22, 23, 25, 53, 69, 80, 110, 119, 123,
    135, 137, 138, 139, 143, 161, 179, 389, 443,
    445, 465, 500, 587, 636, 993, 995, 1433,
    1521, 1723, 2049, 2082, 2083, 2181, 2222,
    2483, 2484, 3000, 3306, 3389, 3690, 4000,
    4444, 4567, 4664, 4711, 4712, 4899, 5000,
    5432, 5500, 5601, 5632, 5900, 5985, 6379,
    6667, 7001, 7002, 8000, 8008, 8009, 8080,
    8081, 8086, 8087, 8090, 8091, 8443, 8888,
    9000, 9042, 9090, 9200, 9418, 9999, 27017
]

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            print(f"[+] Port {port} is OPEN")
            return port
    except:
        pass
    return None


def main():
    print("=== Simple Port Scanner ===\n")

    target = input("Enter target (IP or domain): ").strip()

    if not target:
        print("[-] No target entered.")
        return

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[-] Could not resolve target.")
        return

    print(f"\n[*] Scanning target: {target} ({target_ip})")
    print("[*] Scanning common ports...\n")

    open_ports = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, target_ip, port) for port in COMMON_PORTS]

        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)

    print("\n[*] Scan complete!")

    if open_ports:
        print(f"[+] Open ports: {sorted(open_ports)}")
    else:
        print("[-] No open ports found.")


if __name__ == "__main__":
    main()