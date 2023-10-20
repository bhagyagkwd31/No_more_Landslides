from flask import Flask, render_template, request
from ibm_watson_machine_learning import APIClient
from decouple import config
app = Flask(__name__)


# Load IBM Watson Machine Learning credentials from .env file
wml_api_key = config('WML_API_KEY')
wml_url = config('WML_URL')
wml_space_id = config('WML_SPACE_ID')
wml_deployment_id = config('WML_DEPLOYMENT_ID')

wml_credentials = {
    'apikey':wml_api_key,
    'url': wml_url
}

client = APIClient(wml_credentials)
client.set.default_space(wml_space_id)




@app.route('/')
def home():
    """
    Render the main landing page for user input.

    Returns:
        HTML template: The main landing page for users to enter prediction parameters.
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle the prediction process based on user input.

    Returns:
        HTML template: The result page displaying the prediction result.
    """
    try:
        # Retrieve user input from the form
        latitude = request.form['lat']
        longitude =request.form['lon']
        location = request.form['location']
        temp = int(request.form['temp']) if request.form['temp'].strip() else 0
        air = int(request.form['air']) if request.form['air'].strip() else 0
        humidity = int(request.form['humidity']) if request.form['humidity'].strip() else 0
        wind = int(request.form['wind']) if request.form['wind'].strip() else 0
        slope = int(request.form['slope']) if request.form['slope'].strip() else 0
        scoring_data = {
       client.deployments.ScoringMetaNames.INPUT_DATA: [
        {
             'fields': ['lat', 'lon','location','temp','air','humidity','wind','slope'],
             'values': [[float(latitude), float(longitude),location,temp,int(air),int(humidity),int(wind),int(slope)]] 
        }]
}
        # Make a prediction using the deployed model
        response = client.deployments.score(wml_deployment_id, scoring_data)

        # Extract the prediction result
        prediction = response['predictions'][0]['values'][0][0]
        probability_values= response['predictions'][0]['values'][0][1]
        print(probability_values)
        max_prob = max(probability_values)
        #calculate confidence
        confidence = round(max_prob*100,2)
        return render_template('predict_result.html', prediction=prediction, probability=confidence)
    except Exception as e:
        return f"An error occurred: {str(e)}"
if __name__ == '__main__':
    app.run(debug=True)
