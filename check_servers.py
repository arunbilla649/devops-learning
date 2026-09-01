#!/usr/bin/env python3
import subprocess
import datetime

INPUT_FILE = "servers.txt"
LOG_FILE = "reachability.log"

def check_host(host):
    """Ping a host once, return True if reachable."""
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def main():
    with open(INPUT_FILE, "r") as f:
        hosts = [line.strip() for line in f if line.strip()]

    with open(LOG_FILE, "a") as log:
        for host in hosts:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            reachable = check_host(host)
            status = "UP" if reachable else "DOWN"
            line = f"{timestamp} | {host} | {status}"
            print(line)
            log.write(line + "\n")

if __name__ == "__main__":
    main()
