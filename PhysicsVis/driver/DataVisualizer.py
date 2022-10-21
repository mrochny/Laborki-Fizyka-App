import matplotlib.pyplot as plt
import numpy as np

class DataVisualizer:

    data_x: np.ndarray
    data_y: np.ndarray


    def showGraph(self):
        fig, ax = plt.subplots()
        ax.stem(self.data_x, self.data_y)
        plt.show()

    def debug_seed_random_data(self):
        np.random.seed(4)
        self.data_x = 1.0 + np.arange(9)
        self.data_y = np.random.uniform(3, 9, len(self.data_x))

