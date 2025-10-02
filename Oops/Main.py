import tkinter as tk
from tkinter import ttk
import math
import time

class HeartDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("❤️ Heart Drawing Animation")
        self.root.geometry("800x700")
        self.root.configure(bg="#ffe6f0")
        
        # Variables
        self.is_drawing = False
        self.progress = 0
        self.speed = 5
        self.line_width = 3
        
        # Title
        title_frame = tk.Frame(root, bg="#ffe6f0")
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="❤️ Heart Drawing Animation ❤️",
            font=("Arial", 24, "bold"),
            fg="#ff0000",
            bg="#ffe6f0"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Red lines se banta hua beautiful heart!",
            font=("Arial", 12),
            fg="#666666",
            bg="#ffe6f0"
        )
        subtitle_label.pack()
        
        # Canvas
        canvas_frame = tk.Frame(root, bg="white", relief=tk.RAISED, borderwidth=3)
        canvas_frame.pack(pady=20, padx=20)
        
        self.canvas = tk.Canvas(
            canvas_frame,
            width=600,
            height=400,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Control Panel
        control_frame = tk.Frame(root, bg="#ffe6f0")
        control_frame.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(control_frame, bg="#ffe6f0")
        button_frame.pack(pady=10)
        
        self.start_btn = tk.Button(
            button_frame,
            text="▶ Start",
            command=self.start_drawing,
            font=("Arial", 12, "bold"),
            bg="#ff0000",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            borderwidth=3,
            cursor="hand2"
        )
        self.start_btn.grid(row=0, column=0, padx=5)
        
        self.pause_btn = tk.Button(
            button_frame,
            text="⏸ Pause",
            command=self.pause_drawing,
            font=("Arial", 12, "bold"),
            bg="#ff6600",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            borderwidth=3,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.pause_btn.grid(row=0, column=1, padx=5)
        
        self.reset_btn = tk.Button(
            button_frame,
            text="🔄 Reset",
            command=self.reset_drawing,
            font=("Arial", 12, "bold"),
            bg="#666666",
            fg="white",
            padx=20,
            pady=10,
            relief=tk.RAISED,
            borderwidth=3,
            cursor="hand2"
        )
        self.reset_btn.grid(row=0, column=2, padx=5)
        
        # Speed Control
        speed_frame = tk.Frame(control_frame, bg="#ffe6f0")
        speed_frame.pack(pady=10)
        
        tk.Label(
            speed_frame,
            text="Speed:",
            font=("Arial", 11, "bold"),
            bg="#ffe6f0",
            fg="#333333"
        ).grid(row=0, column=0, padx=5)
        
        self.speed_scale = tk.Scale(
            speed_frame,
            from_=1,
            to=10,
            orient=tk.HORIZONTAL,
            length=200,
            command=self.update_speed,
            bg="#ffe6f0",
            fg="#ff0000",
            font=("Arial", 10),
            highlightthickness=0
        )
        self.speed_scale.set(5)
        self.speed_scale.grid(row=0, column=1, padx=5)
        
        # Line Width Control
        tk.Label(
            speed_frame,
            text="Line Width:",
            font=("Arial", 11, "bold"),
            bg="#ffe6f0",
            fg="#333333"
        ).grid(row=1, column=0, padx=5, pady=5)
        
        self.width_scale = tk.Scale(
            speed_frame,
            from_=1,
            to=8,
            orient=tk.HORIZONTAL,
            length=200,
            command=self.update_width,
            bg="#ffe6f0",
            fg="#ff0000",
            font=("Arial", 10),
            highlightthickness=0
        )
        self.width_scale.set(3)
        self.width_scale.grid(row=1, column=1, padx=5, pady=5)
        
        # Progress Bar
        self.progress_bar = ttk.Progressbar(
            control_frame,
            length=400,
            mode='determinate',
            style="red.Horizontal.TProgressbar"
        )
        self.progress_bar.pack(pady=10)
        
        # Style for progress bar
        style = ttk.Style()
        style.theme_use('default')
        style.configure(
            "red.Horizontal.TProgressbar",
            troughcolor='#ffcccc',
            background='#ff0000',
            thickness=20
        )
        
        # Status Label
        self.status_label = tk.Label(
            control_frame,
            text="Ready to draw!",
            font=("Arial", 10),
            fg="#666666",
            bg="#ffe6f0"
        )
        self.status_label.pack(pady=5)
        
    def get_heart_point(self, t):
        """Calculate heart coordinates using parametric equations"""
        center_x = 300
        center_y = 220
        scale = 12
        
        angle = t * 2 * math.pi
        x = center_x + scale * 16 * math.pow(math.sin(angle), 3)
        y = center_y - scale * (
            13 * math.cos(angle) 
            - 5 * math.cos(2 * angle) 
            - 2 * math.cos(3 * angle) 
            - math.cos(4 * angle)
        )
        
        return x, y
    
    def draw_heart_step(self):
        """Draw heart progressively"""
        if not self.is_drawing:
            return
        
        if self.progress >= 1.0:
            self.is_drawing = False
            self.start_btn.config(state=tk.NORMAL)
            self.pause_btn.config(state=tk.DISABLED)
            self.status_label.config(text="Heart complete! ❤️")
            
            # Fill heart
            points = []
            for i in range(1001):
                t = i / 1000
                x, y = self.get_heart_point(t)
                points.extend([x, y])
            
            self.canvas.create_polygon(
                points,
                fill="#ffcccc",
                outline="",
                tags="fill"
            )
            self.canvas.tag_lower("fill")
            return
        
        # Calculate points
        step = 0.001 * self.speed
        old_progress = self.progress
        self.progress = min(self.progress + step, 1.0)
        
        # Draw line segment
        start_t = old_progress
        end_t = self.progress
        
        x1, y1 = self.get_heart_point(start_t)
        x2, y2 = self.get_heart_point(end_t)
        
        self.canvas.create_line(
            x1, y1, x2, y2,
            fill="#ff0000",
            width=self.line_width,
            capstyle=tk.ROUND,
            smooth=True,
            tags="heart"
        )
        
        # Update progress bar
        self.progress_bar['value'] = self.progress * 100
        self.status_label.config(text=f"Drawing... {int(self.progress * 100)}%")
        
        # Continue animation
        self.root.after(10, self.draw_heart_step)
    
    def start_drawing(self):
        """Start or restart drawing"""
        if self.progress >= 1.0:
            self.reset_drawing()
        
        self.is_drawing = True
        self.start_btn.config(state=tk.DISABLED)
        self.pause_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Drawing heart...")
        self.draw_heart_step()
    
    def pause_drawing(self):
        """Pause drawing"""
        self.is_drawing = False
        self.start_btn.config(state=tk.NORMAL)
        self.pause_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Paused")
    
    def reset_drawing(self):
        """Reset drawing"""
        self.is_drawing = False 
        self.progress = 0 
        self.canvas.delete("all") 
        self.progress_bar['value'] = 0
        self.start_btn.config(state=tk.NORMAL)
        self.pause_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Ready to draw!")
     
    def update_speed(self, value):  
        """Update drawing speed"""  
        self.speed = float(value) 
       
    def update_width(self, value): 
        """Update line width""" 
        self.line_width = float(value)

# Main application 
if __name__ == "__main__":
    root = tk.Tk()
    app = HeartDrawingApp(root) 
    root.mainloop()