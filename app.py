from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    query = request.args.get('q')
    apikey = "ZCVPPAQIZYXS"
    lmt = 8
    
    # TODO: Extract the query term from url using request.args.get()
    # q = request.args.get("q")
    
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {
    "q": query,
    "key": apikey,  # test value
    "limit": lmt
    }

    # our test search
    # q = "excited"

    # get the top 8 GIFs for the search term
    r = requests.get(
       "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s", params)

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        return top_8gifs
    else:
        top_8gifs = None


    # continue a similar pattern until the user makes a selection or starts a new search.


        # TODO: Make an API call to Tenor using the 'requests' library. For 
        # reference on how to use Tenor, see: 
        # https://tenor.com/gifapi/documentation

        # TODO: Use the '.json()' function to get the JSON of the returned response
        # object

        # TODO: Using dictionary notation, get the 'results' field of the JSON,
        # which contains the GIFs as a list

        # TODO: Render the 'index.html' template, passing the list of gifs as a
        # named parameter called 'gifs'

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
