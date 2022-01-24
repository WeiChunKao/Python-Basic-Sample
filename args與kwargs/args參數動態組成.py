from flask import Flask, jsonify
from flask import request
import json
from itertools import chain
app = Flask(__name__)
def DynamicComposition(**kwargs):
    mq_id=""
    for d in kwargs.values():
        L=len(d.values())
        i=0
        for s in d.values():
            if i==0:
                mq_id=s
                i+=1
            elif i<L:
                mq_id+="_"+s
                i+=1
    return mq_id       
@app.route('/test', methods=['POST'])
def test():
    if not request:
        abort(400)
    jsondata=request.json
    Identity=jsondata["Identity"]
    Details=jsondata["Details"]
    #print("Identity:",Identity)
    #print("Details:",Details)
    T=DynamicComposition(Identity=Identity)
    print(T)
    return jsonify({'Result': 'OK', 'Reason':' '}),200,{"Content-Type": "application/json"}
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', debug=False)
