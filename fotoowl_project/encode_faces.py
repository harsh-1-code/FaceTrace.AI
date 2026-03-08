import face_recognition
import os
import pickle

DATASET = "dataset"

encodings = []
image_paths = []

print("Encoding dataset...")

for file in os.listdir(DATASET):

    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):

        path = os.path.join(DATASET, file)

        image = face_recognition.load_image_file(path)
        faces = face_recognition.face_encodings(image)

        for face in faces:
            encodings.append(face)
            image_paths.append(file)

data = {
    "encodings": encodings,
    "paths": image_paths
}

with open("data/encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("Encoding complete")
print("Total faces:", len(encodings))