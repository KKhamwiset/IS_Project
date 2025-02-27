🧠 Neuron Activated
A sophisticated machine learning web application built with Streamlit that empowers users to upload data, train custom ML models, and generate accurate predictions with minimal effort.
✨ Features

📊 Smart Data Upload: Support for CSV and Excel files with automatic format detection
🔍 Interactive Data Exploration: Visualize your data with advanced filtering and statistical analysis
🧩 Feature Engineering: Automatically detect and transform features for optimal model performance
📈 Model Training: Train various ML models with customizable hyperparameters
🔮 Predictions: Generate predictions on new data with confidence scores
📱 Responsive Design: Seamless experience across desktop and mobile devices

🏗️ Project Structure
neuron_activated/
├── .devcontainer/              # Development container configuration
├── .github/workflows/          # CI/CD pipeline configurations
│   └── ci_test.yml             # Automated testing workflow
├── .streamlit/                 # Streamlit configuration files
├── assets/                     # Static assets
│   └── ml_prepare/             # ML preprocessing utilities
├── components/                 # Reusable UI components
│   ├── main_style.py           # Main styling configurations
│   └── sidebar.py              # Sidebar component
├── data/                       # Sample and user data storage
│   ├── income/                 # Income prediction dataset
│   │   ├── adult.data          # Training data
│   │   ├── adult.names         # Feature descriptions
│   │   ├── adult.test          # Test data
│   │   ├── index               # Data index
│   │   ├── old.adult.names     # Legacy feature descriptions
│   │   └── new_folder/         # Additional datasets
│   └── env_tensor/             # Environment tensor data
├── model_training/             # Model training scripts
├── pages/                      # Multi-page app views
├── app.py                      # Main Streamlit application
├── environment.yml             # Conda environment specification
├── README.md                   # Project documentation
└── requirements.txt            # Project dependencies
🚀 Installation
Clone this repository
git clone https://github.com/yourusername/neuron_activated
cd neuron_activated
Create and activate a virtual environment
python -m venv env
On Windows
env\Scripts\activate
On macOS/Linux
source env/bin/activate
Install the required packages
pip install -r requirements.txt
🎮 Usage
Run the Streamlit app
streamlit run app.py
Open your web browser and navigate to http://localhost:8501
Getting Started:

Upload your dataset (CSV or Excel)
Explore and visualize your data
Select target and feature columns
Train and evaluate multiple models
Generate and export predictions

🛠️ Dependencies
streamlit>=1.21.0
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.2.0
matplotlib>=3.5.0
tensorflow==2.15.0
tensorboard==2.15.2
tensorboard-data-server==0.7.2
tensorflow-estimator==2.15.0
tensorflow-io-gcs-filesystem==0.31.0
plotly>=5.10.0
opencv-python-headless>=4.5.0
🔄 CI/CD Pipeline
This project uses GitHub Actions for continuous integration and deployment. The pipeline automatically tests the application on each push to ensure functionality.
💡 Keep Your App Active
To prevent the app from going to sleep on hosting platforms, a keep-alive mechanism is included. You can use services like UptimeRobot (https://uptimerobot.com/) to ping your app regularly.
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
👥 Contributors

Your Name

🙏 Acknowledgments

Special thanks to all the open-source libraries that made this possible
Inspired by the need for accessible machine learning tools