import subprocess

def check_suid_files():
    try:
        cmd = "find / -perm -4000 -type f 2>/dev/null"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        files = result.stdout.strip().split('\n') if result.stdout else []
        if len(files) == 0 or files == ['']:
            return "PASS: No SUID files found."
        else:
            return f"INFO: Found {len(files)} SUID files (listing top 5):\n  " + "\n  ".join(files[:5])
    except Exception as e:
        return f"ERROR: Exception during SUID files check - {e}"
