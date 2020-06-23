#Program to add two arrays

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a= tf.constant([5,3,8])
b=tf.constant([3,-1,2])
c=tf.add(a,b)
with tf.Session() as sess:
  result=sess.run(c)
  print(result)