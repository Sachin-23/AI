Process:
Started with a simple neural network to see how the results vary before applying any pooling, filter, dropout or adding hidden layer.
Structure: The input layer flattens the shape into 1D and then passes it to output layer with activation function `softmax`.
Result: `loss: 49.2774 - accuracy: 0.7157`

Second Neural Network after apply 32 filter with kernel size 3x3.
Structure: The input layer filters the images then the images are flattened and after that the images are passed to output layer with activation function `softmax`.
Result: `loss: 1.0993 - accuracy: 0.9052`

Third Neural Network after apply 32 filter with kernel size 3x3 with max pooling of size 3x3.
Structure: Same network added layer max-pooling with shape of 3x3
Result: `loss: 0.6048 - accuracy: 0.9284`

Fourth Neural Network adding 2 hidden layer with 256 units and dropout with rate of 0.4.
Structure: Same network with 2 addition hidden layer and drop rate of 0.4 
Result: `loss: 0.3360 - accuracy: 0.9453`

Conclusion:
+ By applying filters using `Conv2D` the accuracy increased. As the network has more inputs to train on. But more filters slows down the learning/training time.
+ Adding a hidden layers without any dropout increases the accuracy during training but while evaluation the loss rate increases and accuracy decreases. This shows that the model overfits the training dataset.
+ Increasing more units hidden layers increases the overall accuracy but takes more time to train.
