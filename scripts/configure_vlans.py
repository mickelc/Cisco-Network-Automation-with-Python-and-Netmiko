# This script will add VLAN 40 on SW-1 and VLAN 50 on SW-2

from netmiko import ConnectHandler
from inventory import get_devices

# VLAN configuration for each switch
vlan_configs = {
    "192.168.20.2": [ #SW-1 Management IP
        "vlan 40",
        "name ENGINEERING",
        "exit",
        "interface GigabitEthernet0/2",
        "switchport mode access",
        "switchport access vlan 40",
        "no shutdown",
    ],
    "192.168.30.2": [ #SW-2 Management IP
        "vlan 50",
        "name OPERATIONS",
        "exit",
        "interface GigabitEthernet0/2",
        "switchport mode access",
        "switchport access vlan 50",
        "no shutdown",
    ],
}

# Connect to each switch and apply configuration
for device in get_devices(["SW-1", "SW-2"]):
    print(f"\nConfiguring VLANs on {device['host']}")

# Establish an SSH connection using the device info and close it when finished
    with ConnectHandler(**device) as conn:
        conn.enable()
        
        # Send the VLAN configuration commands to the connected device
        output = conn.send_config_set(
            vlan_configs[device["host"]]
        )

        print(output)
        # Save the running configuration to the startup configuration
        conn.save_config()
  
print("\nVLAN configuration completed.")


