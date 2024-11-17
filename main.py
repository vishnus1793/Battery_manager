import tkinter as tk
import psutil
import time

class BatteryMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Battery Monitor")
        self.root.geometry("300x100")
        
        self.battery_label = tk.Label(self.root, text="Battery: 0%", font=("Arial", 15))
        self.battery_label.pack(pady=20)
        self.update_battery_status()
    def update_battery_status(self):
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            self.battery_label.config(text=f"Battery: {percent}%")
        else:
            self.battery_label.config(text="Battery info unavailable")
        
        self.root.after(1000, self.update_battery_status)
if __name__ == "__main__":
    root = tk.Tk()
    app = BatteryMonitorApp(root)
    root.mainloop()
