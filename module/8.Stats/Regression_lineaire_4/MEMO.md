- Intercept: Linear function $\hat{y}$ that fit $y$
- Slope: Coeff of the intercept
- coeffiscient: $b_0, ... , b_n$ in $\hat{y} = b_0 + \sum_{i=1}^n b_i x_i$
- Sum of Squares of Residuals (SSR)
- Sum Square totals (SST)
- Metric R²
$$ R² = 1 - \frac{SSR}{SST}= 1 -\frac{\sum_{i=1}^n (y_i − \hat{y}_i)^2}{\sum_{i=1}^n (y_i − \bar{y}_i)^2}$$

- Metric Mean Square Error (MSE) and RMSE (root MSE)
$$ MSE = \frac{1}{n} \sum_{i=1}^n (y_i − \hat{f}(x_i))^2 $$

$$ RMSE = \sqrt{MSE}$$
- metric Mean Absolute Error (MAE)
$$ MAE = \frac{\sum_{i=1}^n |y_i − \hat{f}(x_i)|}{n} (Mean Absolute Average)$$

- metric Variance inflation factor $VIF_i$
$$ VIF_i = \frac{1}{1-R_i^2}$$
 Where $R_i^2$ is the $R^2$ of $x_i = affine(x_{j\ne i})$

 - supervized learning: The target is given in the data

 - unsupervized learning: The target is not given in the data

 - classification/regression: The target is categoric/Numeric
 - parametric/
Non-parametric models

- overfitting/underfitting: Too much/ Not enough descriptive variables for the target

- bias/variance tradeoff

- cross-validation: 




