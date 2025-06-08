# securecheck
SecureCheck is a lightweight, modular Linux security baseline checker designed for IT professionals, sysadmins, and security enthusiasts. It performs essential security audits to quickly identify common configuration issues and potential vulnerabilities on Linux systems.


Project Structure
securecheck/
├── securecheck.py           # Main script to run all checks
├── checks/                  # Individual security check modules
│   ├── ssh_root.py
│   ├── firewall.py
│   ├── open_ports.py
│   ├── password_policy.py
│   ├── world_writable.py
│   ├── suid_files.py
│   └── last_login.py
├── README.md
└── .gitignore

USAGE
Run the main script: python3 securecheck.py
The tool will run a series of checks and output the results with PASS, FAIL, WARN, or INFO status.
