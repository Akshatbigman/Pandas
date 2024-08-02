
import pandas as pd
import matplotlib.pyplot as plt

ipl = pd.read_csv("matches.csv", index_col = "id")

ipl.head()
ipl.tail()

ipl.shape

ipl["player_of_match"].value_counts(10)

ipl['season'].max()

ipl['player_of_match'].head(10)

ipl["player_of_match"].value_counts()[0:10]

ipl["player_of_match"].value_counts()[0:5].plot(kind = "bar")

plt.figure(figsize = (5,5))
plt.bar(list(ipl["player_of_match"].value_counts()[0:5].keys()), list(ipl["player_of_match"].value_counts()[0:5]))
plt.show()

ipl["player_of_match"].value_counts()[0:5].keys()

ipl = pd.read_csv("/content/drive/MyDrive/Untitled folder/Dataset/matches.csv", index_col = "id")

ipl['toss_winner'].value_counts()

batting_first = ipl[ipl['win_by_runs'] != 0]
batting_first.head()

plt.figure(figsize = (7,7))
plt.hist(batting_first['win_by_runs'])
plt.show()

batting_first = ipl[ipl['win_by_runs'] != 0]
batting_first['winner'].value_counts()

plt.figure(figsize = (7,7))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()), list(batting_first['winner'].value_counts()[0:3]), color = ['b','y','orange'])
plt.show()

plt.figure(figsize = (7,7))
plt.pie(list(batting_first['winner'].value_counts()), labels = list(batting_first['winner'].value_counts().keys()), autopct = "%0.1f")
plt.show()

plt.figure(figsize = (7,7))
plt.pie(list(batting_first['winner'].value_counts()), labels = list(batting_first['winner'].value_counts().keys()), autopct = "%0.2f")
plt.show()