import numpy as np
import matplotlib.pyplot as plt

class Boid:

    @property
    def acceleration(self):
        alpha = np.pi/30
        a = np.array([0, 0], dtype=float)
        a[0] = self.velocity[0]*(np.cos(alpha)-1) - self.velocity[1]*np.sin(alpha)
        a[1] = self.velocity[0]*np.sin(alpha) + self.velocity[1]*(np.cos(alpha)-1)
        return a

    def update_velocity(self, *, dt: float) -> None:
        """
        Update the velocity of the boid based on its acceleration

        Args:
            dt: The time step for the simulation
        """
        self.velocity = self.velocity + dt*self.acceleration
        
    def move_boid(self, *, dt: float) -> None:
        """
        Move the boid based on its velocity

        Args:
            dt: The time step for the simulation
        """
        self.position = self.position + dt*self.velocity
        self.update_velocity(dt=dt)

    def plot_trajectory(self, *, dt: float, num_steps: int) -> None:
        """
        Plot the trajectory of the boid

        Args:
            dt: The time step for the simulation
            num_steps: The number of steps to simulate
        """
        traj = []
        for _ in range(num_steps):
            self.move_boid(dt=dt)
            traj.append(self.position)
        traj = np.array(traj)
        _, ax = plt.subplots()
        ax.plot(*traj.T, "o-")
        ax.set_aspect("equal")

    def __init__(self, position, velocity):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)