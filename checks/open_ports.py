import subprocess

def check_open_ports():
    try:
        result = subprocess.run("ss -tuln", shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            return "FAIL: Could not retrieve open ports."
        lines = result.stdout.strip().split('\n')[1:]  # skip header
        ports = []
        for line in lines:
            parts = line.split()
            # Typical output: Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port
            local_addr = parts[4]
            port = local_addr.split(':')[-1]
            ports.append(port)
        if ports:
            return f"INFO: Open ports detected: {', '.join(sorted(set(ports)))}"
        else:
            return "PASS: No open TCP/UDP ports detected."
    except Exception as e:
        return f"ERROR: Exception checking open ports - {e}"
