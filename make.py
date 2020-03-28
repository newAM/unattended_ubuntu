#!/usr/bin/env python3.8

import os
import shutil
import subprocess

image = "ubuntu-18.04.4-server-amd64.iso"

image_url = f"http://cdimage.ubuntu.com/releases/18.04.4/release/{image}"

this_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    home = os.path.expanduser("~")
    iso_root = os.path.join(home, "iso")
    os.makedirs(iso_root, exist_ok=True)

    iso_file = os.path.join(iso_root, image)
    iso_name = os.path.splitext(image)[0]
    iso_dir = os.path.join(iso_root, iso_name)

    if not os.path.isfile(iso_file):
        subprocess.run(["wget", image_url, "-O", iso_file], check=True)

    if os.path.isdir(iso_dir):
        shutil.rmtree(iso_dir)

    os.makedirs(iso_dir)
    subprocess.run(["bsdtar", "xfp", iso_file, "-C", iso_dir], check=True)
    subprocess.run(["chmod", "+w", "-R", iso_dir], check=True)

    shutil.copyfile(
        os.path.join(this_dir, "isolinux.cfg"),
        os.path.join(iso_dir, "isolinux", "isolinux.cfg"),
    )
    shutil.copyfile(
        os.path.join(this_dir, "txt.cfg"),
        os.path.join(iso_dir, "isolinux", "txt.cfg"),
    )
    shutil.copyfile(
        os.path.join(this_dir, "preseed.cfg"),
        os.path.join(iso_dir, "preseed", "preseed.cfg"),
    )

    subprocess.run(
        [
            "mkisofs",
            "-r",
            # fmt: off
            "-V", f"cust-{iso_name}",
            "-cache-inodes",
            "-J",
            "-l",
            "-b", "isolinux/isolinux.bin",
            "-c", "isolinux/boot.cat",
            "-no-emul-boot",
            "-boot-load-size", "4",
            "-boot-info-table",
            "-o", os.path.join(this_dir, f"custom-{image}"),
            # fmt: on
            iso_dir,
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
