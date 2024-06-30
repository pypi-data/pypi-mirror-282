import numpy as np
import pandas as pd
import pymc as pm
import matplotlib.pyplot as plt

# Sample data generation function
def generate_data(start_date, end_date, n_points, group_values):
    dates = pd.date_range(start=start_date, end=end_date, periods=n_points)
    groups = np.random.choice(group_values, size=n_points)
    values = np.random.poisson(size=n_points) + groups * 0.5
    return pd.DataFrame({"date": dates, "group": groups, "value": values})


class Prophetoid:
    """Model inspired by Facebook's Prophet."""

    def __init__(self, date_col, target_col, group_cols, fourier_order=1):
        self.date_col = date_col
        self.target_col = target_col
        self.group_cols = group_cols
        self.fourier_order = fourier_order
        self.model = None

    def prepare_data(self, data):
        # Ensure the date column is in datetime format
        data[self.date_col] = pd.to_datetime(data[self.date_col])

        # Extracting the day of the week
        data["weekday"] = data[self.date_col].dt.dayofweek

        # Creating Fourier series terms for seasonality (365.24-day period)
        t = (
            data[self.date_col] - data[self.date_col].min()
        ).dt.total_seconds() / (24 * 3600)  # time in days since start

        for k in range(1, self.fourier_order + 1):
            data[f"cos_term_{k}"] = np.cos(2 * np.pi * k * t / 365.24)
            data[f"sin_term_{k}"] = np.sin(2 * np.pi * k * t / 365.24)

        return data

    def build_model(self, data):
        # Prepare data
        prepared_data = self.prepare_data(data.copy())

        # Extract the unique categories for the groupings
        coords = {col: prepared_data[col].unique().tolist() for col in self.group_cols}
        coords["weekday"] = np.arange(7).tolist()

        with pm.Model(coords=coords) as model:
            # Priors for fixed effects
            intercept = pm.Normal("intercept", mu=0, sigma=1)

            beta_cos = {}
            beta_sin = {}
            for k in range(1, self.fourier_order + 1):
                beta_cos[k] = pm.Normal(f"beta_cos_{k}", mu=0, sigma=1)
                beta_sin[k] = pm.Normal(f"beta_sin_{k}", mu=0, sigma=1)

            beta_weekday = pm.Normal("beta_weekday", mu=0, sigma=1, dims="weekday")

            # Random effects for groupings
            group_betas = {}
            for col in self.group_cols:
                group_betas[col] = pm.Normal(f"beta_{col}", mu=0, sigma=1, dims=col)

            # Construct the linear predictor
            mu = intercept
            for k in range(1, self.fourier_order + 1):
                X_cos = prepared_data[f"cos_term_{k}"].values
                X_sin = prepared_data[f"sin_term_{k}"].values
                mu += beta_cos[k] * X_cos + beta_sin[k] * X_sin

            X_weekday = prepared_data["weekday"].values
            mu += beta_weekday[X_weekday]

            for col in self.group_cols:
                X_group = pd.Categorical(prepared_data[col]).codes
                mu += group_betas[col][X_group]

            # Likelihood (observed data)
            lambda_ = pm.math.exp(mu)
            observed_data = prepared_data[self.target_col].values
            pm.Poisson("observed", mu=lambda_, observed=observed_data)

        self.model = model

    def fit(self, data, draws=1000, tune=1000):
        self.build_model(data)
        with self.model:
            self.trace = pm.sample(
                draws=draws,
                tune=tune,
                return_inferencedata=True,
                idata_kwargs={"log_likelihood": True},
            )

    def set_temporal_features(self, dates):
        """Set the temporal features for the given dates."""
        dates_df = pd.DataFrame({self.date_col: dates})
        dates_df[self.date_col] = pd.to_datetime(dates_df[self.date_col])
        dates_df["weekday"] = dates_df[self.date_col].dt.dayofweek

        t = (
            dates_df[self.date_col] - dates_df[self.date_col].min()
        ).dt.total_seconds() / (24 * 3600)

        # Compute Fourier series terms
        fourier_terms = np.zeros((len(dates_df), 2 * self.fourier_order))
        for k in range(1, self.fourier_order + 1):
            fourier_terms[:, 2 * k - 2] = np.cos(2 * np.pi * k * t / 365.24)
            fourier_terms[:, 2 * k - 1] = np.sin(2 * np.pi * k * t / 365.24)

        # Update model with the new temporal features
        self.model.set_data({
            f"cos_term_{k}": fourier_terms[:, 2 * k - 2] for k in range(1, self.fourier_order + 1)
        })
        self.model.set_data({
            f"sin_term_{k}": fourier_terms[:, 2 * k - 1] for k in range(1, self.fourier_order + 1)
        })
        self.model.set_data({"weekday": dates_df["weekday"].values})

    def predict(self, dates):
        # Set temporal features for prediction dates
        self.set_temporal_features(dates)

        # Use pymc.sample_posterior_predictive to generate posterior predictive samples
        with self.model:
            posterior_pred = pm.sample_posterior_predictive(
                trace=self.trace,
                var_names=["observed"],
                random_seed=2018,
                predictions=True
            ).predictions

        return posterior_pred


# Example usage with sample data
if __name__ == "__main__":
    # Generate sample data
    np.random.seed(0)
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    n_points = 365
    group_values = [0, 1, 2]
    data = generate_data(start_date, end_date, n_points, group_values)

    # Instantiate and fit Prophetoid model
    model = Prophetoid(date_col="date", target_col="value", group_cols=["group"], fourier_order=2)
    model.fit(data)

    # Generate prediction dates
    prediction_dates = pd.date_range(start="2024-01-01", end="2024-01-10")

    # Make predictions
    predictions = model.predict(prediction_dates)

    # Plotting example (just a simple plot of predictions)
    plt.figure(figsize=(10, 6))
    plt.plot(data["date"], data["value"], label="Observed")
    plt.plot(prediction_dates, predictions["observed"].mean(axis=0), label="Predicted", linestyle="--")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Observed vs Predicted Values")
    plt.legend()
    plt.show()

