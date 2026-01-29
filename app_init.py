from flask import Flask, render_template, request, jsonify, redirect, send_file
import json
from time import time
from src.functions import *
from src.callgroq import *

cache_is_on = True # when True, it will cache Groq's flashcard list response and will use the locally saved flashcard list
file_is_already_list = False # when True, it will automatically get the file's elements as the flashcard list, skipping Groq call.

app = Flask(__name__)