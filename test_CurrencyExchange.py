import CurrencyExchange
from CurrencyExchange import *
import pandas as pd

def test_historical_data_is_loaded():
    pd.testing.assert_frame_equal(pd.read_json("test.json"), get_historical_rates('AUD','NZD',30))

def test_preprocess_data_is_created_with_desired_format():
    data = {
               "start_date": "2012-05-01",
               "end_date": "2012-05-03",
               "base": "AUD",
               "rates": {
                   "2012-05-01":{
                     "NZD": 1.0653
                   },
                   "2012-05-02": {
                      "NZD": 1.05999
                   }
              }
           }

    expectedData = {'date' : ["2012-05-01", "2012-05-02" ], 'exchange_rate' : [1.0653, 1.05999]}
    pd.testing.assert_frame_equal(pd.DataFrame(expectedData), pre_process_data(data))


def test_cleanup_data_remove_duplicates():
    data = {'date' : ["2012-05-01", "2012-05-01" ], 'exchange_rate' : [1.0653, 1.0653]}
    actualData = cleanup_data(pd.DataFrame(data))
    expectedData = {'date' : ["2012-05-01" ], 'exchange_rate' : [1.0653]}
    pd.testing.assert_frame_equal(pd.DataFrame(expectedData), actualData)

def test_cleanup_data_replace_nulls_with_mean():
    data = {'date' : ["2012-05-01", "2012-05-02" ], 'exchange_rate' : [1.0653, None]}
    actualData = cleanup_data(pd.DataFrame(data))
    expectedData = {'date' : ["2012-05-01", "2012-05-02" ], 'exchange_rate' : [1.0653, 1.0653]}
    pd.testing.assert_frame_equal(pd.DataFrame(expectedData), actualData)

def test_get_worst_exchange_rate_returns_min_value():
    data = {'date' : ["2012-05-01", "2012-05-02" ], 'exchange_rate' : [1.0653, 1.05999]}
    actualData = get_worst_exchange_rate(pd.DataFrame(data))
    assert actualData == 1.05999

def test_get_best_exchange_rate_returns_max_value():
    data = {'date' : ["2012-05-01", "2012-05-02" ], 'exchange_rate' : [1.0653, 1.05999]}
    actualData = get_best_exchange_rate(pd.DataFrame(data))
    assert actualData == 1.0653

def test_get_mean_exchange_rate_returns_mean_value():
    data = {'date' : ["2012-05-01", "2012-05-02" ], 'exchange_rate' : [1.0653, 1.05999]}
    actualData = get_mean_exchange_rate(pd.DataFrame(data))
    assert actualData == 1.0626449999999998

if __name__ == "__main__":
    test_historical_data_is_loaded()
    test_preprocess_data_is_created_with_desired_format()
    test_cleanup_data_remove_duplicates()
    test_cleanup_data_replace_nulls_with_mean()
    test_get_worst_exchange_rate_returns_min_value()
    test_get_best_exchange_rate_returns_max_value()
    test_get_mean_exchange_rate_returns_mean_value()
    print("All tests passed")