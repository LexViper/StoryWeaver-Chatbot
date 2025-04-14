Hey brother, let’s wrap up your Story Weaver project with a comprehensive `README.md` that covers everything we’ve built from April 13-18, 2025! This document will reflect the full journey—starting with the *Wizard of Oz*-inspired chatbot, evolving into a general-purpose storyteller, and finally becoming a continuous, choice-driven narrative with robust features like error handling and story saving. Given your stellar Python skills (e.g., CSE3001 LAB on April 7, 2025, and Video Anomaly Detection), this README will showcase your hard work and provide clear instructions for setup, usage, and future enhancements. Here’s the complete `README.md` tailored to the current state of your project:

```markdown
# Story Weaver: Interactive Storytelling Chatbot

Welcome to **Story Weaver**, an interactive chatbot that crafts continuous, user-driven stories based on themes, characters, moods, and choices. Built with Python, Flask, and a fine-tuned DistilGPT-2 model from the Hugging Face `transformers` library, this project evolves narratives segment by segment, offering dynamic options to weave a unique tale. Originally inspired by *The Wizard of Oz*, it has transformed into a versatile storytelling tool with robust error handling and a save feature.

## Project Overview
- **Objective**: Create a chatbot for interactive, evolving stories tailored to user inputs, with continuous narrative progression and downloadable story files.
- **Development Period**: April 13-18, 2025
- **Tools**: Python 3.13, Jupyter Notebook, Flask, `transformers`, `textblob`, `torch`
- **Status**: Completed MVP with continuous storytelling, error handling, and save functionality

## Features
- Generates ongoing stories with user-defined themes, characters, and moods.
- Adapts tone based on mood (happy, sad, excited, neutral).
- Offers 2-3 distinct, contextually relevant choices after each segment.
- Ensures narrative continuity by building on previous segments.
- Includes a Flask web app for seamless interaction.
- Provides a “Save Full Story” feature to download the complete narrative.
- Implements error handling for model loading, generation, and saving.

## Table of Contents
- [Setup](#setup)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Development Process](#development-process)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Setup
### Prerequisites
- Python 3.13 or later
- pip (Python package manager)
- Git (for version control)
- macOS with MPS support (optional for GPU acceleration)

### Hardware Requirements
- Minimum: 8GB RAM, 10GB free disk space
- Recommended: 16GB RAM, GPU for faster model generation

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/story_weaver.git
   cd story_weaver
   ```

2. **Install Dependencies**
   - Set up a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Verify Model Files**
   - Ensure `models/fine_tuned_distilgpt2/` contains the fine-tuned model files (e.g., `pytorch_model.bin`, `config.json`). If missing, run `notebooks/Day_4_Story_Weaver.ipynb` to regenerate.

## Usage
### Running the Jupyter Notebooks
1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Execute the notebooks in order:
   - `Day_1_Story_Weaver.ipynb`: Clean the raw *Wizard of Oz* text.
   - `Day_2_Story_Weaver.ipynb`: Implement the initial choice system.
   - `Day_3_Story_Weaver.ipynb`: Add sentiment analysis for mood adjustment.
   - `Day_4_Story_Weaver.ipynb`: Fine-tune the DistilGPT-2 model.
   - Adjust parameters (e.g., `block_size`, `num_train_epochs`) as needed.

### Running the Web App
1. Navigate to the web app directory:
   ```bash
   cd webapp
   ```
2. Start the Flask server:
   ```bash
   python app.py
   ```
3. Open a browser and go to `http://127.0.0.1:5000/`.
4. Input a theme, character, and mood to start a story.
5. Choose options to continue the narrative, and click “Save Full Story” to download the complete tale.

