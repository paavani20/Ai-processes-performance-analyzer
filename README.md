---

## AI-Powered Performance Analyzer for OS Processes  
This project is an AI-powered tool designed to monitor and analyze OS processes in real-time, detecting anomalies using machine learning.

### 📁 Installation and Setup  
Follow these steps to set up the project:

#### 1. Clone the Repository  
```bash
git clone [git_repo_link here]
cd AI_Powered-Performance-Analyzer
```

#### 2. Create a Virtual Environment  
Create a new virtual environment for the project (recommended).  
```bash
python3 -m venv env     # For Linux/Mac
python -m venv env       # For Windows
```

#### 3. Activate the Virtual Environment  
```bash
source env/bin/activate    # For Linux/Mac
.\env\Scripts\activate      # For Windows
```

#### 4. Install Required Packages  
Install all necessary packages using the `requirements.txt` file.  
```bash
pip install -r requirements.txt
```

#### 5. Train the Model  
Run the training script to create the anomaly detection model.  
```bash
python train_model.py
```

#### 6. Run the Web Interface  
Launch the Streamlit app to start monitoring processes.  
```bash
streamlit run visualization.py
```

#### 7. Access the Interface  
Open your browser and go to:  
```
http://localhost:8501
```

---

### 📌 Note  
- Ensure you have Python 3.x installed.  
- Install additional packages if prompted by any error messages.  
- Thank you.
