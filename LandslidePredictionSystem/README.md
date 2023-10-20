# Landslide Prediction System

The Landslide Prediction System is a web application that predicts the likelihood of a landslide based on user-provided parameters such as Latitude, Longitude, Geographic location ,Temperature,Air quality, Humidity, Wind speed and Slope. This README provides detailed instructions for setting up and using the application.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation
1. Build & Train Model using Auto AI.
   Use XGB Classifier Algorithm.
   https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/welcome-main.html?context=wx&audience=wdp

2. **Install Python:**

   If Python is not already installed on your system, you can download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads/). 

3. **Clone the Repository:**

   Start by cloning the repository to your local machine using Git:

   ```bash
   git clone https://github.com/SurajGudaji/No_more_Landslides
   cd LandslidePredictionSystem

4. **Set Up Environment Variables:**
    Create a .env file in the project's root directory to manage environment variables. Here's a sample .env file:
    
    ```bash
    WML_API_KEY = <IBM Cloud API key>
    WML_URL = <Base URL for the Watson Machine Learning API endpoints>
    WML_SPACE_ID= <Deployment space ID>
    WML_DEPLOYMENT_ID =<Deployment ID>
    ```
   
5. **Install Dependencies:**
   Install the required Python packages listed in the requirements.txt file:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Application**

   Start the Flask application using the following command:
   ```
   python -m flask run
   ```
   This will start the application, and you can access it in your web browser at http://localhost:5000/.
2. Enter the required parameters
   including latitude, longitude etc


   **Snap:**-
   
   ![Alt text](/LandslidePredictionSystem/snapshots/landslide_prediction.png)


3. Click the "Predict" button to generate predictions based on the input parameters.

4. The result page will display the predicted severity and confidence level.
   
   **Snap:**-
   ![Alt text](/LandslidePredictionSystem/snapshots/output_predict.png)



    
   

