import socket

def grab_banner(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, port))

        try:
            banner = sock.recv(1024).decode().strip()
            if banner:
                print(f"[+] Banner: {banner}")
            else:
                print("[-] No banner received.")
        except:
            print("[-] No banner received.")

        sock.close()

    except Exception as e:
        print(f"[-] Connection failed: {e}")


def main():
    print("=== Simple Banner Grabber ===\n")

    target = input("Enter target (IP or domain): ").strip()
    port_input = input("Enter port: ").strip()

    if not target or not port_input:
        print("[-] Missing input.")
        return

    try:
        port = int(port_input)
    except ValueError:
        print("[-] Invalid port.")
        return

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[-] Could not resolve target.")
        return

    print(f"\n[*] Connecting to {target} ({target_ip}) on port {port}...\n")

    grab_banner(target_ip, port)

    print("\n[*] Done.")


if __name__ == "__main__":
    main()