# Day 2: Story Weaver Notebook Explanation

This document explains the `Day_2_Story_Weaver.ipynb` Jupyter Notebook, which implements an interactive choice system for the Story Weaver chatbot project on April 14, 2025.

## Notebook Overview
- **File Location**: `STORY_WEAVER/notebooks/Day_2_Story_Weaver.ipynb`
- **Purpose**: Add a user choice system, generate story branches with DistilGPT-2, and store the story state.
- **Structure**: Organized into cells with markdown explanations and Python code.

## Cell-by-Cell Breakdown
### Cell 1: Introduction
- **Content**: Markdown outlining Day 2 objectives (choice system, story generation).
- **Purpose**: Provides context.

### Cell 2: Setup
- **Content**: Loads the cleaned file and DistilGPT-2 model.
- **Purpose**: Reuses Day 1 environment.

### Cell 3: Initialize Story State
- **Content**: Defines `story_state` and `choices` dictionary, fixes `get_user_choice()` scope.
- **Purpose**: Sets up interactive framework.

### Cell 4: Get User Choice
- **Content**: Prompts user for input (1 or 2) and validates it.
- **Purpose**: Enables interactivity.

### Cell 5: Generate Story
- **Content**: Creates a prompt based on choice and generates a 200-character story.
- **Output Example**: