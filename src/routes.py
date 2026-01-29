from app_init import *
from flask import request
from src.filetotext import file_to_text
import os

@app.route("/")
def homepage():
    return "<h1>Please use main.py to specify the location of your file.</h1>"

@app.route("/cards")
def main():
    path = request.args.get("path", None)

    if path is None:
        return "File doesnt exist"
    
    if file_is_already_list:
        sentences = ast.literal_eval(f.read())
    else:
        cached = None
        if cache_is_on:
            cached = "./static/caches/" + path.replace(":\\", "-").replace("\\", "-").replace(":/", "-").replace("://", "-").replace("//", "-").replace("/", "-") + ".txt"

        if cached is None or not os.path.exists(cached):
            msgs = file_to_text(path)
            sentences = callGroq(msgs)

            if cache_is_on:
                with open(cached, encoding="utf-8", mode="w") as f:
                    f.write(str(sentences))
        else:
            with open(cached, encoding="utf-8") as f:
                sentences = ast.literal_eval(f.read())

    return render_template("index.html", sentences=sentences[::-1], token=gen_token(), counter=len(sentences))

@app.route("/submit-texts", methods=["POST"])
def submit():
    raw_data = request.data
    json_str = raw_data.decode("utf-8")

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON"}), 400
    
    token = data["token"]

    words = [x["text"] for x in data["texts"]]
    filename = makeDocument(words, token)

    return jsonify({"redirect": f"/download/{filename}"})
    #return jsonify({"redirect": f"/status?token={token}"})

@app.route("/download/<filename>")
def download(filename):
    return render_template("download.html", filename=filename)