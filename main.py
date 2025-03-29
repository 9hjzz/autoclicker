import tkinter as tk
from tkinter import simpledialog
import time
import threading

class AutoClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Auto Clicker")
        self.click_points = []
        self.is_running = False

        self.start_button = tk.Button(master, text="Iniciar", command=self.start_clicking)
        self.start_button.pack(pady=20)

        self.add_point_button = tk.Button(master, text="Agregar Punto de Click", command=self.add_click_point)
        self.add_point_button.pack(pady=20)

    def add_click_point(self):
        point = simpledialog.askstring("Input", "Ingrese las coordenadas del punto (x,y):")
        if point:
            self.click_points.append(tuple(map(int, point.split(','))))

    def start_clicking(self):
        if not self.is_running:
            self.is_running = True
            threading.Thread(target=self.click).start()

    def click(self):
        while self.is_running:
            for point in self.click_points:
                # Simulate clicking at the specified coordinates
                print(f"Clicking at {point}")
                time.sleep(1)  # Delay between clicks

    def stop_clicking(self):
        self.is_running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()
