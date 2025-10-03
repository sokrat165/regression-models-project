# regression-models-project
# Regression Models Project This project demonstrates different regression techniques and their applications, including methods to handle overfitting and multicollinearity.
## Models Implemented
- Linear Regression 
-Simple 
- Multiple 
- Polynomial 
- Ridge Regression (L2 Regularization) 
- Lasso Regression (L1 Regularization) 
## Workflow 
1. Train and compare Linear, Ridge, and Lasso regression models. 
2. Evaluate models using **K-Fold Cross Validation**. 
3. Store model parameters (coefficients, intercepts). 
4. Build a script to reload parameters and serve predictions via an **API**. 
5. Handle scaling by saving and reusing the scaler object for new inputs. 
## Key Points 
- Ridge improves stability and reduces multicollinearity. 
- Lasso performs feature selection by removing irrelevant features. 
- Both methods reduce overfitting and improve generalization. 
- Proper scaling and saving of parameters are required for accurate deployment. 
## Requirements 
- Python 3.x 
- scikit-learn 
- pandas 
- numpy 
- joblib 
- FastAPI (for API deployment)
