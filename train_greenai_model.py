import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Dummy dataset – replace this with your real one or enhance later
data = pd.DataFrame({
    'landfills': [2, 5, 1, 3, 4],
    'disposals': [3, 6, 2, 4, 5],
    'recyclings': [5, 2, 3, 4, 6],
    'baskets': [10, 25, 15, 20, 30],
    'wastewater': [1, 2, 1, 1, 3],
    'garbage_ratio': [0.34, 0.52, 0.28, 0.44, 0.60]
})

# Split features and target
X = data.drop(columns='garbage_ratio')
y = data['garbage_ratio']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
with open("greenai_garbage_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as greenai_garbage_model.pkl")
