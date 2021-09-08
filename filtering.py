import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("star_with_gravity.csv")

boolean =[]
for d in df.Distance:
  if d<=100:
    boolean.append(True)
  else:
    boolean.append(False)

is_dist = pd.Series(boolean)

star_dist=df[is_dist]

star_dist.reset_index(inplace=True,drop=True)

gravity_boolean = []
for g in star_dist.Gravity:
  if g<=350 and g>=150:
    gravity_boolean.append(True)
  else :
    gravity_boolean.append(False)

is_gravity = pd.Series(gravity_boolean)

final_stars = star_dist[is_gravity]

final_stars.reset_index(inplace=True,drop=True)

final_stars.to_csv("filtered_stars.csv")