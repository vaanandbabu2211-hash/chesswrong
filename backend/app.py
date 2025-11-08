from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer import ChessMistakeAnalyzer
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to talk to backend

# Initialize analyzer
# For now, we'll simulate Stockfish (since installing it is complex)
analyzer = ChessMistakeAnalyzer(stockfish_path="stockfish")

@app.route('/api/analyze', methods=['POST'])
def analyze_games():
    """
    API endpoint to analyze chess games.
    Expects PGN data and player name.
    """
    try:
        data = request.get_json()
        pgn_data = data.get('pgn')
        player_name = data.get('player_name')
        
        if not pgn_data or not player_name:
            return jsonify({'error': 'Missing PGN data or player name'}), 400
        
        # For MVP, return mock data
        # TODO: Replace with actual analysis once Stockfish is installed
        mock_results = {
            'summary': {
                'total_games': 10,
                'total_blunders': 23,
                'total_hung_pieces': 8,
                'blunders_per_game': 2.3
            },
            'top_mistakes': [
                {
                    'type': 'Blunders',
                    'count': 23,
                    'percentage': 230
                },
                {
                    'type': 'Hanging Pieces',
                    'count': 8,
                    'most_common': 'knight'
                }
            ],
            'recommendations': [
                'Practice slower, more careful play. Double-check moves before playing.',
                'You frequently hang knights. Before moving, ask: Is this piece defended?'
            ]
        }
        
        return jsonify(mock_results), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check endpoint."""
    return jsonify({'status': 'healthy', 'message': 'ChessWrong API is running!'}), 200

if __name__ == '__main__':
    print("🚀 Starting ChessWrong API...")
    print("📍 Server running at: http://localhost:5000")
    app.run(debug=True, port=5000)