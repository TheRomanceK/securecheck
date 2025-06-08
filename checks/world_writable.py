import subprocess

def check_world_writable():
    try:
        cmd = "find /etc /home -type f -perm -002 2>/dev/null"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        files = result.stdout.strip().split('\n') if result.stdout else []
        if len(files) == 0 or files == ['']:
            return "PASS: No world-writable files found in /etc or /home."
        else:
            return f"FAIL: World-writable files found:\n  " + "\n  ".join(files[:5]) + ("..." if len(files) > 5 else "")
    except Exception as e:
        return f"ERROR: Exception during world-writable files check - {e}"
