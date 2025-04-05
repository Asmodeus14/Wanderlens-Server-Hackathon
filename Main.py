from flask import Flask, request, jsonify
from mongo.db import insert_document, get_documents  # your existing imports
import datetime
import os
import json
from dotenv import load_dotenv
from flask_cors import CORS
from google import genai
import logging
from GenAI import gen
from solovsgroup import process_images
import tempfile
import numpy as np
import pandas as pd
import cv2 as cv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return "Welcome to the Flask MongoDB App!"

@app.route("/create_trip", methods=["GET", "POST"])
def documents():
    if request.method == "POST":
        data = request.get_json()
        inserted_id = insert_document(data)
        response = jsonify({"inserted_id": str(inserted_id)})
        return app.make_response((response, 201))
    
    elif request.method == "GET":
        docs = get_documents(limit=10)  # Limit query size
        if not isinstance(docs, (list, dict)):
            docs = {"error": "Unexpected docs format", "docs": str(docs)}
        return jsonify(docs)

API_KEY = os.getenv("GEMINI_KEY")  # Your Gemini API key from the environment
MODEL = "gemini-2.0-flash"

@app.route("/ai", methods=["POST"])
def ai_suggestions():
    try:
        logging.info("AI suggestion request received")
        suggestions = gen()
        return jsonify({"suggestions": suggestions})
    except Exception as e:
        logging.error(f"Error calling Gemini API: {str(e)}", exc_info=True)
        return jsonify({"error": "Failed to generate suggestions", "details": str(e)}), 500

@app.route("/process", methods=["POST"])
def process_images_endpoint():
    if "images" not in request.files:
        return jsonify({"message": "No images provided."}), 400

    token = request.form.get("token", "no")
    upload_time = request.form.get("uploadTime", datetime.datetime.now().isoformat())

    files = request.files.getlist("images")

    try:
        with tempfile.TemporaryDirectory() as tmpdirname:
            file_paths = []
            for file in files:
                if file:
                    filename = file.filename
                    filepath = os.path.join(tmpdirname, filename)
                    file.save(filepath)  # Save directly to disk
                    file_paths.append(filepath)

            result_dict = process_images(file_paths)
    except Exception as e:
        logging.error(f"Error processing images: {str(e)}", exc_info=True)
        return jsonify({"message": "Error processing images", "error": str(e)}), 500

    return jsonify({
        "message": "Processing successful",
        "token": token,
        "uploadTime": upload_time,
        "result": result_dict
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
