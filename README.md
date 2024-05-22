# Exchange-rates-api

## Project overview
   This project gets the exchange rates for given number of days (30) from AUD to  NZD exchanges rates, analyzes the json data and prints the worst, best and mean of the exchange rates. 
## Setup
  
### Prerequisites:

- Python 3.x and the following libraries to be installed:
- requests
- datetime
- pandas

### Installation
1. Clone the repository:
```
 git clone https://github.com/Rajesh-Tamada/Exchange-rates-api.git
```
2. Install the dependencies by running the following command:
```
 pip install requests datetime pandas
```

## Execution

 Command line: Open the command line interface and navigate to the directory where the script `CurrentExchange.py` is located and execute the following command:
   
   ```python CurrencyExchange.py``` 
   
OR

 Jupyter Notebook : Open jupyter Notebook and navigate to the directory where `exchange_rate.ipynb` file is located. Open the file and run the cells in the notebook to execute the script.
 
This will generate the following output in the command prompt or jupyter notebook:            
```
***********statistics*****************
worst exhange rate =  ***  on the date ****
best exhange rate =  ***  on the date ****
mean exhange rate =  ***
```

## Approach

The script has the following steps:

1. ### Data Acquisition: 
    - `get_historical_rates(base_currency, converted_currency, amount_of_days)` : This function builds the API request to get the exchange rates from exchangeratesapi for the given source , target and date range which is no of days past from current date to current date.
    - If there is any error in the response from API, this function loads the sample data from test.json. And the retrieved data is stored in a pandas DataFrame.
    - Please note that the current subscription plan does not support the API which is being used in this function. So it gives the following error and loads data from test.json.    
   ```
    Error: 403 Client Error: Forbidden for url: https://api.exchangeratesapi.io/v1/timeseries?access_key=b9cb3955b3ecdfe9632d1c45a1251bdd&base=AUD&start_date=2024-04-22&end_date=2024-05-
    22
    loading data from sample file.........
   ```
    
2. ### Data pre processing:
    - `pre_process_data(data)` : This function gets the dataframe from the response json and creates the dictionary to process the data and store it in desired format [ { date: <value>, exchange_rate: <value> }, ... ]
    - The desired format is then stored in pandas dataframe and returns for further processing.  

3. ### Data Cleanup:
    - `cleanup_data(df)` : This function checks data for duplicates and null values. Drops the duplicates and replaces nulls with mean value.  
    
4. ### statistics:
    - `get_worst_exchange_rate(df)`: This function returns min exchange rate value.  
    - `get_best_exchange_rate(df)`: This function returns max exchange rate value.   
    - `get_mean_exchange_rate(df)`: This function returns mean exchange rate value.   
    
5. ### Overall Execution:  
    - `main()` : This function takes care of invoking all the above functions sequentially and passes the result from one function to the other.  
    
## Testing

   - The code is return in TDD approach and all the functionality can be tested independently in the unit tests. All the tests are located in `test_CurrencyExchange.py`

### Tests Execution:
   - To run the tests, execute the following command from the terminal/command prompt within the project directory:
   ```
   python test_CurrencyExchange.py
```

### Test Coverage:
 - Below tests are written to test the functionality of all the functions:
 `test_historical_data_is_loaded()` - Verifies that the historical data is loaded and returned in dataframe.  
 `test_preprocess_data_is_created_with_desired_format()` - Verifies that the data is converted to the desired format.   
 `test_cleanup_data_remove_duplicates()` - This checks if the function cleanup removes the duplicate records.   
 `test_cleanup_data_replace_nulls_with_mean()` - This test verifies that the cleanup function replaces nulls with mean value.  
 `test_get_worst_exchange_rate_returns_min_value()` - This test verifies that the function returns expected min value.   
 `test_get_best_exchange_rate_returns_max_value()` - This verifies that the function returns expected max value.   
 `test_get_mean_exchange_rate_returns_mean_value()` - This verifies that the function returns expected mean value.   
