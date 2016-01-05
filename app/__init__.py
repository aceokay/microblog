from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Putting the import at the end avoids the circular import error.
from app import views
