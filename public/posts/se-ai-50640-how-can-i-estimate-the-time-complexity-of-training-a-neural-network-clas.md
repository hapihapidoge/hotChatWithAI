# How can I estimate the time complexity of training a neural network classifier?

Curated at: `2026-07-01T04:53:52.234421+00:00`
Model: `Public Q&A`
Author: `Timur Surov`
Tags: `public-q&a, AI Stack Exchange, neural-networks, training, python, computational-complexity, time-complexity`
Source: https://ai.stackexchange.com/questions/50640/how-can-i-estimate-the-time-complexity-of-training-a-neural-network-classifier


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 1; answer score: 1.
- The answer was accepted by the question author.
- Viewed 32 times on the source site.

## Question

I'm working on a face classifier using YOLO, but for the classification step, we are using a neural network with the following architecture: [code omitted] I'm training the network with N classes of 200 embeddings each, which means I have 200*N inputs to the neural network. I want to see if there is way to estimate the time complexity of the training phase of the neural network in function of the number of classes. Thank you!

## Answer

To estimate the time complexity of training your neural network as a function of the number of classes ( $N$ ), we need to look at two factors: the mathematical operations per sample (the forward and backward pass) and the total number of samples in your dataset.For this specific architecture, the theoretical time complexity per epoch is $O(N^2 + N \cdot d)$ , where $N$ is the number of classes and $d$ is your input_dim.Here is the step-by-step breakdown of how to arrive at that estimate. Complexity of a Single Forward PassThe time complexity of a fully connected (nn.Linear) layer is proportional to the number of multiplications and additions required, which is essentially the product of the input features and output features: $O(\text{in\_features} \times \text{out\_features})$ .Let $d$ be your input_dim and $N$ be your num_classes.Layer 1: nn.Linear(input_dim, 256) takes $O(d \times 256)$ operations.Layer 2: nn.Linear(256, 128) takes $O(256 \times 128)$ operations (a constant).Layer 3: nn.Linear(128, num_classes) takes $O(128 \times N)$ operations.Activation functions (ReLU) and Dropout are element-wise operations and operate in linear time relative to their input size, so they don't dominate the matrix multiplications.Summing these up, the complexity for a single sample is: $$O(d \cdot 256 + 256 \cdot 128 + 128 \cdot N)$$ Since constants are dropped in Big-O notation, the c...
