import PhysicsVis as pv

def main():
    visualizer = pv.PhysicsVisualizer()
    visualizer.math_engine.fetch_data("data.csv")
    visualizer.math_engine.showGraph()




if __name__ == '__main__':
    main()


