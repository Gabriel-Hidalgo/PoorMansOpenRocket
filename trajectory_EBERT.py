import matplotlib.pyplot as plt
def trajectory(px,py):
    plt.figure(num=0, figsize=(10,6))
    plt.plot(px,py, color='blue', linewidth=5, label='Trajectory')
    plt.xlabel('Horizontal Position (m)')
    plt.ylabel('Vertical Position (m)')
    plt.title('Rocket Trajectory')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()