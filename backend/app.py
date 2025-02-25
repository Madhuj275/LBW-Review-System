from flask import Flask, request, jsonify, render_template
import os
from lbw_review import process_video

# Initialize Flask app and set template folder to "frontend"
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "frontend"))

# Configure upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Video upload route
@app.route('/upload', methods=['POST'])
def upload_video():
    # Check if a video file was uploaded
    if 'video' not in request.files:
        return jsonify({"error": "No video file uploaded"}), 400
    
    # Get the uploaded video file
    video = request.files['video']
    
    # Save the video to the uploads folder
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)
    
    # Process the video using the LBW review logic
    result = process_video(video_path)
    
    # Return the result as JSON
    return jsonify({"result": result})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
