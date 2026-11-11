
from getpass import getpass

DEVICES = {
    "R1": {
        "device_type": "cisco_xe",
        "host": "192.168.10.1",
    },
    "R2": {
        "device_type": "cisco_xe",
        "host": "192.168.10.2",
    },
    "SW-1": {
        "device_type": "cisco_ios",
        "host": "192.168.20.2",
    },
    "SW-2": {
        "device_type": "cisco_ios",
        "host": "192.168.30.2",
    },
    "MGMT-SW": {
        "device_type": "cisco_ios",
        "host": "192.168.10.254",
    },
}

#Defining a function
def get_devices(names):
    username = input("SSH username: ") #Requesting the username for SSH
    password = getpass("SSH password: ") #Securely requesting password
    secret = getpass("Enable secret: ")

    return [
        {
            **DEVICES[name],
            "username": username,
            "password": password,
            "secret": secret,
        }
        for name in names
    ]

