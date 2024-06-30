import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc as pm

from scipy.special import expit as inverse_logit

RANDOM_SEED = 8927
rng = np.random.default_rng(RANDOM_SEED)
az.style.use("arviz-darkgrid")

# Number of data points
n = 250
# Create features
x1 = rng.normal(loc=0.0, scale=2.0, size=n)
x2 = rng.normal(loc=0.0, scale=2.0, size=n)
# Define target variable
intercept = -0.5
beta_x1 = 1
beta_x2 = -1
beta_interaction = 2
z = intercept + beta_x1 * x1 + beta_x2 * x2 + beta_interaction * x1 * x2
p = inverse_logit(z)
# note binomial with n=1 is equal to a Bernoulli
y = rng.binomial(n=1, p=p, size=n)
df = pd.DataFrame(dict(x1=x1, x2=x2, y=y))
df.head()

labels = ["Intercept", "x1", "x2", "x1:x2"]
df["Intercept"] = np.ones(len(df))
df["x1:x2"] = df["x1"] * df["x2"]
# reorder columns to be in the same order as labels
df = df[labels]
x = df.to_numpy()

indices = rng.permutation(x.shape[0])
train_prop = 0.7
train_size = int(train_prop * x.shape[0])
training_idx, test_idx = indices[:train_size], indices[train_size:]
x_train, x_test = x[training_idx, :], x[test_idx, :]
y_train, y_test = y[training_idx], y[test_idx]


coords = {"coeffs": labels}

with pm.Model(coords=coords) as model:
    # data containers
    X = pm.MutableData("X", x_train)
    y = pm.MutableData("y", y_train)
    # priors
    b = pm.Normal("b", mu=0, sigma=1, dims="coeffs")
    # linear model
    mu = pm.math.dot(X, b)
    # link function
    p = pm.Deterministic("p", pm.math.invlogit(mu))
    # likelihood
    pm.Bernoulli("obs", p=p, observed=y)


with model:
    idata = pm.sample()

with model:
    pm.set_data({"X": x_test, "y": y_test})
    pm.sample_posterior_predictive(trace=idata)
