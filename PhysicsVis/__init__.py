from PhysicsVis.driver.DataVisualizer import DataVisualizer as dv


class PhysicsVisualizer:

    math_engine: dv = dv()

    def __init__(self):
        self.math_engine.fetch_data("nothing.csv")
