from .demand_trend import DemandCurve
from datetime import timedelta
from scipy.stats import linregress


class Forecast:
    def __init__(self, orders_df):
        self.orders_df = orders_df

        self._generate_weekly_trends()
        self._generate_monthly_trends()
        self._demand_model = DemandCurve(orders_df, 0.0, 0.0)

    def forcast_demand(self, price, sale_date):
        # get the day of the week
        week_day = sale_date.weekday()

        # get the month
        month = sale_date.month

        # get the trend for the day of the week
        week_day_trend = self.week_day_trend.get(week_day)

        # get the trend for the month
        month_trend = self.month_trend.get(month)

        # get the trend for the price
        price_trend = self._demand_model.predict_demand(price)
        price_trend = price_trend * self._demand_model.average_daily_sales

        # calculate the demand
        demand = price_trend * month_trend * week_day_trend * (1.0 + self.slope)

        return demand

    def forecast_thrity_days(self, price, sale_date):
        demand = []
        date = sale_date
        for _ in range(30):
            demand.append(self.forcast_demand(price, date))
            date = date + timedelta(days=1)

        return int(sum(demand))

    def _generate_weekly_trends(self):
        df = self.orders_df.copy()
        df["week_day"] = df["date"].dt.dayofweek
        del df["date"]

        week_day = df.groupby("week_day").sum()
        week_day_sums = df.groupby("week_day")["quantity"].sum()
        total_quantity = week_day_sums.sum()

        week_day["percentage"] = week_day["quantity"] / total_quantity

        self.week_day_trend = week_day["percentage"].to_dict()
        max_week = max(self.week_day_trend.values())
        for k, v in self.week_day_trend.items():
            self.week_day_trend[k] = v / max_week

        # create a dictionary of week day names and their corresponding trend
        self.week_day_trend_names = {
            "Monday": self.week_day_trend[0],
            "Tuesday": self.week_day_trend[1],
            "Wednesday": self.week_day_trend[2],
            "Thursday": self.week_day_trend[3],
            "Friday": self.week_day_trend[4],
            "Saturday": self.week_day_trend[5],
            "Sunday": self.week_day_trend[6],
        }

    def _generate_monthly_trends(self):
        df = self.orders_df.copy()
        df["month"] = df["date"].dt.month
        df["year"] = df["date"].dt.year
        del df["date"]

        month = df.groupby(["month", "year"]).sum().reset_index()
        month = month.sort_values(by=["year", "month"])

        units = list(month["quantity"])[:-1]
        x = list(range(len(units)))
        slope, _, _, _, _ = linregress(x, units)
        self.slope = slope / 100

        month = month.groupby("month").mean()
        total_quantity = month.sum()["quantity"]

        month["percentage"] = month["quantity"] / total_quantity

        self.month_trend = month["percentage"].to_dict()
        max_month = max(self.month_trend.values())

        for k, v in self.month_trend.items():
            self.month_trend[k] = v / max_month

        for i in range(1, 13):
            if i not in self.month_trend:
                self.month_trend[i] = 0.0

        # create a dictionary of month names and their corresponding trend
        self.month_trend_names = {
            "January": self.month_trend[1],
            "February": self.month_trend[2],
            "March": self.month_trend[3],
            "April": self.month_trend[4],
            "May": self.month_trend[5],
            "June": self.month_trend[6],
            "July": self.month_trend[7],
            "August": self.month_trend[8],
            "September": self.month_trend[9],
            "October": self.month_trend[10],
            "November": self.month_trend[11],
            "December": self.month_trend[12],
        }
