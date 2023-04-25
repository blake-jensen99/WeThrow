from flask import Flask

app = Flask(__name__)

DB = 'wethrow_schema'

app.secret_key = "secret"