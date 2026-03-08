from flask import Flask, render_template, request, jsonify, send_from_directory
import face_recognition
import pickle
import os

app = Flask(__name__)

DATASET = "dataset"
CAPTURE = "static/capture.jpg"

# load dataset encodings
with open("data/encodings.pkl", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
image_paths = data["paths"]

# group encodings by image
dataset_faces = {}

for enc, path in zip(known_encodings, image_paths):

    if path not in dataset_faces:
        dataset_faces[path] = []

    dataset_faces[path].append(enc)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dataset/<filename>")
def dataset_files(filename):
    return send_from_directory(DATASET, filename)


@app.route("/search", methods=["POST"])
def search():

    file = request.files["image"]
    file.save(CAPTURE)

    image = face_recognition.load_image_file(CAPTURE)

    selfie_locations = face_recognition.face_locations(image)
    selfie_encodings = face_recognition.face_encodings(image, selfie_locations)

    if len(selfie_encodings) == 0:
        return jsonify({"photos": []})

    results = []

    # check each dataset image
    for img, faces in dataset_faces.items():

        match_all = True

        for selfie_face in selfie_encodings:

            matches = face_recognition.compare_faces(
                faces,
                selfie_face,
                tolerance=0.5
            )

            if True not in matches:
                match_all = False
                break

        if match_all:
            results.append(img)

    return jsonify({"photos": results})


if __name__ == "__main__":
    app.run(debug=True)