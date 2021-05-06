import os
from flask import Flask, jsonify
import asyncio
import threading

loop = asyncio.get_event_loop()
app = Flask(__name__)

#we define the route /
@app.route('/')
def welcome():
    # return a json
    result = loop.run_until_complete(hello())
    return jsonify({"result": result})

async def hello():
    return await asyncio.gather(
        sleep(5),
        sleep(4)
    )

async def sleep(seconds):
    await asyncio.sleep(seconds)
    print(f"Inside flask function: {threading.current_thread().name}")
    print(seconds)
    return 1

if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=3000, debug=True)