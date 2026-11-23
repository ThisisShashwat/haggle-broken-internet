"""Deliberately broken: it needs the internet while predicting."""

import urllib.request

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
extra = urllib.request.urlopen("https://hackatime.hackclub.com/api/v1/stats", timeout=10).read()
guess = train["hours_spent"].mean()
pd.DataFrame({"project_id": test["project_id"], "hours_spent": guess}).to_csv("predictions.csv", index=False)
