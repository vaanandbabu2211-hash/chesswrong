import json
from collections import defaultdict
import re

class ChessMistakeAnalyzer:
    def __init__(self):
        self.games = []
        self.username = ""
        
    def load_games_from_json(self, json_data, username):
        """Load games from Chess.com JSON format"""
        self.username = username.lower()
        self.games = []
        
        if isinstance(json_data, dict) and 'games' in json_data:
            self.games = json_data['games']
        elif isinstance(json_data, list):
            self.games = json_data
        else:
            raise ValueError("Invalid JSON format. Expected Chess.com games format.")
        
        return len(self.games)
    
    def extract_opening(self, pgn):
        """Extract opening name from PGN"""
        eco_match = re.search(r'\[ECO "([^"]+)"\]', pgn)
        eco_url_match = re.search(r'\[ECOUrl "([^"]+)"\]', pgn)
        
        if eco_url_match:
            url = eco_url_match.group(1)
            opening = url.split('/openings/')[-1].replace('-', ' ').title()
            return opening[:50]
        elif eco_match:
            return eco_match.group(1)
        return "Unknown Opening"
    
    def get_player_color(self, game):
        """Determine if user played white or black"""
        white_user = game.get('white', {}).get('username', '').lower()
        black_user = game.get('black', {}).get('username', '').lower()
        
        if white_user == self.username:
            return 'white'
        elif black_user == self.username:
            return 'black'
        return None
    
    def get_game_result(self, game, color):
        """Get result from user's perspective"""
        if color == 'white':
            result = game.get('white', {}).get('result', '')
        else:
            result = game.get('black', {}).get('result', '')
        
        if result == 'win':
            return 'win'
        elif result in ['checkmated', 'resigned', 'timeout', 'abandoned']:
            return 'loss'
        else:
            return 'draw'
    
    def analyze_all_games(self):
        """Analyze all games and return comprehensive statistics"""
        if not self.games:
            return {"error": "No games loaded"}
        
        stats = {
            'total_games': len(self.games),
            'wins': 0,
            'losses': 0,
            'draws': 0,
            'win_rate': 0,
            'white_games': 0,
            'black_games': 0,
            'white_wins': 0,
            'black_wins': 0,
            'time_controls': defaultdict(int),
            'openings': defaultdict(lambda: {'total': 0, 'wins': 0, 'losses': 0, 'draws': 0}),
            'mistakes': {
                'resignations': 0,
                'timeouts': 0,
                'checkmates': 0
            },
            'rating_history': [],
            'avg_rating': 0
        }
        
        ratings = []
        
        for game in self.games:
            color = self.get_player_color(game)
            if not color:
                continue
            
            if color == 'white':
                stats['white_games'] += 1
            else:
                stats['black_games'] += 1
            
            result = self.get_game_result(game, color)
            if result == 'win':
                stats['wins'] += 1
                if color == 'white':
                    stats['white_wins'] += 1
                else:
                    stats['black_wins'] += 1
            elif result == 'loss':
                stats['losses'] += 1
            else:
                stats['draws'] += 1
            
            tc = game.get('time_class', 'unknown')
            stats['time_controls'][tc] += 1
            
            pgn = game.get('pgn', '')
            opening = self.extract_opening(pgn)
            stats['openings'][opening]['total'] += 1
            if result == 'win':
                stats['openings'][opening]['wins'] += 1
            elif result == 'loss':
                stats['openings'][opening]['losses'] += 1
            else:
                stats['openings'][opening]['draws'] += 1
            
            if color == 'white':
                my_result = game.get('white', {}).get('result', '')
            else:
                my_result = game.get('black', {}).get('result', '')
            
            if my_result == 'resigned':
                stats['mistakes']['resignations'] += 1
            elif my_result == 'timeout':
                stats['mistakes']['timeouts'] += 1
            elif my_result == 'checkmated':
                stats['mistakes']['checkmates'] += 1
            
            if color == 'white':
                rating = game.get('white', {}).get('rating', 0)
            else:
                rating = game.get('black', {}).get('rating', 0)
            
            if rating:
                ratings.append(rating)
                stats['rating_history'].append({
                    'date': game.get('end_time', 0),
                    'rating': rating
                })
        
        if stats['wins'] + stats['losses'] > 0:
            stats['win_rate'] = round((stats['wins'] / (stats['wins'] + stats['losses'])) * 100, 1)
        
        if stats['white_games'] > 0:
            stats['white_win_rate'] = round((stats['white_wins'] / stats['white_games']) * 100, 1)
        else:
            stats['white_win_rate'] = 0
        
        if stats['black_games'] > 0:
            stats['black_win_rate'] = round((stats['black_wins'] / stats['black_games']) * 100, 1)
        else:
            stats['black_win_rate'] = 0
        
        if ratings:
            stats['avg_rating'] = round(sum(ratings) / len(ratings))
        
        opening_list = []
        for opening, data in stats['openings'].items():
            win_rate = 0
            if data['total'] > 0:
                win_rate = round((data['wins'] / data['total']) * 100, 1)
            opening_list.append({
                'name': opening,
                'games': data['total'],
                'wins': data['wins'],
                'losses': data['losses'],
                'draws': data['draws'],
                'win_rate': win_rate
            })
        
        opening_list.sort(key=lambda x: x['games'], reverse=True)
        stats['opening_performance'] = opening_list[:10]
        
        stats['time_controls'] = dict(stats['time_controls'])
        stats['recommendations'] = self.generate_recommendations(stats)
        
        return stats
    
    def generate_recommendations(self, stats):
        """Generate personalized recommendations"""
        recommendations = []
        
        total_losses = stats['losses']
        if total_losses > 0:
            timeout_rate = (stats['mistakes']['timeouts'] / total_losses) * 100
            if timeout_rate > 20:
                recommendations.append({
                    'category': 'Time Management',
                    'issue': f'{timeout_rate:.0f}% of your losses are from timeouts',
                    'suggestion': 'Play longer time controls or practice faster decision-making'
                })
        
        if abs(stats.get('white_win_rate', 0) - stats.get('black_win_rate', 0)) > 15:
            if stats.get('white_win_rate', 0) > stats.get('black_win_rate', 0):
                recommendations.append({
                    'category': 'Color Balance',
                    'issue': 'Significantly better with White pieces',
                    'suggestion': 'Study Black opening repertoire and defensive techniques'
                })
            else:
                recommendations.append({
                    'category': 'Color Balance',
                    'issue': 'Significantly better with Black pieces',
                    'suggestion': 'Review White opening principles and attacking patterns'
                })
        
        opening_perf = stats.get('opening_performance', [])
        if opening_perf:
            weak_openings = [op for op in opening_perf if op['games'] >= 3 and op['win_rate'] < 40]
            if weak_openings:
                worst = weak_openings[0]
                recommendations.append({
                    'category': 'Opening Repertoire',
                    'issue': f'Low win rate ({worst["win_rate"]}%) in {worst["name"]}',
                    'suggestion': f'Study this opening more or consider switching to alternatives'
                })
        
        if stats['mistakes']['resignations'] > stats['total_games'] * 0.3:
            recommendations.append({
                'category': 'Fighting Spirit',
                'issue': 'High resignation rate',
                'suggestion': 'Try to play out difficult positions - practice helps!'
            })
        
        if not recommendations:
            recommendations.append({
                'category': 'General',
                'issue': 'Keep up the good work!',
                'suggestion': 'Focus on consistency and learning from each game'
            })
        
        return recommendations