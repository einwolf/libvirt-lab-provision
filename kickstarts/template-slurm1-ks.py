#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
from pathlib import Path

hosts = [
    {
        "hostname": "slurm1-head1",
        "mac_eth0": "52:54:00:7c:53:e8"
    },
    {
        "hostname": "slurm1-db1",
        "mac_eth0": "52:54:00:02:5c:df",
    },
    {
        "hostname": "slurm1-worker1",
        "mac_eth0": "52:54:00:6d:2d:7e",
    },
    {
        "hostname": "slurm1-worker2",
        "mac_eth0": "52:54:00:0b:9b:ba",
    },
    {
        "hostname": "slurm1-worker3",
        "mac_eth0": "52:54:00:5b:0c:2f",
    },
    {
        "hostname": "slurm1-worker4",
        "mac_eth0": "52:54:00:d0:98:64",
    },
    {
        "hostname": "slurm1-gpu1",
        "mac_eth0": "52:54:00:6f:ff:33",
    }
]


def main():
    template_loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=template_loader)
    template = env.get_template("slurm-base1-ks.cfg")

    for host in hosts:
        ks_file_name = f"{host['hostname']}-ks.cfg"
        print(f"Write {ks_file_name}")

        with open(ks_file_name, "w+") as ks_file:
            ks_file.write(template.render(**host))



if __name__ == "__main__":
    main()
