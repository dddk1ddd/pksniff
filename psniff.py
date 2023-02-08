import subprocess


def _main():
    while True:
        command = input("Enter command (list, start, etl2txt, exit): ")

        if command == "start":
            device = input("Enter device number: ")
            if not device:
                device = 1
            print("Monitoring device " + device + " in Realtime\n\n")
            subprocess.run(["pktmon", "start", "-c", "--comp", device, "-m", "real-time"])
        elif command == "etl2txt":
            print("Converting PktMon.etl to PktMon.txt\n\n")
            subprocess.run(["pktmon", "etl2txt", "C:\\Windows\\system32\\PktMon.etl"])
        elif command == "list":
            print("Listing devices\n\n")
            subprocess.run(["pktmon", "list"])
        elif command == "exit":
            return
        else:
            print("Invalid argument.")


if __name__ != "__main__":
    pass
else:
    _main()
