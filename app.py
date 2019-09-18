from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    
    # TODO: Extract the query term from url using request.args.get()
    query = request.args.get('query')
    apikey = "ZCVPPAQIZYXS"
    lmt = 10
    
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    
    params = {
    "q": query,
    "key": apikey,  # test value
    "limit": lmt
    }

    # get the GIFs for the search term
    # TODO: Make an API call to Tenor using the 'requests' library.
    r = requests.get(
       "https://api.tenor.com/v1/search", params)

    if r.status_code == 200:
        # TODO: Use the '.json()' function to get the JSON of the returned response
        # object & TODO: Using dictionary notation, get the 'results' field of the JSON,
        # which contains the GIFs as a list
        gifs = json.loads(r.content)['results']
    else:
        gifs = None


    # continue a similar pattern until the user makes a selection or starts a new search.


    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html", gifs=gifs)

if __name__ == '__main__':
    app.run(debug=True)
