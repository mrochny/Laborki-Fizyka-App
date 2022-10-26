
from PhysicsVis.user_interface.UserInterface import UI


class PhysicsVisualizer:

    interface: UI

    def __init__(self):
        self.interface = UI()
        self.interface.engine.calculate_uncertainty_M1("mohr.csv")
