
score = [85,79,93]
print("语文成绩: %d 分" % score[0])
print("数学成绩: %d 分" % score[1])
print("英语成绩: %d 分" % score[2])

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b))
