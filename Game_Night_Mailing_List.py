import pandas as pd

# Open Mailing List
games_night_list = pd.read_excel("Games Night Mailing List.xlsx")
df = pd.DataFrame(games_night_list)

# Counts the number of times a person has declined
decline = {"x"}
df["Total"] = df.isin(decline).sum(1)

# Removes person off the mailing list if they decline 3 times
df = df.drop(df[df.Total >= 3].index)

# Updates the mailing list
f = open("Games Night Mailing List.xlsx", "w")
df.to_excel("Games Night Mailing List.xlsx", index=False)