from flask import g
from .IOStrategies import *
from flask import request

def getRestIO():
    if 'restIO' not in g:
        g.restIO = RESTInputOutput()
    return g.restIO

def getFlaskIO():
    if 'flaskIO' not in g:
        g.flaskIO = FlaskInputOutput()
    return g.flaskIO

def getWebIO():
    if '/api/' in request.path:
        return getRestIO()
    return getFlaskIO()

def getConsoleIO():
    if not getConsoleIO.console:
        getConsoleIO.console = ConsoleIO()
    return getConsoleIO.console

getConsoleIO.console = None
 
def getDictIO():
    if not getDictIO.dict:
        getDictIO.dict = DictIO()
    return getDictIO.dict

