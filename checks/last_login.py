import subprocess

def check_inactive_users(days=30):
    try:
        result = subprocess.run(f"lastlog -b {days}", shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            return "FAIL: Could not run lastlog command."
        lines = result.stdout.strip().split('\n')
        inactive_users = []
        for line in lines[1:]:  # skip header
            if 'Never logged in' in line:
                user = line.split()[0]
                inactive_users.append(user)
        if len(inactive_users) == 0:
            return f"PASS: No users inactive for more than {days} days."
        else:
            return f"WARN: Users inactive for more than {days} days:\n  " + ", ".join(inactive_users)
    except Exception as e:
        return f"ERROR: Exception during last login check - {e}"
