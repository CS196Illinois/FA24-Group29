from flask import Flask, request, jsonify
from flask_cors import CORS
from recommendation import recommend_songs  # Ensure this function works properly

app = Flask(__name__)
CORS(app)
# Root route for testing server
@app.route('/')
def home():
    return "Flask API is running!"

# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    # Check if request body contains JSON
    print(f"Received request data: {request.json}")
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400

    user_data = request.json
    song_list = user_data.get('songs', [])

    # Check if songs were provided in the request
    if not song_list:
        return jsonify({'error': 'No songs provided'}), 400

    # Debugging output to check what is received
    print(f"Received song list: {song_list}")

    # Pass the list of song inputs to the recommendation function
    try:
        recommendations = recommend_songs(song_list)
    except Exception as e:
        print(f"Error in recommend_songs: {e}")
        return jsonify({'error': 'Error processing recommendation'}), 500

    return jsonify({
        'status': 'success',
        'recommendations': recommendations
    })

if __name__ == '__main__':
    app.run(debug=True)