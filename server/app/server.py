from flask import Flask

app = Flask(__name__)

@app.route('/')
def square_root():
    n = 25  # Replace with the desired value of n
    return f"The square root of {n} is: {n**0.5}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)