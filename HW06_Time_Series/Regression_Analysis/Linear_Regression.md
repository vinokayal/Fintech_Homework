# Linear Regression
### A Yen for the Future
  This assignment is to predict Yen's future movements against the U.S. dollar.
  
#### Time Series Forecasting
**Step 1:**
Load Important Libraries

* Pandas

* Numpy

* Matplotlib

**Step 2:**
Load CSV file (Yen.CSV)

* Using PATH specify the file path for Yen.CSV

* Using pandas function pd.read_csv, read the CSV file

**Step 3:**
Slice the data in uploaded Data Frame and create new Data Frame (Yen_Futures)

* Slice the Data in the Yen_data and move it to new Data Frame using .loc function.

```markdown
yen_futures=yen_data.loc["1990-01-01":,:]
```
**Step 4:**

```markdown
returns=(yen_data[['Settle']].pct_change()*100)
returns=returns.replace(-np.inf,np.nan).dropna()
yen_data['Return']=returns.copy()
yen_data['Lagged_Return']=returns.shift()
yen_data = yen_data.dropna()
```
**Step 5:**
Divide the Dataset

```markdown
train=yen_data[:"2017"]
test=yen_data['2018':]
X_train=train["Lagged_Return"].to_frame()
X_test=test["Lagged_Return"].to_frame()
y_train=train["Return"]
y_test=test["Return"]
```
**Step 6:**

```markdown
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
Results = y_test.to_frame()
Results["Predicted Return"] = predictions
```
**Step 7:**

```markdown
|Date       | Return  |Predicted Return| 
|-----------|---------| ---------------|
|2018-01-02 |0.297285 |-0.009599       |
|-----------|---------| ---------------|
|2018-01-03 |-0.240479|-0.010033      |
```

**Step 8:**
```markdown
from sklearn.metrics import mean_squared_error, r2_score
# Calculate the mean_squared_error (MSE) on actual versus predicted test "y" 
# (Hint: use the dataframe above)
mse = mean_squared_error(
    Results["Return"],
    Results["Predicted Return"]
)

# Using that mean-squared-error, calculate the root-mean-squared error (RMSE):
rmse = np.sqrt(mse)
print(f"Out-of-Sample Root Mean Squared Error (RMSE): {rmse}")
```
**Out-of-Sample Root Mean Squared Error (RMSE): 0.41545437184712763**

**Step 9:**
```markdown
# Construct a dataframe using just the "y" training data:
in_sample_results = y_train.to_frame()

# Add a column of "in-sample" predictions to that DataFrame:  
in_sample_results["In-sample Predictions"] = model.predict(X_train)

# Calculate in-sample mean_squared_error (for comparison to out-of-sample)
in_sample_mse = mean_squared_error(
    in_sample_results["Return"],
    in_sample_results["In-sample Predictions"]
)

# Calculate in-sample root mean_squared_error (for comparison to out-of-sample)
in_sample_rmse = np.sqrt(in_sample_mse)
print(f"In-sample Root Mean Squared Error (RMSE): {in_sample_rmse}")
```
**In-sample Root Mean Squared Error (RMSE): 0.5962037920929946**