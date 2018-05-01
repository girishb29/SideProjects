# Support Vector Machines for Classification  
## Predicting Defective Products  
  
**By: Heather M. Steich, M.S.**  
**Date: March 27$^{th}$, 2018**  
**Written in: Python 3.4.5**  
  
---  
  
### Problem Statement  
  
Predict defective products from key process variables.  
  
---  
  
### Dataset Description  
  
Each row in the `*.csv` file corresponds to a product. Each product consists of 8 columns/features (f1-f8), which are key process variable measurement results collected from the production line. The “target” column contains the final test results of the product. Any product with a “target” measurement value less than 1,000 is considered a defective product.  
  
---  
  
### Goal  
  
Build an accurate machine learning model to predict whether the product is defective or not, given all the available features (excluding the “target” column).  

