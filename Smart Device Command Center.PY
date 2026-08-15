from abc import ABC, abstractmethod


# ==========================================
# SMART DEFENCE COMMAND CENTER
# Abstraction + Polymorphism Project
# ==========================================


# ABSTRACT CLASS
class SmartDevice(ABC):

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.status = "OFFLINE"

    def show_status(self):
        print("\n📟 DEVICE STATUS")
        print("Device   :", self.name)
        print("Location :", self.location)
        print("Status   :", self.status)

    @abstractmethod
    def execute_command(self, command):
        pass


# ==========================================
# DRONE
# ==========================================

class SurveillanceDrone(SmartDevice):

    def __init__(self, name, location, battery):
        super().__init__(name, location)
        self.battery = battery

    def execute_command(self, command):

        self.status = "ONLINE"

        if command == "scan":
            print("🚁 Drone is scanning the assigned area.")

        elif command == "return":
            print("🚁 Drone is returning to its base.")

        elif command == "status":
            print("🔋 Drone Battery:", self.battery, "%")

        else:
            print("❌ Drone does not understand this command.")


# ==========================================
# RESCUE ROBOT
# ==========================================

class RescueRobot(SmartDevice):

    def __init__(self, name, location, battery):
        super().__init__(name, location)
        self.battery = battery

    def execute_command(self, command):

        self.status = "ONLINE"

        if command == "scan":
            print("🤖 Robot is scanning the area for rescue conditions.")

        elif command == "return":
            print("🤖 Robot is returning to the support station.")

        elif command == "status":
            print("🔋 Robot Battery:", self.battery, "%")

        else:
            print("❌ Robot does not understand this command.")


# ==========================================
# RADAR SYSTEM
# ==========================================

class RadarSystem(SmartDevice):

    def __init__(self, name, location, range_km):
        super().__init__(name, location)
        self.range_km = range_km

    def execute_command(self, command):

        self.status = "ONLINE"

        if command == "scan":
            print("📡 Radar is scanning its monitoring range.")

        elif command == "return":
            print("📡 Radar has stopped its active scan.")

        elif command == "status":
            print("📡 Radar Range:", self.range_km, "km")

        else:
            print("❌ Radar does not understand this command.")


# ==========================================
# COMMUNICATION UNIT
# ==========================================

class CommunicationUnit(SmartDevice):

    def __init__(self, name, location, channel):
        super().__init__(name, location)
        self.channel = channel

    def execute_command(self, command):

        self.status = "ONLINE"

        if command == "scan":
            print("📡 Communication Unit is checking network connectivity.")

        elif command == "return":
            print("📡 Communication Unit is switching to standby mode.")

        elif command == "status":
            print("📶 Communication Channel:", self.channel)

        else:
            print("❌ Communication Unit does not understand this command.")


# ==========================================
# CREATE OBJECTS
# ==========================================

drone = SurveillanceDrone(
    "Falcon Drone",
    "Sector A",
    87
)

robot = RescueRobot(
    "RescueBot X1",
    "Sector B",
    92
)

radar = RadarSystem(
    "Eagle Radar",
    "Command Tower",
    150
)

communication = CommunicationUnit(
    "SecureLink",
    "Control Room",
    "Channel 7"
)


# ==========================================
# POLYMORPHISM
# ==========================================

devices = [
    drone,
    robot,
    radar,
    communication
]


print("=" * 50)
print("🛡️ SMART DEFENCE COMMAND CENTER")
print("=" * 50)

print("\nAvailable Devices:")

for i, device in enumerate(devices, 1):
    print(i, ".", device.name)


# ==========================================
# COMMAND CENTER MENU
# ==========================================

while True:

    print("\n" + "=" * 50)
    print("🎛️ COMMAND CENTER MENU")
    print("=" * 50)

    print("1️⃣  Scan")
    print("2️⃣  Status")
    print("3️⃣  Return / Standby")
    print("4️⃣  Show Device Information")
    print("5️⃣  Exit")

    choice = input("\nEnter your choice: ")

    if choice == "5":
        print("\n🔒 Command Center shutting down...")
        print("👋 Goodbye Commander!")
        break

    # --------------------------------------
    # SELECT DEVICE
    # --------------------------------------

    print("\nSelect a device:")

    for i, device in enumerate(devices, 1):
        print(i, ".", device.name)

    try:
        device_number = int(input("\nEnter device number: "))

        if device_number < 1 or device_number > len(devices):
            print("❌ Invalid device number.")
            continue

        selected_device = devices[device_number - 1]

    except ValueError:
        print("❌ Please enter a number.")
        continue

    # --------------------------------------
    # EXECUTE COMMAND
    # --------------------------------------

    if choice == "1":
        selected_device.execute_command("scan")

    elif choice == "2":
        selected_device.execute_command("status")

    elif choice == "3":
        selected_device.execute_command("return")

    elif choice == "4":
        selected_device.show_status()

    else:
        print("❌ Invalid choice.")