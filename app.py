from flask import Flask, render_template, request 

import requests 

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST']) 

def index(): 

    movies = [] 
 

    if request.method == 'POST': 

        search_query = request.form['search_query'] 

        api_key = "" 

        url = f"http://www.omdbapi.com/?s={search_query}&apikey={fa7ea1c2}" 

        response = requests.get(url) 

        data = response.json() 

        print(data) #look in the terminal at the data 

 
 

    return render_template('index.html', movies=movies) 

 
 

if __name__ == "__main__": 

    app.run(debug=True) 