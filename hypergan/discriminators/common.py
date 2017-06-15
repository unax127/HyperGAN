import tensorflow as tf
import hyperchamber as hc

def repeating_block(component, net, depth):
    ops = component.ops
    config = component.config
    layer_regularizer = config.layer_regularizer
    filter_size_w = 2
    filter_size_h = 2
    filter = [1,filter_size_w,filter_size_h,1]
    stride = [1,filter_size_w,filter_size_h,1]
    for i in range(config.block_repeat_count-1):
        net = activation(net)
        if layer_regularizer is not None:
            net = component.layer_regularizer(net)
        net = ops.conv2d(net, 3, 3, 1, 1, depth)
        print("[discriminator] hidden layer", net)

    net = tf.nn.avg_pool(net, ksize=filter, strides=stride, padding='SAME')
    print('[discriminator] layer', net)
    return net

def standard_block(component, net, depth, fltr=3):
    ops = component.ops
    config = component.config
    filter_size_w = 2
    filter_size_h = 2
    filter = [1,filter_size_w,filter_size_h,1]
    stride = [1,filter_size_w,filter_size_h,1]

    net = ops.conv2d(net, fltr, fltr, 1, 1, depth)
    #TODO
    net = tf.nn.avg_pool(net, ksize=filter, strides=stride, padding='SAME')
    print('[discriminator] layer', net)
    return net

def strided_block(component, net, depth):
    ops = component.ops
    config = component.config
    net = ops.conv2d(net, 3, 3, 2, 2, depth)
    print('[discriminator] layer', net)
    return net
