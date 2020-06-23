#Program to find area of a triangle using Heron's Formula

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def compute_area(sides):
  #slice the input to get sides
  a=sides[:,0]
  b=sides[:,1]
  c=sides[:,2]

  #Herons formula
  s=(a+b+c)*0.5
  areasq=s*(s-a)*(s-b)*(s-c)
  return tf.sqrt(areasq)

with tf.Session() as sess:
  area=compute_area(tf.constant([[5.0,3.0,7.1],[2.3,4.1,4.8]]))
  result=sess.run(area)
  print(result)

#Taking Values at Run Time
with tf.Session() as sess:
  sides=tf.placeholder(tf.float32, shape=(None, 3))
  area=compute_area(sides)
  result=sess.run(area, feed_dict={
      sides:[
             [5.0,3.0,7.1],
             [2.3,4.1,4.8]
      ]
  })
  print(result)