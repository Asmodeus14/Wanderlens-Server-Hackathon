import cv2 as cv
import face_recognition
import numpy as np
import os

# Load Haar cascade for face detection
haar_cascade_path = cv.data.haarcascades + "har_default.xml"
haar_cascade = cv.CascadeClassifier(haar_cascade_path)


if haar_cascade.empty():
    raise ValueError("Error loading Haar cascade file. Check the file path!")

known_face_encodings = []
known_face_names = []
person_counter = 1  

def load_known_faces(img_list):
    
    global person_counter
    for img_path in img_list:
        image = cv.imread(img_path)
        if image is None:
            print(f"Warning: Unable to load image: {img_path}")
            continue

        rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_image)

        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(f"person{person_counter}")
            person_counter += 1

def recognize_faces_in_image(image):
    
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces_detected = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    recognized_names = []
    
    for (x, y, w, h) in faces_detected:
        face_image = image[y:y+h, x:x+w]
        rgb_face = cv.cvtColor(face_image, cv.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_face)

        if encodings:
            face_encoding = encodings[0]
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                match_index = matches.index(True)
                name = known_face_names[match_index]
            else:
                global person_counter
                name = f"person{person_counter}"
                known_face_encodings.append(face_encoding)
                known_face_names.append(name)
                person_counter += 1

            recognized_names.append(name)
    
    return recognized_names

def process_images(image_paths):
    
    results = {"solo": {}, "group": {}}

    for img_path in image_paths:
        image = cv.imread(img_path)
        if image is None:
            print(f"Warning: Unable to load image: {img_path}")
            continue

        recognized_names = recognize_faces_in_image(image)
        num_faces = len(recognized_names)

        if num_faces == 0:
            continue  
        elif num_faces == 1:
            name = recognized_names[0]
            results["solo"].setdefault(name, []).append(img_path)
        else:
            for name in recognized_names:
                results["group"].setdefault(name, []).append(img_path)

    return results


if __name__ == "__main__":
    # List of images
    image_list = ["testing/a.jpg", "testing/b.jpg", "testing/e.jpg", "testing/f.jpg", "testing/ff.jpeg"]

    
    load_known_faces(image_list)

    
    categorized_results = process_images(image_list)

    
    print(categorized_results)
