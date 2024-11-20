import matplotlib.pyplot as plt
import jax.numpy as jnp

def plot_value_function(i, j, k, values, grid):

    plt.contourf(grid.coordinate_vectors[0],
                 grid.coordinate_vectors[1],
                 values[:, :, i, j, k].T)
    plt.colorbar()
    plt.contour(grid.coordinate_vectors[0],
                grid.coordinate_vectors[1],
                values[:, :, i, j, k].T,
                levels=0,
                colors="black",
                linewidths=3)

    plt.title("angle: %.2f deg, v_rob: %.2f, v_hum: %.2f"%(grid.coordinate_vectors[2][i] * 180 / jnp.pi, grid.coordinate_vectors[3][j], grid.coordinate_vectors[4][k]))