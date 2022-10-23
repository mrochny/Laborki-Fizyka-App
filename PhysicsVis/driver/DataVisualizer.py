import matplotlib.pyplot as plt
import numpy as np

class DataVisualizer:

    data_x: np.ndarray
    data_y: np.ndarray


    def show_graph(self):
        fig, ax = plt.subplots()
        ax.stem(self.data_x, self.data_y)
        plt.show()

    def debug_seed_random_data(self):
        np.random.seed(4)
        self.data_x = 1.0 + np.arange(9)
        self.data_y = np.random.uniform(3, 9, len(self.data_x))

    def __reset_data(self):
        self.data_x = np.ndarray(shape=(1, 1))
        self.data_x[0] = 0
        self.data_y = np.ndarray(shape=(1, 1))
        self.data_y[0] = 0

    def fetch_data(self, file_path: str, delimiter: str = ","):
        try:
            tmp_data = np.genfromtxt(file_path, delimiter=delimiter, invalid_raise=True)
            self.data_x = tmp_data[0]
            self.data_y = tmp_data[1]
        except Exception as e:
            print(e)
            self.__reset_data()


