from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from pathlib import Path

# Add parent directory to path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

# Now import from ml directory
from ml.main import recommend_songs
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        # Get song list from request
        user_data = request.json
        song_list = user_data.get('songs', [])

        # Validate song list
        if not song_list:
            return jsonify({'error': 'No songs provided'}), 400

        # Call the ML model's recommend_songs function
        recommendations = recommend_songs(song_list)

        # Return recommendations
        return jsonify({
            'status': 'success',
            'recommendations': recommendations
        })

    except Exception as e:
        print(f"Error in recommendation: {str(e)}")
        return jsonify({'error': 'Error processing recommendation'}), 500

if __name__ == '__main__':
    app.run(debug=True)