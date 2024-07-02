import pandas as pd
import unittest
import datetime
from scipy.stats import linregress
from ..forecast import Forecast

class ForecastTests(unittest.TestCase):
    def setUp(self):
        # Create a sample orders DataFrame
        orders_data = {
            "price": [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50],
            "quantity": [100, 80, 60, 40, 20, 100, 80, 60, 40, 20, 100, 80, 60, 40, 20, 100, 80, 60, 40, 20],
            "date": [
                datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 2), datetime.datetime(2022, 1, 3),
                datetime.datetime(2022, 2, 4), datetime.datetime(2022, 2, 5), datetime.datetime(2022, 1, 6),
                datetime.datetime(2022, 3, 7), datetime.datetime(2022, 3, 8), datetime.datetime(2022, 3, 9),
                datetime.datetime(2022, 4, 10), datetime.datetime(2022, 4, 11), datetime.datetime(2022, 4, 12),
                datetime.datetime(2022, 5, 13), datetime.datetime(2022, 5, 14), datetime.datetime(2022, 5, 15),
                datetime.datetime(2022, 6, 16), datetime.datetime(2022, 6, 17), datetime.datetime(2022, 6, 18),
                datetime.datetime(2022, 7, 19), datetime.datetime(2022, 7, 20),
            ],
        }
        self.orders_df = pd.DataFrame(orders_data)
        self.forecast = Forecast(self.orders_df)

    def test_generate_monthly_trends(self):
        # Test if monthly trends are generated correctly
        expected_month_trend = {
            "January": 1.0,
            "February": 0.17647058823529413,
            "March": 0.5294117647058824,
            "April": 0.5882352941176471,
            "May": 0.35294117647058826,
            "June": 0.7058823529411765,
            "July": 0.17647058823529413,
            "August": 0,
            "September": 0,
            "October": 0,
            "November": 0,
            "December": 0,
        }
        self.assertEqual(self.forecast.month_trend_names, expected_month_trend)


if __name__ == "__main__":
    unittest.main()