#!/usr/bin/env python3
import shutil

def check_disk_usage(path="/", threshold=80):
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100

    if percent_used > threshold:
        print(f"WARNING: Disk usage is at {percent_used:.1f}%")
    else:
        print(f"OK: Disk usage is at {percent_used:.1f}%")

if __name__ == "__main__":
    check_disk_usage()
