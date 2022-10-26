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

    # csv files with data need to be provided, in format:
    # mohr: (distilled water, rubbing alcohol, salt water)
    # r1, r2, r3, ... , rn (values from 0.1 to 0.9)
    # 1/m1, 1/m2, 1/m3, ... ,1/mn (so one of the following: 1, 10, 100)
    @staticmethod
    def calculate_uncertainty_M1(mohr_path: str):
        data_mohr = np.ndarray(shape=(1, 1))
        R_UNCERTAINTY: float = 0.005
        try:
            data_mohr = np.genfromtxt(mohr_path, delimiter=',')
        except Exception as e:
            print(e)
            return
        weights_amount: int = len(data_mohr[0]) // 3
        if len(data_mohr[0]) % 3 != 0:
            return
        source_moments: float = DataVisualizer.__calculate_mohr_subproduct(data_mohr[0:2, 0:weights_amount])
        print(source_moments)
        alcohol_moments: float = DataVisualizer.__calculate_mohr_subproduct(data_mohr[0:2, weights_amount:weights_amount * 2])
        print(alcohol_moments)
        salty_moments: float = DataVisualizer.__calculate_mohr_subproduct(data_mohr[0:2, weights_amount*2:])
        print(salty_moments)
        alcohol_uncertainty: float = R_UNCERTAINTY/alcohol_moments + R_UNCERTAINTY/source_moments
        print("Niepewnosc denaturatu: ")
        print(alcohol_uncertainty)
        salty_uncertainty: float = R_UNCERTAINTY/salty_moments + R_UNCERTAINTY/source_moments
        print("Niepewnosc slonej wody: ")
        print(salty_uncertainty)
        return

    @staticmethod
    def __calculate_mohr_subproduct(subarray: np.ndarray) -> float:
        moments_sum: float = 0
        for i in range(len(subarray[0])):
            moments_sum += subarray[0, i] / subarray[1, i]
        return moments_sum







