# Unattended Ubuntu Server ISO Creator

This creates an ISO which will install Ubuntu server 18.04 LTS unattended.
Tested with virtualbox.

Please do not actually use this as-is.  This should be used only as a reference.

## Requirements
```bash
sudo apt install wget libarchive-tools
```
`libarchive-tools` may be replaced with `bsdtar` for older Ubuntu installs.

## Usage
```bash
./make.py
```

## References
* [linux-unattended-installation](https://github.com/core-process/linux-unattended-installation/tree/master/ubuntu/18.04/custom)
* [installation-guide](https://help.ubuntu.com/lts/installation-guide/i386/apb.html)
* [example-preseed.txt](https://help.ubuntu.com/lts/installation-guide/example-preseed.txt)
