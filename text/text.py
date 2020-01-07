import speech_recognition as sr
import os
import os
import uuid
from flask import Blueprint, current_app, session, url_for, render_template
from flask_socketio import emit
from socketio_examples import socketio

bp = Blueprint('text', __name__, static_folder='static',
               template_folder='templates')


@bp.route('/')
def index():
    """Return the client application."""
    return render_template('audio/main.html')

def to_text(file_name):
    file_path = path.join(os.getcwd(), "long_test.wav")

    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)

    Sphinx local rec
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        
        
    #Google speech rec    
    #try:
    #    print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='en'))
    #except sr.UnknownValueError:
    #    print("Google Speech Recognition could not understand audio")
    #except sr.RequestError as e:
    #    print("Could not request results from Google Speech Recognition service; {0}".format(e))