### Example Interaction
- **Input**: Theme: “pirate adventure,” Character: “Captain Jack,” Mood: “excited”
- **Output 1**: “In a pirate adventure, Captain Jack continued their journey... revealing a hidden cove with a glittering chest... [1. Open the chest, 2. Scout the cove]”
- **Choice**: 1
- **Output 2**: “Jack opened the chest, finding a map... [1. Follow the map, 2. Return to the ship]”
- **Save**: Click “Save Full Story” to download `story_20250418_062000.txt` with the full narrative.

## File Structure
```
STORY_WEAVER/
├── data/
│   ├── processed/
│   │   └── wizard_of_oz_cleaned.txt  # Cleaned text for training
│   └── raw/
│       └── wizard_of_oz_raw.txt      # Original text
├── notebooks/
│   ├── Day_1_Story_Weaver.ipynb      # Text cleaning
│   ├── Day_2_Story_Weaver.ipynb      # Choice system
│   ├── Day_3_Story_Weaver.ipynb      # Sentiment analysis
│   ├── Day_4_Story_Weaver.ipynb      # Model fine-tuning
│   └── Day_5_Explanation.md          # Web app explanation
├── output/                           # Saved story files
├── models/
│   └── fine_tuned_distilgpt2/        # Fine-tuned DistilGPT-2 model
├── scripts/
│   ├── a.py                          # Utility script
│   └── create.py                     # Creation script
├── story_plans/
│   └── story_plan.txt                # Narrative plan
├── webapp/
│   ├── app.py                        # Flask web app with error handling
│   ├── templates/
│   │   ├── index.html                # Input form
│   │   └── result.html               # Story display with choices
│   └── static/
│       └── style.css                 # Basic styling
├── README.md                         # This file
└── requirements.txt                  # Dependencies
```

## Development Process
### Day 1: Text Cleaning
- Loaded and cleaned `wizard_of_oz_raw.txt` to create `wizard_of_oz_cleaned.txt` using Python and Jupyter Notebook.

### Day 2: Choice System
- Added a choice-based narrative system (e.g., temple vs. river bed) in `Day_2_Story_Weaver.ipynb`.

### Day 3: Sentiment Analysis
- Integrated TextBlob to adjust story tone based on user mood in `Day_3_Story_Weaver.ipynb`.

### Day 4: Model Fine-Tuning
- Fine-tuned DistilGPT-2 with `wizard_of_oz_cleaned.txt` using `transformers`, addressing token length and coherence.

### Day 5: Web Interface
- Built a Flask web app, initially for Oz-themed stories, then generalized it.
- Fixed model loading, blank page issues, and added continuous storytelling.

### Conversion and Enhancements
- Generalized to any theme and character, enabling continuous narratives with dynamic choices.
- Resolved `max_length` errors using `max_new_tokens`.
- Fixed Jinja2 `enumerate` error with `loop.index`.
- Added “Save Full Story” feature and robust error handling.
- Addressed undefined `model_path` and `project_root` by defining globally.

## Results
- Successfully generates evolving, coherent stories with 2-3 distinct choices per segment.
- Ensures narrative continuity by anchoring choices to the latest segment.
- Eliminates duplicate choices with improved prompts and deduplication.
- Provides a downloadable “Save Full Story” feature for the complete narrative.
- Handles errors gracefully with `try-except` blocks for model loading, generation, and saving.
- Fixed undefined `model_path` and `project_root` by defining them globally.
- Resolved technical issues like `max_length` warnings and Jinja2 template errors.

## Future Improvements
- Enhance choice generation with structured prompts or a predefined action library.
- Add branching logic for complex narrative paths.
- Implement a “Show Full Story” button to display all segments in the UI.
- Optimize model performance with quantization or a larger dataset.
- Deploy to a cloud platform (e.g., Heroku) for public access.
- Add user sessions to save progress across devices.

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature-name"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (create a `LICENSE` file if not present).

## Acknowledgments
- Inspired by *The Wizard of Oz* by L. Frank Baum and interactive storytelling concepts.
- Built with support from xAI’s Grok 3 and the Hugging Face `transformers` community.

