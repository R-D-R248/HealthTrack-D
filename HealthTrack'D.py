from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
import tkinter as tk
import random
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

# Load and preprocess data
data = pd.read_csv('Diseases_Symptoms.csv')
data = data.to_numpy()

# Preprocess symptoms
symptoms_rawdata = data[:, 2]
symptoms = []

for symptoms_entry in symptoms_rawdata:
    symptoms.extend([s.strip().lower() for s in symptoms_entry.split(',')])

# Ensure symptoms are unique and sorted
symptoms = sorted(set(symptoms))
random_symptoms = np.array([
    symptoms[random.randint(0, 999)],
    symptoms[random.randint(0, 999)],
    symptoms[random.randint(0, 999)],
    symptoms[random.randint(0, 999)],
    symptoms[random.randint(0, 999)]
])
# Prepare symptom matrix for each disease
symptom_matrix = []
diagnosis = []

for i in range(len(data)):
    current_symptoms = data[i, 2].split(',')
    current_symptoms = [s.strip().lower() for s in current_symptoms]
    
    # Encode the current symptoms using the list of all possible symptoms
    current_symptom_encoded = np.zeros(len(symptoms))
    for s in current_symptoms:
        if s in symptoms:
            idx = symptoms.index(s)
            current_symptom_encoded[idx] = 1
    
    symptom_matrix.append(current_symptom_encoded)
    diagnosis.append(f"{data[i, 1]}: {data[i, 3]}")

symptom_matrix = np.array(symptom_matrix)

# Train the classifier
classifier = DecisionTreeClassifier(random_state=0)
classifier.fit(symptom_matrix, diagnosis)

classifier1 = DecisionTreeClassifier(random_state=1)
classifier1.fit(symptom_matrix, diagnosis)

classifier2 = DecisionTreeClassifier(random_state=2)
classifier2.fit(symptom_matrix, diagnosis)
# Tkinter User Interface setup
m = tk.Tk()
m.attributes("-fullscreen", True)

bg_image = Image.open("Bg-Image.png")  
bg_image = bg_image.resize((m.winfo_screenwidth(), m.winfo_screenheight()), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Set the background image using a Label widget
bg_label = tk.Label(m, image=bg_photo)
bg_label.place(relwidth=1, relheight=1) 

def quit_button():
    m.destroy()

Heading = tk.Label(m, text="HealthTrack'D", font=("Arial", 48))
Heading.pack()

rand_label = tk.Label(m, text = "Random Symptoms", font=("Arial", 14))
rand_label.pack(pady=5)
rand_text = tk.Label(m, text=random_symptoms)
rand_text.pack(pady=5)
# Create symptom input fields
symptom_label = tk.Label(m, text="Enter Symptom 1:", font=("Arial", 14))
symptom_label.pack(pady=5)
symptom_entry = tk.Entry(m, font=("Arial", 14))
symptom_entry.pack(pady=10)

symptom2_label = tk.Label(m, text="Enter Symptom 2:", font=("Arial", 14))
symptom2_label.pack(pady=5)
symptom2_entry = tk.Entry(m, font=("Arial", 14))
symptom2_entry.pack(pady=10)

predict_1 = tk.Label(m, text= 'Prediction 1')
predict_1.pack()
predict_2 = tk.Label(m, text= 'Prediction 2')
predict_2.pack()
predict_3 = tk.Label(m, text= 'Prediction 3')
predict_3.pack()



# Function to get user input and predict diagnosis
def user_input():
    symptom1 = "\'" + symptom_entry.get().lower().strip() + "\'"
    symptom2 = "\'" + symptom2_entry.get().lower().strip() + "\'"

    # Check if symptoms are valid
    if symptom1 in symptoms and symptom2 in symptoms:
        # Encode symptoms into the symptom matrix
        user_input_encoded = np.zeros(len(symptoms))
        user_input_encoded[symptoms.index(symptom1)] = 1
        user_input_encoded[symptoms.index(symptom2)] = 1

        # Predict the diagnosis
        prediction = classifier.predict([user_input_encoded])
        prediction1 = classifier1.predict([user_input_encoded])
        prediction2 = classifier2.predict([user_input_encoded])
        predict_1.config(text=prediction[0])
        predict_2.config(text=prediction1[0])
        predict_3.config(text=prediction2[0])
    else:
        messagebox.showerror("Symptom Error!", "One or both symptoms are not recognized.")

# Button to trigger prediction
predict_button = tk.Button(m, text="Predict Diagnosis", font=("Arial", 14), command=user_input)
predict_button.pack(pady=20)

button = tk.Button(m, text="Quit", font=("Arial", 14), command=quit_button)
button.pack()

m.mainloop()
quit
