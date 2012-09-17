#!/usr/bin/env python

import sys
import json
import os

from flask import Flask
from soco import SoCo

app = Flask(__name__)

sonos = SoCo(os.environ["SONOS_IP"])


@app.route("/play")
def play():
    return json.dumps(sonos.play())

@app.route("/pause")
def pause():
    return json.dumps(sonos.pause())

@app.route("/stop")
def stop():
    return json.dumps(sonos.stop())

@app.route("/mute")
def mute():
    return json.dumps(sonos.mute())

@app.route("/next")
def next():
    return json.dumps(sonos.next())

@app.route("/volume/up")
def volume_up():
    return json.dumps(sonos.volume( sonos.volume() + 5 ))

@app.route("/volume/down")
def volume_down():
    return json.dumps(sonos.volume( sonos.volume() - 5 ))

@app.route("/volume")
def volume():
    return json.dumps(sonos.volume())

@app.route("/volume/<int:volume>")
def volume(volume=False):
    if volume >= 0 and volume <= 100:
        return json.dumps(sonos.volume(volume))
    else:
        return json.dumps(False)

@app.route("/previous")
def previous():
    return json.dumps(sonos.previous())

@app.route("/current")
def current():
    return json.dumps(sonos.get_current_track_info())

if __name__ == "__main__":
    app.run()

