import chess
import chess.pgn
from collections import defaultdict
import io

class ChessMistakeAnalyzer:
    """Analyzes chess games to find common mistakes and patterns."""
    
    def __init__(self, stockfish_path=None):
        """Initialize analyzer (Stockfish optional for MVP)."""
        self.stockfish_path = stockfish_path
        
    def analyze_game(self, pgn_string, player_name):
        """
        Analyze a single game (simplified version without engine).
        
        Args:
            pgn_string: PGN format game string
            player_name: Username to analyze
            
        Returns:
            dict with basic game info
        """
        game = chess.pgn.read_game(io.StringIO(pgn_string))
        if not game:
            return None
            
        # Basic game info
        white_player = game.headers.get("White", "")
        black_player = game.headers.get("Black", "")
        result = game.headers.get("Result", "*")
        
        if player_name.lower() == white_player.lower():
            player_color = "white"
        elif player_name.lower() == black_player.lower():
            player_color = "black"
        else:
            return None
        
        return {
            'color': player_color,
            'result': result,
            'opponent': black_player if player_color == 'white' else white_player
        }
    
    def analyze_multiple_games(self, pgn_data, player_name):
        """
        Analyze multiple games and return statistics.
        
        Args:
            pgn_data: String containing multiple PGN games
            player_name: Username to analyze
            
        Returns:
            dict with game statistics
        """
        games_analyzed = []
        wins = 0
        losses = 0
        draws = 0
        
        pgn_io = io.StringIO(pgn_data)
        
        while True:
            game = chess.pgn.read_game(pgn_io)
            if game is None:
                break
            
            game_info = self.analyze_game(str(game), player_name)
            
            if game_info:
                games_analyzed.append(game_info)
                
                result = game_info['result']
                color = game_info['color']
                
                # Determine win/loss/draw
                if result == "1-0":
                    if color == "white":
                        wins += 1
                    else:
                        losses += 1
                elif result == "0-1":
                    if color == "black":
                        wins += 1
                    else:
                        losses += 1
                elif result == "1/2-1/2":
                    draws += 1
        
        total_games = len(games_analyzed)
        
        # Generate mock insights for MVP
        insights = {
            'summary': {
                'total_games': total_games,
                'wins': wins,
                'losses': losses,
                'draws': draws,
                'win_rate': (wins / total_games * 100) if total_games > 0 else 0,
                'total_blunders': total_games * 2,  # Mock data
                'total_hung_pieces': int(total_games * 0.3),  # Mock data
                'blunders_per_game': 2.0  # Mock data
            },
            'top_mistakes': [
                {
                    'type': 'Blunders',
                    'count': total_games * 2,
                    'percentage': 200
                },
                {
                    'type': 'Hanging Pieces',
                    'count': int(total_games * 0.3),
                    'most_common': 'knight'
                },
                {
                    'type': 'Opening Mistakes',
                    'count': int(total_games * 0.5)
                }
            ],
            'recommendations': [
                'Practice slower, more careful play. Double-check moves before playing.',
                'You frequently hang knights. Before moving, ask: "Is this piece defended?"',
                'Study your openings more deeply. You make mistakes in the first 10 moves.'
            ]
        }
        
        return insights


if __name__ == "__main__":
    print("✅ ChessMistakeAnalyzer loaded successfully!")