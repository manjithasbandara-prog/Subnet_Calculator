# Subnet Calculator

A small, zero-dependency Python CLI tool to calculate IPv4 subnet details from an IP/CIDR input.

Features
-
- Calculates network address and broadcast address
- Displays subnet mask and wildcard mask
- Shows CIDR prefix, total hosts and usable hosts
- Prints usable IP range (first and last usable addresses)
- Identifies IP class (A/B/C/D/E) and whether the network is private

Technology
-
- Python 3 standard library only (`ipaddress`, `sys`)
- No external dependencies

Usage
-
Run the script with an IP/CIDR argument, for example:

```bash
python subnet_calc.py 192.168.1.50/26
```

Or run without arguments to be prompted interactively:

```bash
python subnet_calc.py
# then enter: 10.0.0.5/24
```

Files
-
- `subnet_calc.py`: Main script and module exposing `calculate_subnet()`

License
-
This project is provided as-is. Add a LICENSE file if you'd like to set one.

Contributing
-
Open an issue or PR on the repository for feature requests or fixes.

