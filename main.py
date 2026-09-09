import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score  
df = pd.read_csv('ddataset.csv')
print(df.head())
print(df.describe())


#STEP 1 Data Cleaning
columns_to_fix = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

for col in columns_to_fix:
    median_value = df[col].replace(0, pd.NA).median()
    df[col] =df[col].replace(0, median_value)


# Count and display the number of zero value in each column
print("\n--- Zero values Count ---")
print((df==0).sum())

# STEP 2 Data Separation
#Seperate the featurs (x) from the target (y)
X = df.drop('Outcome', axis=1)
y =  df['Outcome']

#Quick check to see what X looks like 
print("Features of X")
print(X.head())

#Quick check to see what y looks like 
print("Features of y")
print(y.head())


#Split the data into 80% Training and 20% testing 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Verify the Split sizes
print("\n-- Data Split Size--")
print(f"Training Data Size: {X_train.shape[0]} patients")
print(f"Testing Data Size: {X_test.shape[0]} patients")

# #initialize the random forest model 
# model = RandomForestClassifier(random_state=42)

# initialize the tuned random forest model
model = RandomForestClassifier(n_estimators=200, max_depth=5, random_state=42)

# #Train the model using our training data
# model.fit(X_train, y_train)
# print("\n--- Model Training ---")
# print("Model has been successfully trained!")

# Train the tuned model
model.fit(X_train, y_train)

# Make predictions and grade the new model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print('\n--- Tuned Final Exam Results ---')
print(f"New Model Accuracy: {accuracy * 100:.2f}%")

# # 1. Ask the model to predict outcome fot the testing data
# y_pred = model.predict(X_test)

# # 2. Compare the model's Predictions (y_pred) to the actual answers (y_test)
# accuracy = accuracy_score(y_test, y_pred)

# print("\n--- Fianl Exam Results ---")
# print(f"Model Accuracy: {accuracy * 100:.2f}%")

print(y_pred)

#RANKING THE MEDICAL FEATURES FORM MOST TO LEAST IMPORTANT
#1. Extract the importance scores form our trained model
importances = model.feature_importances_

#2. Match those scores up with our colunm names (Glucose, BMI, etc.)
feature_importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
})

#3. Sort the list form most imortant to the least important
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

#4. Display the results
print("\n--- Feature Importance ---")
print(feature_importance_df)

# To save the trained model to your computer 
joblib.dump(model, 'diabetes_model.pkl')

print("\n--- Model Export ---")
print("Model saved successfully as 'diabetes_model.pkl'!")