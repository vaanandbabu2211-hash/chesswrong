# ♟️ ChessWrong - Advanced Chess Mistake Analyzer

**Stop repeating the same mistakes. Start improving faster.**

ChessWrong analyzes your Chess.com games to find patterns in your mistakes and gives you personalized recommendations to improve your game.

## 🎯 What Makes ChessWrong Different?

Unlike Chess.com's built-in analysis that reviews games one at a time, ChessWrong analyzes **all your games together** to find:

- 🔍 **Pattern Recognition** - "You hang pieces in 30% of your losses"
- 📊 **Opening Performance** - Which openings work best for YOU
- ⏰ **Time Management Issues** - Do you lose to time pressure?
- 🎨 **Color Balance** - Win rate differences between White and Black
- 📈 **Rating Performance** - How you perform against different skill levels
- 💡 **Personalized Tips** - Specific advice based on YOUR play style

## ✨ Features

### Advanced Analytics
- **Bulk Analysis**: Upload entire months of games at once
- **Pattern Detection**: Find your most common mistakes automatically
- **Opening Analysis**: See which openings work best for your rating
- **Time Pressure Detection**: Identify when you lose on time
- **Rating Performance**: Track how you perform against stronger/weaker players
- **Color Analysis**: Compare your White vs Black performance

### Beautiful Dashboard
- Clean, modern interface
- Interactive visualizations
- Color-coded insights (green = good, red = needs work)
- Priority-based recommendations

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Modern web browser (Chrome, Firefox, Edge)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vaanandbabu2211-hash/chesswrong.git
   cd chesswrong
   ```

2. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the backend**
   ```bash
   python app.py
   ```
   
   You should see:
   ```
   🚀 ChessWrong API v2.0 Starting...
   📍 Server running at: http://localhost:5000
   ```

4. **Open the frontend**
   - Open `frontend/index.html` in your browser
   - Or double-click the file in File Explorer

## 📖 How to Use

### Step 1: Get Your Chess.com Data
1. Go to [Chess.com](https://chess.com)
2. Navigate to your profile
3. Click on "Archive" or "Stats"
4. Download your games as JSON for any month
   - URL format: `https://api.chess.com/pub/player/YOUR_USERNAME/games/YYYY/MM`
   - Example: `https://api.chess.com/pub/player/varshetaa/games/2024/11`
5. Right-click → Save As → `username_games_monthyear.json`

### Step 2: Upload and Analyze
1. Open ChessWrong in your browser
2. Click the upload area or drag & drop your JSON file
3. Enter your Chess.com username
4. Click "Analyze My Games"
5. Wait a few seconds...
6. **Get insights!**

## 📊 What You'll Learn

### Example Insights

```
📊 Performance Summary
- 127 games analyzed
- 52% overall win rate
- Average rating: 847

❌ Common Mistake Patterns
1. Time Pressure Losses (18 times - 35% of losses)
   → You lose 65% of games with <2 min left
   
2. Struggles Against Stronger Players
   → 31% win rate vs 900+ rated opponents
   → 68% win rate vs <800 rated opponents

🎯 Opening Performance
✅ Italian Game: 15 games, 61% win rate
❌ Sicilian Defense: 23 games, 38% win rate
⚠️ French Defense: 8 games, 50% win rate

💡 Personalized Recommendations
HIGH PRIORITY:
- Consider playing Italian Game more often (61% WR vs Sicilian at 38%)
- Manage time better - you lose 35% of games to time pressure

MEDIUM PRIORITY:
- Your win rate with White (58%) is higher than Black (41%)
- Study more Black openings to balance your game
```

## 🛠️ Technical Stack

### Backend
- **Python 3.x** - Core language
- **Flask** - Web framework
- **python-chess** - Chess logic and PGN parsing
- **Flask-CORS** - Cross-origin requests

### Frontend
- **Pure HTML/CSS/JavaScript** - No frameworks needed
- **Modern CSS** - Gradients, animations, responsive design
- **Fetch API** - Communication with backend

## 📁 Project Structure

```
chesswrong/
├── backend/
│   ├── app.py              # Flask API server
│   ├── analyzer.py         # Core analysis logic
│   └── requirements.txt    # Python dependencies
├── frontend/
│   └── index.html          # Web interface
└── README.md               # This file
```

## 🎓 Learning Features

This project is perfect for learning:
- Python API development with Flask
- JSON data processing
- Chess data analysis
- Frontend-backend communication
- Git and GitHub workflow
- Data visualization

## 🔮 Future Features

Planned improvements:
- [ ] Stockfish integration for move-by-move analysis
- [ ] Opening repertoire builder
- [ ] Endgame performance analysis
- [ ] Compare with other players at your rating
- [ ] Export reports as PDF
- [ ] Track improvement over time
- [ ] Mobile app version
- [ ] Lichess support

## 🤝 Contributing

This is a learning project! Contributions welcome:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/cool-feature`)
3. Commit your changes (`git commit -m 'Add cool feature'`)
4. Push to the branch (`git push origin feature/cool-feature`)
5. Open a Pull Request

## 📝 License

MIT License - feel free to use this for learning!

## 🙋 Support

Having issues? 
1. Make sure backend is running (`python app.py`)
2. Check that your JSON file is from Chess.com
3. Verify your username is correct
4. Open an issue on GitHub with error details

## 🎯 Why "ChessWrong"?

Because we all make mistakes in chess. The key is learning from them and not repeating them. ChessWrong helps you identify YOUR specific patterns so you can improve faster.

---

**Made with ♟️ by chess players, for chess players**

*Stop wondering why you're stuck at your rating. Start understanding your game.*