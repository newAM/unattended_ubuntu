# Unattended Ubuntu Server Installer

Unattended Ubuntu 20.04 LTS server installer.

Please do not actually use this as-is.  This should be used only as a reference.

## Requirements
```bash
sudo apt install libosinfo-bin qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
sudo service libvirtd start
sudo update-rc.d libvirtd enable
service libvirtd status
sudo adduser `id -un` libvirt
sudo adduser `id -un` kvm
```

For headed environments:
```bash
sudo apt install tigervnc-viewer virt-manager
```

### Usage
Creating a password.
```bash
echo "password" > password && makepasswd --clearfrom password --crypt-md5
```

The `makepasswd` dependency can be installed on Ubuntu 20.04 with this command.
```bash
sudo apt install makepasswd
```

Serve files.
```bash
cd www
python3 -m http.server 3003
```

Create a VM.
```bash
wget http://releases.ubuntu.com/20.04/ubuntu-20.04-live-server-amd64.iso

virt-install \
    --name test1 \
    --ram 4096 \
    --disk pool=default,size=32,bus=virtio,format=qcow2 \
    --vcpus 4 \
    --os-type linux \
    --os-variant ubuntu20.04 \
    --virt-type kvm \
    --graphics vnc,port=5901,listen=0.0.0.0 \
    --autostart \
    --noautoconsole \
    --location ubuntu-20.04-live-server-amd64.iso,kernel=casper/vmlinuz,initrd=casper/initrd \
    --extra-args "autoinstall ds=nocloud-net;s=http://10.0.0.3:3003/"
```

* `--disk`
  * `size=32` size in GB
  * `bus=virtio` makes disk IOs faster
  * `format=qcow2` QEMU Copy On Write format, performant enough with snapshots
* `--os-variant` discover variants with `osinfo-query os`
* `--noautoconsole` do not automatically connect to the VNC session

Removing a VM.
```bash
virsh shutdown test1
virsh destroy test1
virsh undefine test1
# or
python3.8 kill_vm.py test1
```

## References
* [creating guests with virt install](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-guest_virtual_machine_installation_overview-creating_guests_with_virt_install)
* [Bridging reference](https://wiki.debian.org/BridgeNetworkConnections#Configuring_bridging_in_.2Fetc.2Fnetwork.2Finterfaces)
* [Ubuntu KVM Installation](https://help.ubuntu.com/community/KVM/Installation)
* [Please test autoinstalls for 20.04!](https://discourse.ubuntu.com/t/please-test-autoinstalls-for-20-04/15250)
