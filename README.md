# Cisco-Network-Automation-with-Python-and-Netmiko

### Automating OSPF Routing and VLAN Configuration in Cisco Modeling Labs (CML)

## Project Overview

This project demonstrates how Python and Netmiko can be used to automate network configuration and verification tasks within a simulated enterprise network built using Cisco Modeling Labs (CML).

The lab consists of two Cisco routers, two access switches, a management switch, and an Ubuntu Linux automation server.

Rather than manually configuring every network device, I developed Python scripts to establish SSH connections, deploy OSPF routing configurations, create VLANs, and retrieve network verification outputs.

The project was completed in two phases:

- **Phase 1:** Automating OSPF routing between Cisco routers.
- **Phase 2:** Automating VLAN creation and interface assignments on Cisco switches.

## Technologies & Tools

| Technology | Purpose |
|---|---|
| Cisco Modeling Labs (CML) | Network simulation environment |
| Python 3 | Network automation scripting |
| Netmiko | SSH-based device configuration |
| Cisco IOS XE | Router operating system |
| Cisco IOS | Switch configuration |
| Ubuntu Linux | Centralized automation server |
| OSPF | Dynamic routing between routers |
| IEEE 802.1Q | VLAN tagging and trunking |
| SSHv2 | Secure remote device management |

## Network Topology

The network consists of the following devices:

- 2 Cisco routers (R1 and R2)
- 2 Cisco access switches (SW-1 and SW-2)
- 1 management switch (MGMT-SW)
- 1 Ubuntu Linux automation server
- 2 endpoint PCs

The management network provides SSH connectivity between the automation server and the Cisco devices.

### IP Addressing Scheme

| Device | Interface | IP Address |
|---|---|---|
| Ubuntu Server | ens2 | 192.168.10.10/24 |
| MGMT-SW | VLAN 10 | 192.168.10.254 |
| R1 | GigabitEthernet1 | 192.168.10.1 |
| R2 | GigabitEthernet1 | 192.168.10.2 |
| R1 | GigabitEthernet2.20 | 192.168.20.1 |
| R2 | GigabitEthernet2.30 | 192.168.30.1 |
| SW-1 | VLAN 20 | 192.168.20.2 |
| SW-2 | VLAN 30 | 192.168.30.2 |
