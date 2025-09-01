# HealthTrack'D AI

HealthTrack'D is a Python-based AI application that predicts possible diseases based on symptoms entered by the user. The application uses **Decision Tree Classifiers** and a dataset of diseases and their symptoms. It features a **full-screen Tkinter GUI** with a background image and interactive inputs.

---

## Features

- Predicts possible diseases based on **two symptoms** entered by the user.
- Displays **three predictions** using different Decision Tree Classifiers for comparison.
- Shows **random symptoms** to help the user explore common symptoms.
- Full-screen GUI with background image.
- Easy to run in **IDLE** or directly as a Python script.

---

## Requirements

- Python 3.8+
- Required Python libraries:
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `tkinter` (comes with Python)
  - `Pillow` (for image handling)

Install missing libraries using pip:

pip install numpy pandas scikit-learn Pillow





## File Structure

HealthTrackD/
- ├── Diseases_Symptoms.csv
- ├── Bg-Image.png
- ├── HealthTrackD.py
- ├── License.md
- └── README.md



## Usage

1. Place `Diseases_Symptoms.csv` and `Bg-Image.png` in the same folder as `HealthTrackD.py`.  
2. Run the Python script:

python HealthTrackD.py

3. Enter **two symptoms** in the GUI input fields.  
4. Click **Predict Diagnosis** to see the predicted diseases.  
5. Click **Quit** to exit.

---

## Notes

- Ensure the CSV file and image file names exactly match the script references.  
- Symptoms must match the entries in the dataset; otherwise, an error will be shown.

---

## Author

- Roshan Deepu Roy
