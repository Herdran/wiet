import os
import matplotlib; matplotlib.use("TkAgg")

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import matplotlib.animation as mpl_animation
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# @tf.function
def funny_function(x):
    return (x - 5.0) ** 2


# @tf.function
def wavy_function(x):
    return 40.0 * tf.sin(x)


# @tf.function
def combined_function(x):
    return 0.5 * funny_function(x) + 0.5 * wavy_function(x)


def main():
    current_x = tf.Variable(-47.0)

    xs = tf.Variable(np.linspace(-50.0, 50.0, 1000))
    ys = combined_function(xs)

    optimiser = tf.keras.optimizers.SGD(learning_rate=0.1, momentum=0.3)

    fig, ax = plt.subplots()

    def step(i):
        with tf.GradientTape() as tape:
            current_y = combined_function(current_x)
        gradients = tape.gradient(current_y, [current_x])

        ax.clear()
        ax.plot(xs.numpy(), ys.numpy())
        ax.scatter([current_x.numpy()], [current_y.numpy()])

        optimiser.apply_gradients(zip(gradients, [current_x]))

    animation = mpl_animation.FuncAnimation(fig, step, interval=100)
    plt.show()




if __name__ == '__main__':
    main()