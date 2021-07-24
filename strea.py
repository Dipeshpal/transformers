import streamlit as st
from pyngrok import ngrok
import requests

url = "None"
if not hasattr(st, 'already_started_server'):
    # Hack the fact that Python modules (like st) only load once to
    # keep track of whether this file already ran.
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')

    from flask import Flask

    app = Flask(__name__)


    @app.route('/foo')
    def serve_foo():
        return 'This page is served via Flask!'


    endpoint = ngrok.connect(8888).public_url
    print(' * Tunnel URL:', endpoint)
    status = requests.get(
        f"https://jarvis-ai-api.herokuapp.com/update_api_endpoint/?username=dipeshpal&token=5d57286c59a3c6d8c30e1d6675c0a6&endpoint={endpoint}")
    print(status)
    app.run(port=8888)

# We'll never reach this part of the code the first time this file executes!
# Your normal Streamlit app goes here:
x = st.slider('Pick a number')
st.write('You picked:', x)
st.write('url', url)
