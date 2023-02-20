from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    print('\n\nThe app is running...\n')
    return "hello world"

if __name__=='__main__':
    home()
    app.run(host='0.0.0.0', port=5000)