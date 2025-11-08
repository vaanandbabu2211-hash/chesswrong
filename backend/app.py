from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer import ChessMistakeAnalyzer
import json

app = Flask(__name__)
CORS(app)

print("🚀 ChessWrong API v2.0 Starting...")
print("📍 Server running at: http://localhost:5000")
print("✅ JSON file support (Chess.com format)")
print("✅ Opening performance analysis")
print("✅ Rating-based performance tracking")
print("✅ Time pressure detection")
print("✅ Personalized recommendations")
print()

analyzer = ChessMistakeAnalyzer()

@app.route('/')
def home():
    return jsonify({
        "name": "ChessWrong API",
        "version": "2.0",
        "status": "running",
        "endpoints": {
            "/analyze": "POST - Analyze chess games from JSON file",
            "/health": "GET - Check API health"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": "2.0"})

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Get games data and username
        games_data = data.get('games')
        username = data.get('username', '')
        
        if not games_data:
            return jsonify({"error": "No games data provided"}), 400
        
        if not username:
            return jsonify({"error": "Username is required"}), 400
        
        # Parse JSON if it's a string
        if isinstance(games_data, str):
            try:
                games_data = json.loads(games_data)
            except json.JSONDecodeError:
                return jsonify({"error": "Invalid JSON format"}), 400
        
        # Load games
        game_count = analyzer.load_games_from_json(games_data, username)
        print(f"📊 Analyzing {game_count} games for {username}...")
        
        # Analyze
        results = analyzer.analyze_all_games()
        
        print(f"✅ Analysis complete!")
        print(f"   Win Rate: {results.get('win_rate', 0)}%")
        print(f"   Total Games: {results.get('total_games', 0)}")
        print()
        
        return jsonify(results)
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"error": f"Analysis failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)