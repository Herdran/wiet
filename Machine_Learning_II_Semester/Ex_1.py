import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import matplotlib; matplotlib.use("TkAgg")
import matplotlib.animation as mpl_animation
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


# @tf.function
def z_function(x, y):
    return (x ** 4) + (y ** 4) - 2*(x ** 2) - 2*(y ** 2) + 4*(x * y)


def main():
    current_x = tf.Variable(1.0)
    current_y = tf.Variable(1.0)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    xs = np.arange(-3, 3, 0.01)
    ys = np.arange(-3, 3, 0.01)
    xs, ys = np.meshgrid(xs, ys)
    zs = z_function(xs, ys)

    optimiser = tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.02)

    def step(i):
        with tf.GradientTape() as tape:
            current_z = z_function(current_x, current_y)
        if i % 2 == 0:
            gradients = tape.gradient(current_z, [current_x])
        else:
            gradients = tape.gradient(current_z, [current_y])

        ax.clear()
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        ax.plot_surface(xs, ys, zs, linewidth=0, color='r', antialiased=False, alpha=0.3)
        ax.scatter([current_x.numpy()], [current_y.numpy()], [current_z.numpy()])
        if i % 2 == 0:
            optimiser.apply_gradients(zip(gradients, [current_x]))
        else:
            optimiser.apply_gradients(zip(gradients, [current_y]))

    animation = mpl_animation.FuncAnimation(fig, step, interval=100)

    plt.show()


if __name__ == '__main__':
    main()