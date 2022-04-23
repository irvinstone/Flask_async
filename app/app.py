import os
from flask import Flask, jsonify
import asyncio
import threading
import cx_Oracle

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

@app.route('/hola')
def connection():
    connection = cx_Oracle.connect(user="RESULTADOS_IN_2022", password="RESULTADOS_IN_2022",
                               dsn="192.168.50.21:1847/nacion19c")

    # Acquire a connection from the pool
    # connection = pool.acquire()

    # Use the pooled connection
    data = []
    cursor = connection.cursor()
    for result in cursor.execute(
        '''
        SELECT x.ESTADO name FROM ACTA_ESTADO_REG x
    WHERE CCODI_UBIGEO = '010101'
    '''
    ):
        print(result)
        data.append(result)


    # Release the connection to the pool
    # pool.release(connection)

    # Close the pool
    # pool.close()
    cursor.close()

    return jsonify({"connected":data})


if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=3000, debug=True)