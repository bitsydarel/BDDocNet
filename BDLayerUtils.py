import tensorflow as tf


def bd_convolution_layer(filters, kernel_size, strides, padding ="same", activation="leaky"):
    tf.layers.Conv2D(filters, kernel_size, strides, padding, activation)
    pass


def bd_identity_convolution_layer(same_output = False):
    pass


if __name__ == "__main__":
    bd_convolution_layer(6, 3, 1)

