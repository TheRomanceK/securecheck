from checks import (
    ssh_root,
    firewall,
    open_ports,
    password_policy,
    world_writable,
    suid_files,
    last_login
)

def main():
    print("Starting SecureCheck - Linux Security Baseline Checker\n")
    results = []
    results.append(ssh_root.check_ssh_root_login())
    results.append(firewall.check_firewall())
    results.append(open_ports.check_open_ports())
    results.append(password_policy.check_password_policy())
    results.append(world_writable.check_world_writable())
    results.append(suid_files.check_suid_files())
    results.append(last_login.check_inactive_users(days=30))

    for r in results:
        print(r)

if __name__ == "__main__":
    main()
