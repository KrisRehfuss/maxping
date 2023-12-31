import subprocess

ip_addresses = [
    "10.47.9.159",
    "10.47.9.158",
    "10.47.9.157",
    "10.47.9.156",
    "10.47.9.154",
    "10.47.9.151",
    "10.47.9.147",
    "10.47.9.144",
    "10.47.9.142",
    "10.47.9.136",
    "10.47.9.129",
    "10.47.6.79",
    "10.47.6.78",
    "10.47.6.77",
    "10.47.6.72",
    "10.47.190.1",
    "10.47.88.5",
    "10.47.88.16",
    "10.47.249.3",
    "10.47.249.2",
    "10.47.12.1",
    "10.47.13.88",
    "10.47.13.63",
    "10.47.13.57",
    "10.47.13.56",
    "10.47.13.5",
    "10.47.13.36",
    "10.47.13.34",
    "10.47.13.234",
    "10.47.13.23",
    "10.47.13.221",
    "10.47.13.220",
    "10.47.13.216",
    "10.47.13.206",
    "10.47.13.201",
    "10.47.13.199",
    "10.47.13.19",
    "10.47.13.188",
    "10.47.13.186",
    "10.47.13.185",
    "10.47.13.18",
    "10.47.13.17",
    "10.47.13.165",
    "10.47.13.163",
    "10.47.13.16",
    "10.47.13.15",
    "10.47.13.140",
    "10.47.13.14",
    "10.47.13.139",
    "10.47.13.138",
    "10.47.13.137",
    "10.47.13.123",
    "10.47.13.12",
    "10.47.13.113",
    "10.47.13.105",
    "10.47.12.95",
    "10.47.12.94",
    "10.47.12.93",
    "10.47.12.91",
    "10.47.12.90",
    "10.47.12.9",
    "10.47.12.87",
    "10.47.12.86",
    "10.47.12.84",
    "10.47.12.82",
    "10.47.12.78",
    "10.47.12.76",
    "10.47.12.75",
    "10.47.12.70",
    "10.47.12.7",
    "10.47.12.67",
    "10.47.12.66",
    "10.47.12.65",
    "10.47.12.64",
    "10.47.12.62",
    "10.47.12.6",
    "10.47.12.57",
    "10.47.12.56",
    "10.47.12.55",
    "10.47.12.52",
    "10.47.12.50",
    "10.47.12.49",
    "10.47.12.46",
    "10.47.12.41",
    "10.47.12.40",
    "10.47.12.4",
    "10.47.12.38",
    "10.47.12.37",
    "10.47.12.34",
    "10.47.12.33",
    "10.47.12.30",
    "10.47.12.29",
    "10.47.12.28",
    "10.47.12.252",
    "10.47.12.250",
    "10.47.12.246",
    "10.47.12.242",
    "10.47.12.241",
    "10.47.12.24",
    "10.47.12.239",
    "10.47.12.231",
    "10.47.12.230",
    "10.47.12.226",
    "10.47.12.218",
    "10.47.12.217",
    "10.47.12.214",
    "10.47.12.213",
    "10.47.12.210",
    "10.47.12.206",
    "10.47.12.205",
    "10.47.12.203",
    "10.47.12.202",
    "10.47.12.200",
    "10.47.12.198",
    "10.47.12.193",
    "10.47.12.191",
    "10.47.12.19",
    "10.47.12.185",
    "10.47.12.17",
    "10.47.12.166",
    "10.47.12.160",
    "10.47.12.16",
    "10.47.12.154",
    "10.47.12.15",
    "10.47.12.146",
    "10.47.12.145",
    "10.47.12.144",
    "10.47.12.143",
    "10.47.12.142",
    "10.47.12.14",
    "10.47.12.135",
    "10.47.12.132",
    "10.47.12.13",
    "10.47.12.129",
    "10.47.12.127",
    "10.47.12.125",
    "10.47.12.124",
    "10.47.12.123",
    "10.47.12.122",
    "10.47.12.12",
    "10.47.12.111",
    "10.47.12.108",
    "10.47.12.106",
    "10.47.12.105",
    "10.47.12.104",
    "10.47.12.103",
    "10.47.12.102",
    "10.47.12.101",
    "10.47.12.10",
    "10.47.10.5",
    "10.47.154.97",
    "10.47.154.93",
    "10.47.154.92",
    "10.47.154.88",
    "10.47.154.86",
    "10.47.154.85",
    "10.47.154.84",
    "10.47.154.76",
    "10.47.154.75",
    "10.47.154.64",
    "10.47.154.62",
    "10.47.154.61",
    "10.47.154.60",
    "10.47.154.58",
    "10.47.154.57",
    "10.47.154.43",
    "10.47.154.40",
    "10.47.154.31",
    "10.47.154.27",
    "10.47.154.26",
    "10.47.154.23",
    "10.47.154.21",
    "10.47.154.20",
    "10.47.154.185",
    "10.47.154.167",
    "10.47.154.14",
    "10.47.154.139",
    "10.47.154.138",
    "10.47.154.137",
    "10.47.154.131",
    "10.47.154.13",
    "10.47.154.1",
    "10.47.134.8",
    "10.47.134.76",
    "10.47.134.73",
    "10.47.134.6",
    "10.47.134.46",
    "10.47.134.40",
    "10.47.134.37",
    "10.47.134.34",
    "10.47.134.32",
    "10.47.134.31",
    "10.47.134.3",
    "10.47.134.28",
    "10.47.134.23",
    "10.47.134.22",
    "10.47.134.130",
    "10.47.134.125",
    "10.47.134.124",
    "10.47.134.123",
    "10.47.134.122",
    "10.47.134.121",
    "10.47.134.116",
    "10.47.134.107",
    "10.47.134.1",
    "10.47.52.1",
    "10.47.174.89",
    "10.47.174.85",
    "10.47.174.80",
    "10.47.174.71",
    "10.47.174.68",
    "10.47.174.62",
    "10.47.174.59",
    "10.47.174.58",
    "10.47.174.57",
    "10.47.174.54",
    "10.47.174.47",
    "10.47.174.4",
    "10.47.174.34",
    "10.47.174.33",
    "10.47.174.31",
    "10.47.174.30",
    "10.47.174.3",
    "10.47.174.29",
    "10.47.174.28",
    "10.47.174.26",
    "10.47.174.253",
    "10.47.174.2",
    "10.47.174.18",
    "10.47.174.119",
    "10.47.174.118",
    "10.47.174.11",
    "10.47.174.109",
    "10.47.174.10",
    "10.47.231.8",
    "10.47.231.5",
    "10.47.231.4",
    "10.47.231.3",
    "10.47.8.142",
    "10.47.8.206",
    "10.47.8.186",
    "10.47.2.210",
    "10.47.8.134",
    "10.47.30.4",
    "10.47.234.3",
    "10.47.4.2",
    "10.47.5.5",
    "10.47.5.1",
    "10.47.8.7",
    "10.47.33.25",
    "10.47.33.18",
    "10.47.33.1",
    "10.47.8.230",
    "10.47.8.170",
    "10.47.8.226",
    "10.47.8.190",
    "10.47.3.176",
    "10.47.3.166",
]


