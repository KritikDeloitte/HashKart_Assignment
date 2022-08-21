from flask import Flask

app = Flask(__name__)

# main driver function
if __name__ == '__main__':
    print('in run')
    app.run(debug=True,port=5000)

import gateway