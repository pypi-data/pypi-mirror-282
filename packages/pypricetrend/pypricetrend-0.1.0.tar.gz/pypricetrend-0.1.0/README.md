# pypricetrend

## Introduction

The `pypricetrend` package provides tools to analyze and forecast product demand based on historical sales data. It includes the `DemandCurve` class for generating demand curves and the `Forecast` class for predicting future demand.

## Classes

### DemandCurve

The `DemandCurve` class generates demand curves for a given product.

#### Initialization

To initialize the `DemandCurve` class, you need to provide a DataFrame containing the columns `price`, `quantity`, and `date`, as well as the `landed_cost` and `fulfillment_cost` of the product.

```python
from pypricetrend import DemandCurve
import pandas as pd

# Sample data
data = {
    'price': [10, 20, 15, 25, 30],
    'quantity': [100, 80, 90, 70, 60],
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'])
}
orders_df = pd.DataFrame(data)

# Initialize the DemandCurve class
landed_cost = 5.0
fulfillment_cost = 2.0
demand_curve = DemandCurve(orders_df, landed_cost, fulfillment_cost)
```

#### Predicting Demand

You can predict the demand for a given price using the `predict_demand` method.

```python
price = 22.5
predicted_demand = demand_curve.predict_demand(price)
print(f"Predicted demand for price {price}: {predicted_demand}")
```

#### Plotting the Demand Curve
You can plot the demand curve for the given product using the `plot_demand_curve method`.

```python
demand_curve.plot_demand_curve()
```

#### Saving and Loading the Model
You can save the demand curve model to a file and load it later.

````python
# Save the model
demand_curve.save_model('demand_curve_model.npy')

# Load the model
demand_curve.load_model('demand_curve_model.npy')
````

### Forecast
The `Forecast` class predicts future demand based on historical sales data.

#### Initialization
To initialize the `Forecast` class, you need to provide a DataFrame containing the columns `price`, `quantity`, and `date`


```python
from pypricetrend import Forecast
import pandas as pd

# Sample data
data = {
    'price': [10, 20, 15, 25, 30],
    'quantity': [100, 80, 90, 70, 60],
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'])
}
orders_df = pd.DataFrame(data)

# Initialize the Forecast class
forecast = Forecast(orders_df)
```

#### Forecasting Demand
You can forecast the demand for a given price and sale date using the forcast_demand method.

```python
Forecasting Demand
You can forecast the demand for a given price and sale date using the forcast_demand method.
```

#### Forecasting for the Next 30 Days
You can forecast the demand for the next 30 days using the `forecast_thrity_days` method.

## Installation
```shell
pip install pypricetrend
```
