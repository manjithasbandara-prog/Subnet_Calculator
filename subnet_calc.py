"""Subnet calculator CLI.

This is the runnable subnet calculator — helper functions are module-level
so it works both as a script and as an importable module.
"""

import ipaddress
import sys


def get_usable_range(network):
    """Get the first and last usable IP in the network."""
    all_hosts = list(network.hosts())
    if len(all_hosts) == 0:
        return "N/A (point-to-point or too small)"
    return f"{all_hosts[0]} - {all_hosts[-1]}"


def get_ip_class(ip):
    """Determine the IP class."""
    first_octet = int(str(ip).split('.')[0])
    if first_octet <= 126:
        return "Class A"
    elif first_octet <= 191:
        return "Class B"
    elif first_octet <= 223:
        return "Class C"
    elif first_octet <= 239:
        return "Class D (Multicast)"
    else:
        return "Class E (Reserved)"


def calculate_subnet(ip_cidr):
    """Calculate all subnet details from an IP/CIDR input."""

    try:
        network = ipaddress.ip_network(ip_cidr, strict=False)

        results = {
            "Input":            ip_cidr,
            "Network Address":  str(network.network_address),
            "Broadcast Address": str(network.broadcast_address),
            "Subnet Mask":      str(network.netmask),
            "Wildcard Mask":    str(network.hostmask),
            "CIDR Prefix":      f"/{network.prefixlen}",
            "Total Hosts":      network.num_addresses,
            "Usable Hosts":     max(network.num_addresses - 2, 0),
            "Usable IP Range":  get_usable_range(network),
            "IP Class":         get_ip_class(network.network_address),
            "Is Private":       network.network_address.is_private,
        }

        return results
    except ValueError as e:
        return {"Error": str(e)}


def display_results(results):
    """Pretty print the results."""
    print("\n" + "=" * 50)
    print("   🌐 SUBNET CALCULATOR RESULTS")
    print("=" * 50)

    for key, value in results.items():
        print(f"  {key:<20}: {value}")

    print("=" * 50 + "\n")


def main():
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input("Enter IP/CIDR (e.g., 192.168.1.50/26): ").strip()

    results = calculate_subnet(user_input)
    display_results(results)


if __name__ == "__main__":
    main()
