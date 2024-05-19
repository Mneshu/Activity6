import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("C:/Users/Sfundesihle/Desktop/test/dataset - 2020-09-24.csv")
print(data.head())

missing_values = data.isnull().sum()
print(missing_values)

duplicates = data.duplicated().sum()
print("Number of duplicate entries:", duplicates)


data['Wins'].hist()
plt.show()

data.columns
data.dtypes
data.size
data.shape


plt.figure(figsize=(10, 5))
plt.plot((data['Club'].head(5)),(data['Wins'].head(5)), marker='o', linestyle='-', color='red')
plt.title('Club Total Wins')
plt.xlabel('Clubs')
plt.ylabel('Wins per Club')
plt.grid(True)
plt.show()

plt.scatter((data['Club'].head(5)),(data['Wins'].head(5)))
plt.title('Scatter Plot of Hours Studied vs. TestScores')
plt.xlabel('Clubs')
plt.ylabel('Wins')
plt.show()


plt.hist((data['Wins'].head(7)), bins=20, color='blue', alpha=0.7)
plt.title('Histogram of Daily Wins Over One Year')
plt.xlabel('Wins (3 points)')
plt.ylabel('Form per Team')
plt.show()


plt.figure(figsize=(8, 5))
plt.bar((data['Club'].head(7)),(data['Clean sheets'].head(7)) , color='blue', alpha=0.7)
plt.title('Clean sheets by club')
plt.xlabel('Clubs')
plt.ylabel('Number of Clean sheets')
plt.show()

plt.figure(figsize=(7, 7))
plt.pie((data['Wins'].head(7)), labels=(data['Club'].head(7)), autopct='%1.1f%%', startangle=140)
plt.title('Teams Goals')
plt.show()

plt.figure(figsize=(6, 8))
plt.boxplot((data['Losses'].head(9)), vert=True, patch_artist=True, meanline=True, showmeans=True)
plt.title('Distribution of losses')
plt.ylabel('Losses')
plt.grid(True)
plt.show()