def ping_ip(ip):
    try:
        # For Windows
        output = subprocess.check_output(
            ["ping", "-n", "1", ip], stderr=subprocess.STDOUT, universal_newlines=True
        )
        if "Received = 1" in output:
            return True
    except subprocess.CalledProcessError:
        pass

    try:
        # For UNIX-like systems
        output = subprocess.check_output(
            ["ping", "-c", "1", ip], stderr=subprocess.STDOUT, universal_newlines=True
        )
        if "1 packets received" in output:
            return True
    except subprocess.CalledProcessError:
        pass

    return False

def main():
    unresponsive_ips = []
    total_ips = len(ip_addresses)
    
    for ip in ip_addresses:
        result = ping_ip(ip)
        if result:
            print(f"{ip} is UP")
        else:
            print(f"{ip} is DOWN")
            unresponsive_ips.append(ip)

    responsive_count = total_ips - len(unresponsive_ips)
    print(f"\nTotal IP addresses scanned: {total_ips}")
    print(f"Number of IP addresses that responded: {responsive_count}")
    print(f"Number of IP addresses that did not respond: {len(unresponsive_ips)}")

    if unresponsive_ips:
        print("\nThe following IP addresses did not respond:")
        for ip in unresponsive_ips:
            print(ip)

if __name__ == "__main__":
    main()
