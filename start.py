#!/usr/bin/env python

from collections import OrderedDict

from flask import Flask, request

app = Flask(__name__)

def fizzbuzz(start, end, triggers):
    message = ""
    for i in xrange(start, end+1):
        line = ""
        for k, v in triggers.iteritems():
            if i % k == 0:
                line += v
        if line == "": line = str(i)
        message += line + '\n'
    return message   

@app.route("/")
def respond():
    triggerdata = request.args.get("triggers", "3:Fizz,5:Buzz").split(',')
    triggers = OrderedDict((int(a), b) for a, b in [p.split(':') for p in triggerdata])
    return fizzbuzz(
            int(request.args.get("start", 1)),
            int(request.args.get("end", 100)),
            triggers
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
