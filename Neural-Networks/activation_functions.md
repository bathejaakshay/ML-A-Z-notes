# [Activation Functions - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2023/10/activation-functions-in-neural-networks/#:~:text=Activation%20functions%20are%20fundamental%20in,unique%20characteristics%20and%20use%20cases.)

### Impact of Activation Functions on Training:
- Activation functions determine how neurons transform input signals into output activations during forward propagation.
- During backpropagation, gradients calculated for each layer depend on the derivative of the activation function.
- The choice of activation function affects the overall training speed, stability, and convergence of neural networks.

### Vanishing Gradients:

- Vanishing gradients occur when the derivatives of activation functions become extremely small, causing slow convergence or stagnation in training.
- Sigmoid and tanh activation functions are known for causing vanishing gradients, especially in deep networks.

### Mitigating the Vanishing Gradient Problem:

- Rectified Linear Unit (ReLU) and its variants, such as Leaky ReLU, address the vanishing gradient problem by providing a non-zero gradient for positive inputs.
- ReLU functions result in faster convergence due to the lack of vanishing gradients when inputs are positive.

### Role of Zero-Centered Activation Functions:

- Activation functions like ELU, which offer zero-centered output, help mitigate the vanishing gradient problem by providing both positive and negative gradients.
- Zero-centered functions contribute to stable weight updates and optimization during training.

### Adaptive Activation Choices:

The choice of activation function should align with the network’s architecture and the specific problem’s requirements. It’s essential to empirically test different activation functions to determine the most suitable one for a given task.

# [Acivation Functions - Towards DS](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6)  

1. Linear or Identity Activation Function.
    f(x) = x  
   Range = \[-inf, +inf\]  
   Not that useful.  
2. Non Linear Activation Functions  
   - Non Linearity makes it easy for the model to generalize or adapt with variety of data and to differentiate between the output.
   - Sigmoid or logistic: f(x) = 1/(1 + e<sup>-x</sup>)
     - Range: \[0,1\]
     - Useful when we have to predict the probability as an output
     - Its differenciable, monotonic
     - Derivative is not monotonic
     - Generalized form: Softmax, used in multiclass classification problem.
   - Tanh or hyperbolic tangent
     - Range \[-1,1\]
     - The advantage is that the negative inputs will be mapped strongly negative and the zero inputs will be mapped near zero in the tanh graph.
     - The function is differentiable.
     - The function is monotonic while its derivative is not monotonic.
     - The tanh function is mainly used classification between two classes.
     - Both sigmoid and tanh are used in feedforward NNs
   - ReLU (Rectified Linear Unit)
     - range: \[0 to inf)
     - The function and its derivative both are monotonic. Its mostly used in CNNs
     - No Vanishing gradient issue
     - The issue is that all the negative values become zero immediately which decreases the ability of the model to fit or train from the data properly.
   - Leaky ReLU
     - Range (-inf, inf)
     - It is an attempt to solve the dying ReLU problem
    
       

![Activation functions](https://github.com/bathejaakshay/ML-A-Z-notes/blob/main/Images/activation_functions.webp)
![Activation functions Derivatives](https://github.com/bathejaakshay/ML-A-Z-notes/blob/main/Images/activation_derivatives.webp)
