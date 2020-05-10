#!/usr/bin/env python3

import argparse
import subprocess

parser = argparse.ArgumentParser(description="Helper script to kill VMs.")
parser.add_argument("vmname", type=str, help="VM domain to kill.")
args = parser.parse_args()

subprocess.run(["virsh", "shutdown", args.vmname])
subprocess.run(["virsh", "destroy", args.vmname])
subprocess.run(["virsh", "undefine", args.vmname])
