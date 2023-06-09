from flask import Flask, render_template, request 

import requests 

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST']) 

def index(): 

    movies = [] 
 

    if request.method == 'POST': 

        #gets search query text from input box on webpage 
        search_query = request.form['search_query'] 

        api_key = "fa7ea1c2" 
        #url that goes to ombd and uses parameters to search database
        url = f"http://www.omdbapi.com/?s={search_query}&apikey={api_key}" 

        #makes request to url

        response = requests.get(url) 

        data = response.json() 

        print(data) #look in the terminal at the data 

        #If the response is true from the JSON then send the movies to the webpage... 

        if data.get('Response') == 'True': 

            movies = data["Search"] # this gets the array of movies using the key Search 

            return render_template('index.html', movies=movies) 

        else: 

            print("Bad Response!")

 
 

    return render_template('index.html', movies=movies) 

 
 

if __name__ == "__main__": 

    app.run(debug=True) 