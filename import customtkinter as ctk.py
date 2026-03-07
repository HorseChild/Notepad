import customtkinter as ctk
from datetime import datetime, timedelta
import calendar

class ModernCalendarApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern Calendar")
        self.geometry("900x700")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.bg_primary = "#0f0f23"
        self.bg_secondary = "#1a1a2e"
        self.accent_purple = "#6d28d9"
        self.accent_pink = "#ec4899"
        self.card_bg = "#16213e"

        self.current_data = datetime.now()
        self.selected_date = None
        self.events = {}

        self.create_header()
        self.create_calendar_grid()
        self.create_event_panel()

        self.display_month()
    def create_header(self):
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(pady=20, padx=20, fill="x")

        self.prev_btn = ctk.CTkButton (
            header_frame, text="←", width = 50, font=('Arial', 20, 'bold')
            command = self.previous_month, fg_color = self.accent_purple
        )
        self.prev_btn.pack(side=left, padx=10)

        self.month_year_label = ctk.CTklabel (
            header_frame, text="", font=("Arial", 28, "bold")
            command=self.go_to_today, fg_color=self.accent_pink
        )
        self.today_btn.pack(side="left", padx=10)

        self.next_btn = ctk.CTkButton (
            header_frame, text="→", width = 50, font=('Arial', 20, 'bold')
            command = self.previous_month, fg_color = self.accent_purple
        )
        self.next_btn.pack(side=left, padx=10)

        def create_calendar_grid (self):
            self.calendar_frame = ctk.CTkFrame(self, fg_color="transparent")
            self.calendar_frame.pack(pady=10, padx=20, fill="both", expand=True)

            days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
            for col, day in enumerate(days):
                day_label = ctk.CTkLabel(
                    self.calendar_frame, text=day,
                    font=("Arial", 14, "bold") text_color=self.accent_pink
                )
                day_label.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

            self.date_buttons = []
            for row in range(1, 7):
                week_buttons = []
                for col in range(7):
                    btn = ctk.CTkButton(
                        self.calendar_frame, text="",
                        width="100", height="80", font("Arial", 16),
                        fg_color=self.card_bg
                    )
                    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                    week_buttons.append(btn)
                self.date_buttons.append(week_buttons)

            for i in range(7):
                self.calendar_frame.grid_columnconfigure(i, weight=1)
            for i in range(7):
                self.calendar_frame.grid_rowconfigure(i, weight=1)
        def create_event_panel (self:)
            event_frame=ctk.CTkFrame(self, corner_radius=15)
            event_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
            title_label = ctk.CTkLabel(
                event_frame, text="Events", font=("Arial", 20, "bold")
            )
            title_label.pack(pady=15)
            self.selected_date_label = ctk.CTkLabel(
                event_frame, text="Select a date to view events",
                font=("Arial", 14), text_color=self.accent_purple
            )
            self.selected_date_label.pack(pady=5)
            self.event_entry = ctk.CTkEntry(
                event_frame, placeholder_text="Add new event",
                font=("Arial", 14)
            )
            self.event_entry.pack(pady=10, padx=20, fill="x")
        
            self.add_event_btn = ctk.CTkButton(
                event_frame, text="Add Event", font=("Arial", 14, "bold"),
                command=self.add_event, fg_color=self.accent_purple
            )

            self.events_textbox = ctk.CTkTextbox(
                event_frame, font=("Arial", 13), wrap="word"
            )
            self.events_textbox.pack(pady=10, padx=20, fill="both", expand=True)
        
        def display_month(self):
            month_name = calendar.month_name[self.current_data.month]
            year = self.current_data.year
            self.month_year_label.configure(text=f"{month_name} {year}")

            first_day_of_month = self.current_data.replace(day=1)
            start_day = first_day_of_month.weekday()
            if start_day == 6:
                start_day = -1

            num_days = calendar.monthrange(year, self.current_data.month)[1]

            day_num = 1
            for row in range(1, 7):
                for col in range(7):
                    btn = self.date_buttons[row-1][col]
                    if (row == 1 and col <= start_day) or day_num > num_days:
                        btn.configure(text="", fg_color=self.card_bg, command=lambda: None)
                    else:
                        btn.configure(
                            text=str(day_num), fg_color=self.bg_secondary,
                            command=lambda d=day_num: self.select_date(d)
                        )
                        day_num += 1