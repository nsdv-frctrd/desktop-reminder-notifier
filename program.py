import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from plyer import notification

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder App")

        self.reminders = []

        self.name_label = tk.Label(root, text="Reminder Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.time_label = tk.Label(root, text="Time (HH:MM):")
        self.time_label.pack()
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        self.set_button = tk.Button(root, text="Set Reminder", command=self.set_reminder)
        self.set_button.pack()

    def set_reminder(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        reminder_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        self.reminders.append({"name": name, "datetime": reminder_datetime})

        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

        messagebox.showinfo("Reminder Set", f"Reminder '{name}' set for {date} {time}")

    def check_reminders(self):
        now = datetime.now()
        for reminder in self.reminders:
            if reminder["datetime"] - now <= timedelta(minutes=30):
                notification_title = "Reminder"
                notification_message = f"Reminder: {reminder['name']} starts in 30 minutes."
                notification.notify(
                    title=notification_title,
                    message=notification_message,
                    timeout=10
                )

def main():
    root = tk.Tk()
    app = ReminderApp(root)

    while True:
        app.check_reminders()
        root.update()
        root.after(1000)  # Check reminders every second

if __name__ == "__main__":
    main()
