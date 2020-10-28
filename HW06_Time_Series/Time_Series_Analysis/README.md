# Time Series Analysis
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
Plot the graph for only Settle column in Yen_Futures

```markdown
ax=yen_futures['Settle'].plot(figsize=(12,8),color="Orange",legend=True);
ax.xaxis.grid(True)
ax.yaxis.grid(True)
```
**Step 5:**
Import library for hp filters and derive noise and trend the in the data

```markdown
import statsmodels.api as sm
ts_noise,ts_trend=sm.tsa.filters.hpfilter(yen_futures['Settle'])
```
**Step 6:**
Create Data Frame using derived data

```markdown
yen_upd=pd.DataFrame({
    "Noise":ts_noise,
    "Trend":ts_trend,
})
```
**Step 7:**
Plot graph for the new data frame Yen_upd(Settle vs Trend)

```markdown
ax=yen_upd[['Settle','Trend']]['2015-01-01':].plot(figsize=(12,8),legend=True,title="Settle vs Trend");
```
**Step 8:**
Plot graph for the Noise

```markdown
yen_upd['Noise'].plot(figsize=(12,8),title="Noise");
```
## Forecasting Returns using an ARMA Model

**Step 9:**
```markdown
from statsmodels.tsa.arima_model import ARMA
returns=(yen_upd[['Settle']].pct_change()*100)
returns=returns.replace(-np.inf,np.nan).dropna()
```

**Step 10:**
```markdown
model = ARMA(returns.values, order=(2,1))
results=model.fit()
results.summary()
```

**Step 11:**
Forecast the values
```markdown
pd.DataFrame(results.forecast(steps=5)[0]).plot(title="5 Day Returns Forcast");
```
## Forecasting Returns using an ARIMA Model

**Step 12:**
```markdown
from statsmodels.tsa.arima_model import ARIMA
model = ARIMA(yen_futures['Settle'], order=(5, 1, 1))
results_1=model.fit()
results_1.summary()
```
**Step 13:**
```markdown
pd.DataFrame(results_1.forecast(steps=5)[0]).plot(title="5 Day Futures Price Forecast");
```
## Volatility Forecasting with GARCH
**Step 14:**
```markdown
from arch import arch_model
model = arch_model(returns, mean="Zero", vol="GARCH", p=2, q=1)
result_3=model.fit(disp="off")
result_3.summary()
```
## Co variance Estimator
**Step 15:**
```markdown
last_day = returns.index.max().strftime('%Y-%m-%d')
forecast_horizon = 5
forecasts = result_3.forecast(start='2019-10-15', horizon=forecast_horizon)
intermediate = np.sqrt(forecasts.variance.dropna() * 252)
```
```markdown
|Date       | h.1    |h.2     |h.3     |h.4     |h.5     |
|-----------|--------| -------|--------|--------|--------|
|2019-10-15 |7.434048|7.475745|7.516867|7.557426|7.597434|
```
##  Visualizing the forecast
**Step 16:**
```markdown
final = intermediate.dropna().T
```
```markdown
|Date|2019-10-15| 
|----|----------|
|h.1 |7.434048  |
|h.2 |7.475745  |
|h.3 |7.516867  |
|h.4 |7.557426  |
|h.6 |7.597434  |
```
**Step 17:**
```markdown
final = intermediate.dropna().T
```
### Questions
Based on your time series analysis, would you buy the yen now?

    Yes, i will buy yen. Prediction is good

Is the risk of the yen expected to increase or decrease?

    Decrease
    
Based on the model evaluation, would you feel confident in using these models for trading?
Yes, model is promising.