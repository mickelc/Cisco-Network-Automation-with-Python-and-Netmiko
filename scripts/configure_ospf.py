
# ============================================================
# PROJECT: Cisco Network Automation with Python and Netmiko
# SCRIPT: configure_ospf.py
#
# PURPOSE:
# 1. Establish SSH connections to R1 and R2.
# 2. Configure OSPF process 1 on both routers.
# 3. Advertise each router's respective LAN subnet.
# 4. Establish OSPF adjacency over the management VLAN.
# 5. Save the configuration on both routers.
# ============================================================

from netmiko import ConnectHandler

# Import the custom get_devices() function from inventory.py.
# This function retrieves device details and prompts for
# SSH credentials.
from inventory import get_devices


# Create a dictionary containing the OSPF commands for each
# router. Each router's management IP serves as its key.
ospf_configs = {

    # R1: Management IP 192.168.10.1
    "192.168.10.1": [
        "router ospf 1",                 # Start OSPF process 1
        "router-id 1.1.1.1",             # Assign a unique router ID
        "passive-interface default",    # Disable OSPF hellos on all interfaces
        "no passive-interface GigabitEthernet1",  # Enable OSPF hellos on Gi1
        "network 192.168.10.0 0.0.0.255 area 0",  # Enable OSPF on management subnet
        "network 192.168.20.0 0.0.0.255 area 0",  # Advertise R1 LAN subnet
    ],

    # R2: Management IP 192.168.10.2
    "192.168.10.2": [
        "router ospf 1",                 # Start OSPF process 1
        "router-id 2.2.2.2",             # Assign a unique router ID
        "passive-interface default",    # Disable OSPF hellos on all interfaces
        "no passive-interface GigabitEthernet1",  # Enable OSPF hellos on Gi1
        "network 192.168.10.0 0.0.0.255 area 0",  # Enable OSPF on management subnet
        "network 192.168.30.0 0.0.0.255 area 0",  # Advertise R2 LAN subnet
    ],
}

# Retrieve R1 and R2 connection details from inventory.py.
# The for loop processes one router at a time.
for device in get_devices(["R1", "R2"]):

    # Display the IP address of the router being configured.
    # The f-string inserts the device's host IP into the text.
    print(f"\nConfiguring OSPF on {device['host']}")

    # Establish an SSH session using the device dictionary.
    # **device unpacks the dictionary into keyword arguments.
    # The with statement automatically closes the connection.
    with ConnectHandler(**device) as conn:

        # Enter privileged EXEC mode (enable mode).
        conn.enable()

        # Select the OSPF commands matching the router's IP.
        # send_config_set() enters configuration mode and
        # sends the commands to the Cisco device.
        output = conn.send_config_set(
            ospf_configs[device["host"]]
        )

        # Display the router's configuration command output.
        print(output)

        # Save the running configuration to startup-config
        # so changes persist after the router reboots.
        conn.save_config()


# Display a message after both routers have been processed.
print("\nOSPF configuration completed.")

