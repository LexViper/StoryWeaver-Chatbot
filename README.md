
# 🎉 Story Weaver: Interactive Storytelling Chatbot 🎭

Welcome to **Story Weaver**, a magical Flask-based chatbot that spins continuous, user-driven tales! Powered by a fine-tuned DistilGPT-2 model, it lets you craft stories with custom themes, characters, and moods, weaving narratives with 2-3 exciting choices per segment. Save your epic adventures with a click—perfect for creative minds! 🚀

---

## ✨ Project Spotlight

- **What’s This?**: An interactive chatbot that co-creates stories, adapting to your mood (happy, sad, excited, neutral) and building on your choices. From pirate quests to magical realms, the story’s yours to shape!
- **Tech Stack**: 🐍 Python | 🌐 Flask | 🤖 Hugging Face Transformers | 📊 Matplotlib
- **Goal**: Deliver a fun, evolving narrative experience with robust error handling and a save feature.

---





## 🚀 How to Execute

### Prerequisites
- Python 3.13+
- pip, Git
- macOS with MPS (optional for GPU)

### Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/story_weaver.git
   cd story_weaver
   ```
2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Verify model files in `models/fine_tuned_distilgpt2/` (run `notebooks/Day_4_Story_Weaver.ipynb` if missing).

### Running the App
1. Navigate to the web app:
   ```bash
   cd webapp
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Open your browser at `http://127.0.0.1:5000/`.
4. Enter a theme, character, and mood, then pick choices to build your story. Click “Save Full Story” to download it!

---

## 🎨 Project Structure
```
STORY_WEAVER/
├── data/                # Raw and processed text (e.g., Wizard of Oz)
├── notebooks/           # Jupyter notebooks for development
├── output/              # Saved story files
├── models/              # Fine-tuned DistilGPT-2 model
├── scripts/             # Utility scripts
├── story_plans/         # Narrative ideas
├── webapp/              # Flask app (app.py, templates, static)
├── README.md            # This file!
└── requirements.txt     # Dependencies
```

---




## 🌟 Results
- 🎭 Generates coherent, evolving stories with unique choices.
- 🔄 Ensures continuity by linking segments.
- 💾 Offers a “Save Full Story” download.
- 🛡️ Handles errors with `try-except` blocks.
- ✅ Fixed tech glitches (e.g., `max_length`, undefined paths).

---

## 🚧 Future Improvements
- 🌳 Add a “Show Full Story” button in the UI.
- 🌠 Implement branching narratives.
- ☁️ Deploy to Heroku for global access.
- 🎨 Enhance UI with animations or themes.

---

## 🤝 Contributing
Love stories? Help us grow!
1. Fork the repo.
2. Create a branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature-name"`.
4. Push: `git push origin feature-name`.
5. Open a PR!

---

## 📜 License
MIT License - Free to use, modify, and share! See [LICENSE](LICENSE) (create this file with MIT text if missing).

---
