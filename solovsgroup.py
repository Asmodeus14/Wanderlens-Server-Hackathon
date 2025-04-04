import cv2

face_cascade = cv2.CascadeClassifier("har_default.xml")

def classify_image(image_path):
    
    img = cv2.imread(image_path)
    if img is None:
        return None, "Unknown"

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return 'solo' if len(faces) == 1 else 'group'

def process_images(image_list):
    
    result_dict = {"solo": [], "group": []}

    for image_path in image_list:
        category = classify_image(image_path)
        if category != "Unknown":
            result_dict[category].append(image_path)

    return result_dict

