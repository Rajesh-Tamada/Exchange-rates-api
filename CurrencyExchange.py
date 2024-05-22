# Notebook to connect exchange rate api and stream the data 
import requests
import pandas as pd
import datetime

def get_historical_rates(base_currency, converted_currency, amount_of_days):

    # sets the start date
    today_date = datetime.datetime.now()
    date_1month = (today_date - datetime.timedelta(days=1 * amount_of_days))

    #send the request
    try:
        url = f'https://api.exchangeratesapi.io/v1/timeseries'
        payload = {'access_key': 'b9cb3955b3ecdfe9632d1c45a1251bdd', 'base': base_currency, 'start_date': date_1month.date(), 'end_date': today_date.date()}
        response = requests.get(url, params=payload)
        response.raise_for_status()
        data = pd.read_json(response.json())
        return data
    except Exception as e:
        print("Error:", e)
        # load sample file
        print("loading data from sample file.........")
        data = pd.read_json("test.json")
        return data

# Pre processing the files to desigred structure
def pre_process_data(data):
    
    # Desired format:
    # [ { date: <value>, exchange_rate: <value> }, ... ]
    # Get 'rates' from the result set
    rates_by_date = data['rates']
    # Convert the dictionary into desired format
    hist_data = []
    for key, value in rates_by_date.items():
        hist_dict = {'date': key, 'exchange_rate': value['NZD']}
        hist_data.append(hist_dict)
    # create dataframe for computing
    df = pd.DataFrame(hist_data)    
    return df

# Data check and replace for datatypes, nulls etc 
def cleanup_data(df):

    #Replace the records with mean value for which the rate is null
    df['exchange_rate'] = df['exchange_rate'].fillna((df['exchange_rate'].mean()))

    #Drop duplicates
    df.drop_duplicates(inplace = True)

    return df

# trasformation methods to call
def get_worst_exchange_rate(df):
    return df['exchange_rate'].min()

def get_best_exchange_rate(df):
    return df['exchange_rate'].max()

def get_mean_exchange_rate(df):
    return df['exchange_rate'].mean()


def main():
    data = get_historical_rates('AUD','NZD',30)
    processed_data = pre_process_data(data)
    result = cleanup_data(processed_data)
    min = get_worst_exchange_rate(result)
    max = get_best_exchange_rate(result)
    mean = get_mean_exchange_rate(result)
    
    print("***********statistics*****************")
    print("worst exhange rate = ", min , " on the date",  result.loc[result.exchange_rate.idxmin(), 'date'])
    print("best exhange rate = ", max, " on the date",  result.loc[result.exchange_rate.idxmax(), 'date'])
    print("mean exhange rate = ", mean)

if __name__ == "__main__":
    main()