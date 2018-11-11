from flask import Flask,request
from caesar import rotate_string
app = Flask(__name__)

form = """
    <!doctype html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
        </head>
        <body>
            <form action="/encrypt" method="post">
            <label for="rotate">ROTATE BY</label>
                <input type="text" name="rotate"><br>
                <textarea name="message">{0}</textarea>
                <input type="submit">
            </form>
        </body>
    </head> 
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/encrypt",methods=['POST'])
def encrypt():
    rotate=int(request.form['rotate'])
    message=request.form['message']
    encrypted_mess=rotate_string(message,rotate)
    return  form.format(encrypted_mess)

if __name__=="__main__":
    app.run(debug=True)