import tkinter as tk
from tkinter import ttk
from core.tracker import WeaponTracker


class TrackerUI:
    def __init__(self, tracker: WeaponTracker):
        self.tracker = tracker
        self.root = tk.Tk()
        self.root.title("Monster Hunter Weapon Tracker")
        self.root.geometry("650x700")
        self.root.configure(bg="#2e2e2e")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#3c3f41",
            foreground="white",
            rowheight=30,
            fieldbackground="#3c3f41",
            bordercolor="#444",
            borderwidth=1,
            font=("Segoe UI", 11),
            anchor="center",
        )
        style.configure(
            "Treeview.Heading",
            background="#2e2e2e",
            foreground="white",
            font=("Segoe UI", 12, "bold"),
            anchor="center",
        )

        self.title_label = tk.Label(
            self.root,
            text="Weapon Usage Tracker",
            font=("Segoe UI", 16, "bold"),
            fg="white",
            bg="#2e2e2e",
        )
        self.title_label.pack(pady=10)

        self.table = ttk.Treeview(
            self.root,
            columns=("weapon", "primary", "secondary"),
            show="headings",
            style="Treeview",
        )
        for col in ("weapon", "primary", "secondary"):
            self.table.heading(col, text=col.capitalize())
            self.table.column(col, anchor="center")
        self.table.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.next_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 13),
            fg="white",
            bg="#2e2e2e",
            justify="left",
        )
        self.next_label.pack(pady=10)

        self.advance_button = tk.Button(
            self.root,
            text="Avançar Arma",
            command=self.advance,
            font=("Segoe UI", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            relief=tk.FLAT,
            padx=15,
            pady=8,
        )
        self.advance_button.pack(pady=20)

        self.update_ui()
        self.root.mainloop()

    def update_ui(self):
        self.table.delete(*self.table.get_children())
        for weapon in self.tracker.weapons.values():
            self.table.insert(
                "", "end", values=(weapon.name, weapon.primary, weapon.secondary)
            )

        primary, secondary = self.tracker.get_next_weapons()
        remaining_primary, remaining_secondary = self.tracker.quests_remaining()
        total_remaining = max(remaining_primary, remaining_secondary)

        self.next_label.config(
            text=(
                f"Próxima primária: {primary.name}\n"
                f"Próxima secundária: {secondary.name}\n"
                f"Quests restantes para alinhamento: {total_remaining}"
            )
        )

    def advance(self):
        self.tracker.advance()
        self.update_ui()
