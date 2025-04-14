# Day 4: Story Weaver Notebook Explanation

This document explains the `Day_4_Story_Weaver.ipynb` Jupyter Notebook, which fine-tunes the DistilGPT-2 model for the Story Weaver chatbot project on April 16, 2025.

## Notebook Overview
- **File Location**: `STORY_WEAVER/notebooks/Day_4_Story_Weaver.ipynb`
- **Purpose**: Fine-tune DistilGPT-2 with cleaned *Wizard of Oz* text for better story generation.
- **Structure**: Organized into cells with markdown explanations and Python code.

## Cell-by-Cell Breakdown
### Cell 1: Introduction
- **Content**: Markdown outlining Day 4 objectives (model fine-tuning).
- **Purpose**: Provides context.

### Cell 2: Setup
- **Content**: Installs `transformers`, loads data, and configures the model.
- **Purpose**: Prepares for training.

### Cell 3: Tokenization
- **Content**: Tokenizes the cleaned text with a block size of 128.
- **Purpose**: Preprocesses data for training.

### Cell 4: Fine-Tuning
- **Content**: Trains the model with 3 epochs and saves it to `models/fine_tuned_distilgpt2/`.
- **Output Example**:  
  - [Add your output here, e.g., "Training loss: 2.34, Model saved successfully."]

## Results
- Fine-tuned DistilGPT-2 with improved coherence on *Wizard of Oz* text.

## Next Steps
- Build the web interface in Day 5.