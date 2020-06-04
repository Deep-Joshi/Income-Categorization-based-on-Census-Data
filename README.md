# Income-Prediction
This repository contains the entire code in Python used to develop an end-to-end machine learning model that classifies census data into income categories. The model is deployed on Heroku cloud using Flask web framework.

Link -> https://income--prediction.herokuapp.com/

The raw and processed dataset can be found under 'data' folder.
'model' directory contains serialized models built using various machine learning algorithms like Logistic Regression, Decision Trees, Random Forest, KNN and XGBoost.
The 'notebooks' directory has the python code used to build machine learning pipeline.
The 'static' folder contains all the static files (images, css,etc) used for developing a web application.
'templates' directory consist all HTML files used for web application creation. 

'Census Data Analysis.twbx' -> Tableau Packaged Workbook (.TWBX) file that contains all the worksheets and dashboards that were used to communicate the insights found during the analysis of processed dataset. 

'requirements.txt' -> Contains all the dependencies required to be installed in order to run this application.

Steps to run the application locally:
Open Command Prompt -> Change the path to a location that contains all these files -> Type 'python Main.py' -> Hit the url on the browser.
