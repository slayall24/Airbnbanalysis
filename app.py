import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score

# Load dataset
df = pd.read_csv('AB_NYC_2019.csv')

# Exploratory Data Analysis and Visualization
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 5))
sns.histplot(df["price"], bins=50, kde=True)
plt.xlim(0, 1000)
plt.title("Distribution of Listing Prices")
plt.show()

plt.figure(figsize=(8, 4))
sns.countplot(x="neighbourhood_group", data=df, hue="neighbourhood_group", palette="viridis", legend=False)
plt.title("Number of Listings by Neighbourhood Group")
plt.show()

relevant_columns = ['price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']
corr_matrix = df[relevant_columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap (Focused on Relevant Columns)")
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x='neighbourhood_group', y='price', data=df, palette='viridis')
plt.title("Price Distribution by Neighbourhood Group")
plt.xlabel("Neighbourhood Group")
plt.ylabel("Price")
plt.show()

# Encoding categorical variables
df_encoded = pd.get_dummies(df, columns=['neighbourhood_group', 'room_type'], drop_first=True)

# Separate features and target variable
X = df_encoded.drop(columns=['price'])
y = df_encoded['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Scaling successfully completed")

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Availability Classification
df["available"] = df["availability_365"].apply(lambda x: 1 if x > 0 else 0)
X = df[["latitude", "longitude", "price", "minimum_nights", "number_of_reviews"]]
y = df["available"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
precision = precision_score(y_test, y_pred)
print("Model Precision Score:", precision)
