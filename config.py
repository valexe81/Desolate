import os
basedir=os.path.abspath(os.path.dirname(__file__)) # saying -> os, get the path, of what is in ()
#gets the path from my computer to config.py



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' #says either "oi, computer, get secret number" or if it can't do that, it will be (the weird thing goose put)

#os = operating system
#path = route to find smth on computer










