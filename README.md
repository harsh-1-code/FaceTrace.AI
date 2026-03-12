cd# FaceTrace.AI

### AI-Powered Event Photo Finder

FaceTrace.ai is an intelligent **face recognition-based photo retrieval system** that allows users to find their photos from large event photo collections using a **single selfie**.

The system detects faces in the uploaded selfie and searches the dataset to return all images where the same person or group of people appear.

---

## Features

* AI-powered **face recognition**
* **Single or multiple person search**
* Group matching logic
* Fast **pre-encoded dataset search**
* Modern **responsive UI**
* Camera-based selfie capture
* Photo **download functionality**
* Mobile friendly design

---

## How It Works

1. The system first **encodes all faces in the dataset** using the `face_recognition` library.
2. A user captures a **selfie through the web camera**.
3. The model detects faces in the selfie.
4. The system compares these faces with the **pre-encoded dataset faces**.
5. Matching images are returned in a **gallery view**.

Group logic:

* **1 face in selfie →** show all images where that person appears
* **2 faces in selfie →** show only images where both appear together
* **3+ faces →** show only group photos containing all detected people

---

## Tech Stack

**Frontend**

* HTML
* CSS
* JavaScript

**Backend**

* Python
* Flask

**AI / Computer Vision**

* face_recognition
* dlib
* OpenCV

---

## Project Structure

```
facetrace-ai
│
├── app.py
├── encode_faces.py
│
├── dataset
│   ├── photo1.jpg
│   ├── photo2.jpg
│
├── static
│   └── capture.jpg
│
├── templates
│   └── index.html
│
└── data
    └── encodings.pkl
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/facetrace-ai.git
cd facetrace-ai
```

Install dependencies

```bash
pip install flask face-recognition opencv-python numpy
```

---

## Encode Dataset

Run the encoding script once to generate face encodings.

```bash
python encode_faces.py
```

This creates:

```
data/encodings.pkl
```

---

## Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Usage

1. Click **Open Camera**
2. Capture a selfie
3. Click **Search Photos**
4. Matching photos will appear in the gallery
5. Download any image using the **Download button**

---

## Example Use Case

Imagine an event with hundreds of photos.

Instead of manually searching through all images, users can simply:

* Upload a selfie
* Instantly find every photo where they appear

---

## Future Improvements

* Real-time face detection
* ZIP download for all matched images
* Face bounding boxes
* Cloud deployment
* Database-based image indexing
* Advanced search filters

---

## License

This project is open-source and available under the **MIT License**.

---

## Author

Developed by ** Harsh Kumar & Ayush Kumar**

AI Project: **FaceTrace.ai – Intelligent Event Photo Finder**

