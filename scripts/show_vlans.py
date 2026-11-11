
from netmiko import ConnectHandler
from inventory import get_devices

names = ["SW-1", "SW-2"]

for device in get_devices(names): ## Loop through each network device in "names"
    print(f"\n{'=' * 55}") #Print a blank line followed by 55 equal signs
    print(f"VLAN TABLE: {device['host']}")
    print("=" * 55)

    with ConnectHandler(**device) as conn:
        output = conn.send_command(
            "show vlan brief"
        )
        print(output)

