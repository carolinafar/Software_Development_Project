# Software_Development_Project

This project is a data analysis and visualization tool for car sales advertisements, built using Python and Streamlit. It explores factors like car age, mileage, and condition to understand pricing trends from car listings. The app is hosted on Render, providing users with an interactive experience to explore car sales data in the U.S.

Dividing the app into the distribution of odometer, price, and model year it's a simple way for the car dealership or anybody with the dataset to filter each variable by car model. With the markdown being car models it would be a helpful tool to find what would better suit the customer. 

The project directory includes the following files and folders:

	•	app.py: Main Streamlit application file, containing the code for the web app interface.
	•	notebooks/EDA.ipynb: Jupyter notebook with in-depth exploratory data analysis.
	•	notebooks/vehicles_us.csv: Dataset of car listings (U.S.).
	•	requirements.txt: List of Python dependencies.
	•	.streamlit/config.toml: Streamlit configuration file.

Libraries Used
    
    • Jupyter Notebook (EDA.ipynb):
        pandas, seaborn, matplotlib.pyplot, and plotly.express
    • app.py (Streamlit app):
        pandas, streamlit, plotly.express

Setup & Installation

	1.	Clone the Repository:

        git clone <repo-url>
        cd <repo-folder>

	2.	Install Dependencies:

        It’s recommended to use a virtual environment:

        python -m venv venv
        source venv/bin/activate  # On Windows use venv\Scripts\activate
        pip install -r requirements.txt

	3.	Run the Application:
        
        Start the Streamlit app locally:

        streamlit run app.py

This is the URL of the app on Render:

https://software-development-project-uhtx.onrender.com 