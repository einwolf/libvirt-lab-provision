#!/bin/bash

virt-install --osinfo fedora39 --name fedora39-master --vcpus 2 --memory 8192 --disk pool=d1disks,size=200 --network=bridge:br0 --location "/data1/libvirt/d1disks/Fedora-Workstation-Live-x86_64-39-1.5.iso" --initrd-inject "/data1/kickstarts/Fedora39s02-ks.cfg" --extra-args="inst.ks=file:/Fedora39s01-ks.cfg console=tty0 console=ttyS0,115200n8" --noautoconsole --wait 0

