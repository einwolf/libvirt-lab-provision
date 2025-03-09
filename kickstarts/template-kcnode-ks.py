#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

hosts = [
    # kc1
    {
        "hostname": "kc1n1",
        "mac_eth0": "52:54:00:7c:53:e8"
    },
    {
        "hostname": "kc1n2",
        "mac_eth0": "52:54:00:02:5c:df",
    },
    {
        "hostname": "kc1n3",
        "mac_eth0": "52:54:00:6d:2d:7e",
    },
    {
        "hostname": "kc1n4",
        "mac_eth0": "52:54:00:0b:9b:ba",
    },
    # kc2
    {
        "hostname": "kc2n1",
        "mac_eth0": "52:54:00:5b:0c:2f",
    },
    {
        "hostname": "kc2n2",
        "mac_eth0": "52:54:00:d0:98:64",
    },
    {
        "hostname": "kc2n3",
        "mac_eth0": "52:54:00:6f:ff:33",
    },
    {
        "hostname": "kc2n4",
        "mac_eth0": "52:54:00:e2:25:f5",
    }
]


def main():
    template_loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=template_loader)
    template = env.get_template("kc-node.cfg")

    for host in hosts:
        ks_file_name = f"{host['hostname']}-ks.cfg"
        print(f"Write {ks_file_name}")

        with open(ks_file_name, "w+") as ks_file:
            ks_file.write(template.render(**host))



if __name__ == "__main__":
    main()
