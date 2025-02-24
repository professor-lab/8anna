from flask import Flask, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt


app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
    