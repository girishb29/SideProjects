# Client Churn Example, an Insurance Case

In this example, I'll use data from an insurance company.  The general business is that the insurance company collects premiums on a monthly basis from the clients.  In return, they pay the approved amount of a client's bills when there is a reported claim.  
  
The first section of the report details one approach to how I would estimate the remaining "value" of a customer, which is the total premium collected minus the total cost.  Additionally, I offer ideas of how the insurance company could use this estimate.  
  
The second section utilizes two CSV files containing data from the year 2016.  After initial data cleansing, reshaping, exploring and visualizing, I build a model to predict the probability of cancellation for each policy in the following month (January 2017).  The output file is a CSV file of the churn probabilities for each policy identification number (*PolicyID*).


