import subprocess

def check_firewall():
    # Check UFW status
    try:
        ufw_status = subprocess.run("ufw status", shell=True, capture_output=True, text=True)
        if ufw_status.returncode == 0:
            if "Status: active" in ufw_status.stdout:
                return "PASS: UFW firewall is active."
            else:
                # Try firewalld
                firewalld_status = subprocess.run("firewall-cmd --state", shell=True, capture_output=True, text=True)
                if firewalld_status.returncode == 0 and firewalld_status.stdout.strip() == "running":
                    return "PASS: firewalld is running."
                else:
                    return "FAIL: No active firewall detected (UFW/firewalld)."
        else:
            return "FAIL: Unable to determine firewall status."
    except Exception as e:
        return f"ERROR: Exception checking firewall - {e}"
