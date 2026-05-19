# What is the meaning of N in the description "The mean operation still operates over all the elements, and divides by N"?

Curated at: `2026-05-19T05:51:32.192939+00:00`
Model: `Public Q&A`
Author: `Alberto`
Tags: `public-q&a, AI Stack Exchange, python, pytorch, mean-squared-error`
Source: https://ai.stackexchange.com/questions/50569/what-is-the-meaning-of-n-in-the-description-the-mean-operation-still-operates-o


## Why It Is Good

- Public Q&A from AI Stack Exchange.
- Question score: 0; answer score: 1.
- The answer was accepted by the question author.
- Viewed 48 times on the source site.

## Question

In torch.nn.MSELoss doc , it is mentioned that : where N is the batch size. Then : The mean operation still operates over all the elements, and divides by N . I am confused about the definition of N. According to my understanding, if the ground truth and predicted inputs are each of shape (B, C, H, W) (a batch of images, each of shape (C, H, W)), and MSE is used in this context as a reconstruction loss in an image reconstruction head with reduction = "mean", then N is defined as the total number of pixels = B × C × H × W. So here, N is the total number of pixels, not the batch size. So my question is: is my understanding of N in this use case correct?

## Answer

Yes, reduction mean is equivalent of summing everything and dividing by the product of the resulting tensor
