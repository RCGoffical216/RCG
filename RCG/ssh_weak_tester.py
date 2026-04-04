import paramiko
import socket

def ssh_test(target, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target, port=port, username=username, password=password, timeout=3)
        print(f"[+] SUCCESS: {username}:{password}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        return False
    except (paramiko.SSHException, socket.error):
        return None

def main():
    print("=== SSH Weak Password Tester (Lab Only) ===\n")
    target = input("Target IP: ").strip()
    port = input("Port (default 22): ").strip()
    port = int(port) if port else 22
    username = input("Username: ").strip()
    passwords = input("Passwords (comma-separated): ").strip().split(",")

    for pwd in passwords:
        pwd = pwd.strip()
        result = ssh_test(target, port, username, pwd)
        if result:
            print(f"[!] Weak password found: {pwd}")
            break
        elif result is None:
            print(f"[-] Connection failed for {pwd}")
        else:
            print(f"[-] {pwd} did not work")

    print("\nTesting complete.")

if __name__ == "__main__":
    main()