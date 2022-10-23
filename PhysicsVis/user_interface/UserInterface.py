import tkinter as tk
from PhysicsVis.driver.DataVisualizer import DataVisualizer as dv


class UI:
    window: tk.Tk
    engine: dv = dv()

    def __init__(self):
        self.window = tk.Tk()
        self.window.size = 1920, 1080

        graph_button = tk.Button(self.window, command=self.handle_show_graph, text="Show graph")
        graph_button.pack()

        tk.mainloop()

    def handle_show_graph(self):
        self.engine.debug_seed_random_data()
        self.engine.show_graph()
