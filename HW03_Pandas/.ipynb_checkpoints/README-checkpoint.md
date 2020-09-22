# A whale off the Portfolio
The requirement is to validate algorithm trading strategies and determine the best performing portfolio across many areas like  volatility, returns, risk, and Sharpe ratios.
## Pseudo code:

### Library Imports:
```sh
1.  Import all libraries like Pandas, Numpy
2.  Include Matplotlib
3.  Import Path to load CSV files
```
### Load CSV file:
1. Load Algo trading file using Path
2. Load Whale data file using Path
3. Load SP500 data file using Path
### Read the CSV file:
Read the csv file using read_csv command and along with that set index value and parse dates for all the upload.
1. Read Algo trading file and assign values to Algo_data dataframe.
2. Read Whale data file and assign the values to Whale_data dataframe.
3. Read SP500 data file and assign the values to SP500 data dataframe.
### Sort the data in dataframe:
1. Sort Algo data in ascending order with Ascending=True
2. Sort Whale data in ascending order with Ascending = True
3. Sort Sp500 data in ascending order with Ascending =True
### View the sample data:
1. View the sample data in Algo trading using head()
2. View the sample data in Whale data using head()
3. View the sample data in SP500 data using head()
### Identify null and remove Null values in Dataframes:
1. Identify null values in the the dataframe using isnull() function and sum it.
```sh
    Algo_data.isnull().sum()
    Whale_data.isnull().sum()
    SP500_data.isnull().sum()
```
2. Drop the null values from dataframe.
```sh
    dropna(inplace=True)
```
### Remove the $ and change the data type for the column 
    sp500_upd["Close"] = sp500_upd["Close"].str.replace('$', '').astype('float64')

### Calculate the daily returns on SP500 data
```sh
    pct_change() function calculates daily returns
```
### Join the different data frames:
    Concat(<dataframe1>,<dataframe2>, axis=columns & Join= Inner)
The above function is to combine multiple data types with join as Inner and drop null using dropna() function.Algo_trade, Whale_data are already having daily returns and it should be combined with daily returns of SP500_data.

### Plot the graph for the combined data set:
plot() function is used to plot the graph for the combined data frame.
```sh
     portfolio_combined.plot(figsize=(30,15), title="Daily Returns");  
```
### Calculate Cumulative Returns
```sh
    cumulative_returns = (1+ portfolio_combined).cumprod()
```
### Plot the graph and box for the combined dataframe
```sh
    portfolio_combined.plot.box(figsize=(30,15));
```
### Calculate the standard deviation for the combined dataframe
portfolio_daily_std = portfolio_combined.std()
### Verify 
portfolio_daily_std > portfolio_daily_std ['S&P 500']
### Calculate the Rolling Window 
portfolio_combined.rolling(window=21).std().plot(figsize=(30,15), title="21 Day Rolling Standard Deviation");
### Identify the Correlation between data:
portfolio_correlation=portfolio_combined.corr()

### Calculate Beta for Tiger Global Management LLC:
```sh
portfolio_TGR_rolling_covariance=portfolio_combined['TIGER GLOBAL MANAGEMENT LLC'].rolling(window=30).cov(portfolio_combined['S&P 500'])
```
### Calculate Sharp Ratios:
```sh
portfolio_sharp_ratios=(portfolio_combined.mean()*252)/(portfolio_combined.std()*np.sqrt(252))
```
### Plot graph for Sharp Ratios:
```sh
portfolio_sharp_ratios.plot(kind="bar", title="Sharpe Ratios");
```
### Upload 3 custom data files (GOOG, APPL,COST)
```sh
cost_upload = Path("<file path>")
goog_upload = Path("<file path>")
aapl_upload = Path("<file path>")
appl_data=pd.read_csv(aapl_upload,index_col="Trade DATE",parse_dates=True,infer_datetime_format=True)
cost_data=pd.read_csv(cost_upload,index_col="Trade DATE",parse_dates=True,infer_datetime_format=True)
goog_data=pd.read_csv(goog_upload,index_col="Trade DATE",parse_dates=True,infer_datetime_format=True)
```
### Combined all the data sheet into single dataframe
```sh
usr_portfolio=pd.concat([appl_upd,cost_data,goog_data],axis='rows',join='inner')
usr_portfolio.dropna(inplace=True)
usr_portfolio.head()
```
### Pivot the dataframe
```sh
usr_portfolio_upd=usr_portfolio.pivot(columns="Symbol",values="NOCP")
usr_portfolio_upd.dropna(inplace=True)
usr_portfolio_upd
```
### Caculate the daily returns
```sh
usr_portfolio_rtns=usr_portfolio_upd.pct_change()
usr_portfolio_rtns.dropna(inplace=True)
usr_portfolio_rtns.head()
```
### Assging the weights and calculate the risk
```sh
weights=[1/3,1/3,1/3]
usr_pf_wg_rtns=usr_portfolio_rtns.dot(weights)
usr_pf_wg_rtns.head()
```
### Combine the Custom dataframe to the combined whale dataframe
```sh
new_portfolio_combined = pd.concat([portfolio_combined,usr_pf_wg_rtns], axis='columns', join='inner')
```
### Rename the column name
```sh
new_portfolio_combined=new_portfolio_combined.rename(columns={0:"Custom"})
```
### Calculate the daily std
```sh
combined_pf_daily_std = new_portfolio_combined.std()
print(combined_pf_daily_std)
```
### Calculate the Annual Standard Deviation
```sh
combined_portfolio_annual_std=combined_pf_daily_std*np.sqrt(252)
print(combined_portfolio_annual_std)
```
### Calucate Sharp Ratios for the Custom Combined Portfolio.
```sh
combined_portfolio_sharpe_ratios = (new_portfolio_combined.mean() * 252) / (new_portfolio_combined.std() * np.sqrt(252))
combined_portfolio_sharpe_ratios
```
### Calculate the Correlation for the Combined Portfolio:
```sh
combined_portfolio_correlation=new_portfolio_combined.corr()
```
### Caculate Rolling Covariance & Variance for Custom Portfolio:
```sh
portfolio_custom_rolling_covariance=new_portfolio_combined['Custom'].rolling(window=30).cov(new_portfolio_combined['S&P 500'])
new_portfolio_rolling_variance=new_portfolio_combined['S&P 500'].rolling(window=30).var()
```
### Calculate Beta for Custom Portfolio:
Calculated Beta stored in portfolio_Custom_Beta.
```sh
portfolio_Custom_Beta=portfolio_custom_rolling_covariance / new_portfolio_rolling_variance
```
### plot the graph for custom portfolio:
```sh
portfolio_Custom_Beta.plot(figsize=(30,15),title="Custom Portfolio Beta");
```