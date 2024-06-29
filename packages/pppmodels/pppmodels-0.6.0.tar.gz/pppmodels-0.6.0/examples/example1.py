import pandas as pd
import numpy as np
import pymc as pm

# Example data generation
np.random.seed(42)

# Generate example data
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
data = pd.DataFrame({
    'date': dates,
    'target': np.random.poisson(lam=5, size=len(dates)),
    'group_col1': np.random.choice(['A', 'B', 'C'], size=len(dates)),
    'group_col2': np.random.choice(['X', 'Y', 'Z'], size=len(dates))
})

# Instantiate Prophetoid model
prophet = Prophetoid(data=data,
                     date_col='date',
                     target_col='target',
                     group_cols=['group_col1', 'group_col2'],
                     fourier_order=2)

# Build the Bayesian model
prophet.build_model()

# Fit the model
prophet.fit(draws=1000, tune=1000)

# Example usage to predict for a set of dates
prediction_dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')

# Generate predictions using the model
predictions = prophet.predict(dates=prediction_dates)

# Display predictions
for date, prediction in zip(prediction_dates, predictions):
    print(f"Prediction for {date.date()}: {prediction.mean():.2f} (mean), {np.percentile(prediction, 10):.2f} (10th percentile), {np.percentile(prediction, 90):.2f} (90th percentile)")

