import subprocess


def _main():
    try:
        while True:
            command = input("Enter command (list, start, exit): ")

            if command == "start":
                device = input("Enter device number: ")
                if not device:
                  device = 1
                print("Monitoring device " + device + " in Realtime\n\n")
                subprocess.run(["pktmon", "start", "-c", "--trace",
                                "-p", "Microsoft-Windows-TCPIP", "--comp", device, "-m", "real-time"])
            elif command == "list":
                print("Listing devices\n\n")
                subprocess.run(["pktmon", "list"])
            elif command == "exit":
                return
            else:
                print("Invalid argument.")
    except KeyboardInterrupt:
        print("\nStopping packet monitoring\n\n")
        subprocess.run(["pktmon", "stop"])
        print("Converting PktMon.etl to PktMon.txt\n\n")
        subprocess.run(["pktmon", "etl2txt", "C:\\Windows\\system32\\PktMon.etl"])


if __name__ != "__main__":
    pass
else:
    _main()
