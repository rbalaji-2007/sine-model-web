## Sine Model Web

A simple web application that demonstrates how to deploy a TensorFlow/Keras regression model using **Flask**.

The model predicts the value of **sin(x)** for a given angle (in radians) and compares the prediction with Python's actual `numpy.sin()` result.

> ⚠️ The model is trained only on values in the range **0 to 2π**.

---

## Features

- TensorFlow/Keras regression model
- Flask web application
- User input through a web form
- Displays:
  - Model prediction
  - Actual sine value
- Error handling for invalid inputs
- Lightweight and beginner-friendly project

---

## 📂 Project Structure

```
sine-model-web/
│
├── model/
│   └── sine_wave.keras        # Trained TensorFlow model
│
├── templates/
│   └── index.html             # Web page
|
├── screenshots/
│   └── image.png
│
├── app.py                     # Flask application
├── train_sine_model.py        # Script used to train the model
├── .env.example               # Example environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/rbalaji-2007/sine-model-web.git
cd sine-model-web
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root.

Example:

```env
MODEL_PATH=model/sine_wave.keras
```

---

## ▶️ Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 Model Information

- Framework: TensorFlow / Keras
- Task: Regression
- Input: Angle (radians)
- Output: Predicted `sin(x)`

The model was trained using values between:

```
0 ≤ x ≤ 2π
```

Predictions outside this range may be inaccurate because the model has never seen those values during training.

---

## 🛠️ Built With

- Python
- TensorFlow
- Keras
- Flask
- NumPy
- HTML
- CSS

---

## 📄 License

This project is open-source and available under the MIT License.
