def check_password_policy():
    try:
        with open('/etc/login.defs', 'r') as f:
            lines = f.readlines()
    except Exception as e:
        return f"ERROR: Cannot read /etc/login.defs - {e}"

    max_days = None
    for line in lines:
        if line.strip().startswith('PASS_MAX_DAYS'):
            parts = line.strip().split()
            if len(parts) >= 2:
                try:
                    max_days = int(parts[1])
                except ValueError:
                    continue
    if max_days is None:
        return "WARN: PASS_MAX_DAYS not set in /etc/login.defs."
    elif max_days <= 90:
        return f"PASS: Password maximum age is {max_days} days."
    else:
        return f"FAIL: Password maximum age is {max_days} days, which is too long."
