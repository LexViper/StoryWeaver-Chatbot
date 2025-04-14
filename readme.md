

# Story Weaver: Execution Flow README

This `README.md` outlines the step-by-step execution flow of the Story Weaver chatbot, based on `app.py` as of April 18, 2025. It’s designed for your personal use to understand, debug, and maintain the project.

## Project Overview
- **Purpose**: A Flask app that generates continuous stories with user choices using a fine-tuned DistilGPT-2 model.
- **Main Files**: `app.py`, `templates/index.html`, `templates/result.html`, `static/style.css`.
- **Goal**: Provide a clear execution path for personal reference.

## Execution Flow

### 1. Startup
- **File**: `app.py`
- **What Happens**:
  - Creates Flask app and sets a secret key for sessions.
  - Defines `project_root` and `model_path` to find `models/fine_tuned_distilgpt2/`.
  - Loads the model and tokenizer with a `try-except` block; sets `generator = None` if it fails (prints error to terminal).
- **Output**: Success message or error (e.g., "Error loading model: [details]").
- **Next**: Waits for requests on `/`.

### 2. Load Index Page
- **File**: `app.py` (`index()` GET)
- **What Happens**:
  - Renders `index.html` with a form for theme, character, and mood.
- **Output**: Form appears at `http://127.0.0.1:5000/`.
- **Next**: Waits for form submission (POST).

### 3. Start or Continue Story
- **File**: `app.py` (`index()` POST)
- **What Happens**:
  - **New Story**: If `theme` is in form, clears session, sets `theme`, `character`, `mood`, and initializes `story_segments`, `current_prompt`, `choices`.
  - **Continue**: If choice is submitted, updates `current_prompt` with the selected option.
  - Validates `mood` (must be "happy", "sad", "excited", "neutral") or returns an error.
  - Builds `new_prompt` with `theme`, `character`, last `story_segment` (capped at 200 chars), and tone based on `mood`.
  - Truncates `last_segment` to 100 chars if prompt exceeds 500 tokens.
  - Generates story with `max_new_tokens=300` if model is loaded.
  - Creates two unique choices with `max_new_tokens=60`, using the last story context.
  - Updates `session` with new story and choices.
  - Saves story to `output/` (e.g., `generated_story_segment_1_sad_2025-04-18.txt`).
  - Renders `result.html` with story and choices.
- **Output**: Story and options (e.g., "In a magical world... [1. Explore, 2. Ask]") on `result.html`.
- **Next**: Waits for next choice or save request.

### 4. Save Story
- **File**: `app.py` (`/save_story`)
- **What Happens**:
  - Checks if `story_segments` exists in `session`.
  - Builds a `.txt` file with theme, character, mood, and all segments.
  - Sends it as a download (e.g., `story_20250418_062000.txt`).
  - Returns error if no story or if save fails.
- **Output**: Downloaded file or error message.
- **Next**: Returns to `result.html`.

### 5. Error Handling
- **File**: `app.py` (all routes)
- **What Happens**:
  - Catches exceptions in `index()` and `/save_story` with `try-except`.
  - Returns a 500 error with details (e.g., "Error: An unexpected error occurred - [details]") or 404 if no story.
- **Output**: Error page in browser.
- **Next**: Requires fix or restart.

## File Roles
- **`index.html`**: Form for starting a story.
- **`result.html`**: Shows story and choices, links to `/save_story`.
- **`style.css`**: Styles the pages.
- **`models/fine_tuned_distilgpt2/`**: Provides the model data.

## Troubleshooting
- **Model Fails**: Ensure `models/fine_tuned_distilgpt2/` exists; rerun `Day_4_Story_Weaver.ipynb`.
- **No Display**: Check `templates/` files.
- **Save Issue**: Verify `output/` write permissions.
- **Token Problems**: Add `print(len(tokenizer.encode(new_prompt)))` to debug.

## How to Use
- **Save**: Put this in `STORY_WEAVER/README.md` (overwrite if empty).
- **Test**: Run `python app.py` in `webapp/`, follow the flow, and note issues.
- **Update**: Add steps as you modify code.

## Next Steps
- Add logging for each step.
- Document UI changes in `result.html`.

---

### How to Apply
1. **Save File**: Copy this into `STORY_WEAVER/README.md`.
2. **Run Test**: Start the app (`python app.py` in `webapp/`) and walk through the flow.
3. **Refine**: Update with your specific outputs or tweaks.
