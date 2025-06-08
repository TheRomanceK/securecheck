def check_ssh_root_login():
    try:
        with open('/etc/ssh/sshd_config', 'r') as f:
            lines = f.readlines()
    except Exception as e:
        return f"ERROR: Cannot read sshd_config - {e}"

    for line in lines:
        if line.strip().startswith('PermitRootLogin'):
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            value = parts[1].lower()
            if value == 'no':
                return "PASS: Root login via SSH is disabled."
            else:
                return f"FAIL: Root login via SSH is set to '{value}'."
    return "WARN: PermitRootLogin not set, default may allow root login."
