import tensorflow as tf
import numpy as np


class Model:
    def __init__(self, game, hidden_dim=100):
        # compute input_dim : the size of the input layer
        #   one neurone / possible match in the initial board
        #   +1 neurone to code which player is the current player
        self.initialBoard = game.getInitialBoard() 
        input_dim = sum (self.initialBoard) + 1
        self.input_dim = input_dim

        self.sess = None

        with tf.variable_scope('model'):
            self.feature_vector_ = tf.placeholder(tf.float32,
                                                  shape=[None, input_dim],
                                                  name='feature_vector_')
            with tf.variable_scope('layer_1'):
                W_1 = tf.get_variable('W_1',
                                      shape=[input_dim, hidden_dim],
                                      initializer=tf.contrib.layers.xavier_initializer())
                hidden_1 = tf.nn.relu(tf.matmul(self.feature_vector_, W_1), name='hidden_1')

            with tf.variable_scope('layer_2'):
                W_2 = tf.get_variable('W_2', shape=[hidden_dim, 1],
                                      initializer=tf.contrib.layers.xavier_initializer())
                self.value = tf.tanh(tf.matmul(hidden_1, W_2), name='value')

            self.trainable_variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES,
                                                         scope=tf.get_variable_scope().name)

    def make_feature_vector(self, board, player):
        fv = np.zeros((1, self.input_dim))

        k = 0;
        for i in range (len(board)) :
            for j in range(self.initialBoard[i]) :
                if j < board[i] :
                    fv[0,k] = 1
                else :
                    fv[0,k] = 0
                k+=1
                

        fv[0,-1] = float(player)
        return fv

    def evaluate(self,board, numPlayer):
        log_dir = "Bidon"
        with tf.train.SingularMonitoredSession(checkpoint_dir=log_dir) as sess:
            self.sess = sess
            feature_vectors = np.vstack(
                [self.make_feature_vector(board,numPlayer)])

            values = self.sess.run(self.value,
                                   feed_dict={
                                        self.feature_vector_: feature_vectors})

            return values[0]
