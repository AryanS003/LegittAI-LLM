from flask import Flask
import requests

app = Flask(__name__)

@app.route('/query')
def query():
    return {"response": "Server is running!"}

# Incorrect: Client request in server script
url = 'http://127.0.0.1:5000/query'
params = {'query': 'Who is the most intelligent person?'}
response = requests.get(url, params=params)  # This runs before the server is ready
print(response.json())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)