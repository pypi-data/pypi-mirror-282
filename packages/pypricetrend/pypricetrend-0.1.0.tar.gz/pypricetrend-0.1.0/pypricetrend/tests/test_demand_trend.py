import pandas as pd
import numpy as np
import unittest
from sklearn.linear_model import LinearRegression
from ..demand_trend import DemandCurve

class DemandCurveTests(unittest.TestCase):
    def setUp(self):
        # Create a sample orders DataFrame
        orders_data = {
            "price": [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50],
            "quantity": [100, 80, 60, 40, 20, 100, 80, 60, 40, 20, 100, 80, 60, 40, 20, 100, 80, 60, 40, 20],
            "date": pd.date_range(start="2022-01-01", periods=20),
        }
        self.orders_df = pd.DataFrame(orders_data)

        # Create a sample DemandCurve instance
        self.demand_curve = DemandCurve(self.orders_df, landed_cost=5, fulfillment_cost=2)

    def test_generate_demand_curves(self):
        
        # Check if demand, prices, and profit attributes are not empty
        self.assertTrue(len(self.demand_curve.demand) > 0)
        self.assertTrue(len(self.demand_curve.prices) > 0)
        self.assertTrue(len(self.demand_curve.profit) > 0)

    def test_predict_demand(self):
        # Test if demand prediction is correct for a given price
        price = 25
        expected_demand = self.demand_curve.lin_mdl.predict(np.array([[price]]))[0]
        predicted_demand = self.demand_curve.predict_demand(price)
        self.assertEqual(predicted_demand, expected_demand)

    def test_calculate_price_elasticity(self):
        # Test if price elasticity is calculated correctly
        expected_price_elasticity = (
            self.demand_curve.lin_mdl.coef_[0]
            * (np.mean(self.demand_curve.prices) / np.mean(self.demand_curve.demand))
        )
        calculated_price_elasticity = self.demand_curve._calculate_price_elasticity()
        self.assertEqual(np.round(calculated_price_elasticity, 3), np.round(expected_price_elasticity, 3))

    def test_get_step_size(self):
        # Test if step size is returned correctly for different price ranges
        self.assertEqual(DemandCurve.get_step_size(3), 0.05)
        self.assertEqual(DemandCurve.get_step_size(7), 0.10)
        self.assertEqual(DemandCurve.get_step_size(20), 0.25)
        self.assertEqual(DemandCurve.get_step_size(80), 0.5)
        self.assertEqual(DemandCurve.get_step_size(150), 1.0)

    def test_round_price_to_step_size(self):
        # Test if price is rounded correctly to the nearest step size
        self.assertEqual(DemandCurve.round_price_to_step_size(3.2), 3.20)
        self.assertEqual(DemandCurve.round_price_to_step_size(7.6), 7.60)
        self.assertEqual(DemandCurve.round_price_to_step_size(20.3), 20.25)
        self.assertEqual(DemandCurve.round_price_to_step_size(80.7), 80.50)
        self.assertEqual(DemandCurve.round_price_to_step_size(150.9), 151.00)

    def test_fit_model(self):
        # Test if linear regression model is fitted correctly
        data = pd.DataFrame({
            "normalized_price": [1, 2, 3, 4, 5],
            "total_order_count": [100, 80, 60, 40, 20]
        })
        expected_model = LinearRegression()
        expected_model.fit(np.array(data["normalized_price"]).reshape(-1, 1), np.array(data["total_order_count"]))
        fitted_model = DemandCurve._fit_model(data)
        self.assertEqual(fitted_model.coef_, expected_model.coef_)
        self.assertEqual(fitted_model.intercept_, expected_model.intercept_)


if __name__ == "__main__":
    unittest.main()