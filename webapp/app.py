from flask import Flask, request, render_template, session, send_file
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os
from datetime import datetime
import io

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Define global paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
model_path = os.path.join(project_root, "models", "fine_tuned_distilgpt2")

# Load fine-tuned model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
    model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
except Exception as e:
    print(f"Error loading model: {e}")
    generator = None

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            if 'theme' in request.form:  # Initial story setup
                session.clear()
                session['theme'] = request.form['theme'].strip()[:50] or "a magical world"
                session['character'] = request.form['character'].strip()[:50] or "a brave adventurer"
                session['mood'] = request.form['mood'].lower()
                session['story_segments'] = []
                session['current_prompt'] = ""
                session['choices'] = []
            else:  # Continuation with choice
                choice_index = int(request.form['choice']) - 1
                if choice_index < len(session.get('choices', [])):
                    session['current_prompt'] = session['choices'][choice_index]

            mood = session.get('mood', 'neutral')
            if mood not in ["happy", "sad", "excited", "neutral"]:
                return "Invalid mood! Use happy, sad, excited, neutral."

            tone_adjustments = {
                "happy": "with a joyful and bright atmosphere",
                "sad": "with a somber and reflective mood",
                "excited": "with an adventurous and thrilling vibe",
                "neutral": "with a calm and steady pace"
            }
            theme = session.get('theme', 'a magical world')
            character = session.get('character', 'a brave adventurer')
            last_segment = session.get('story_segments', [])[-1] if session.get('story_segments') else ""
            last_segment = last_segment[-200:] if len(last_segment) > 200 else last_segment
            base_prompt = f"In {theme}, {character} continued their journey... {last_segment} {session.get('current_prompt', '')}"
            new_prompt = f"{base_prompt} The scene unfolded {tone_adjustments[mood]}, revealing..."

            prompt_tokens = len(tokenizer.encode(new_prompt))
            if prompt_tokens > 500:
                last_segment = last_segment[-100:]
                base_prompt = f"In {theme}, {character} continued their journey... {last_segment} {session.get('current_prompt', '')}"
                new_prompt = f"{base_prompt} The scene unfolded {tone_adjustments[mood]}, revealing..."

            if generator is not None:
                story_output = generator(new_prompt, max_new_tokens=300, num_return_sequences=1, 
                                        temperature=0.7, no_repeat_ngram_size=2, truncation=True)
                generated_text = " ".join(story_output[0]['generated_text'].split())
                
                # Improved choices prompt with context and diversity
                choices_context = f"{last_segment} {generated_text[-150:]} Based on this, suggest two distinct actions for {character} to continue the story, ensuring they are different and relevant."
                choices_output = generator(choices_context, max_new_tokens=60, num_return_sequences=2, 
                                         temperature=1.0, truncation=True)
                new_choices = [
                    output['generated_text'].split("Based on")[0].strip() for output in choices_output
                ]
                # Ensure choices are unique and valid
                new_choices = [c for i, c in enumerate(new_choices) if c and c not in new_choices[:i]]
                if len(new_choices) < 2:
                    new_choices = ["Explore a new path", "Talk to a nearby figure"]
            else:
                generated_text = "Error: Model failed to load."
                new_choices = ["Restart", "Try again"]

            session['story_segments'].append(generated_text)
            session['choices'] = new_choices
            session.modified = True

            # Save story
            current_scene = f"segment_{len(session['story_segments'])}"
            output_file = os.path.join(project_root, "output", 
                                     f"generated_story_{current_scene}_{mood}_{datetime.now().strftime('%Y-%m-%d')}.txt")
            os.makedirs(os.path.join(project_root, "output"), exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write("\n\n".join(session['story_segments']))

            return render_template('result.html', story=generated_text, choices=new_choices, 
                                 mood=mood, theme=theme, character=character)
        return render_template('index.html')
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}", 500

@app.route('/save_story')
def save_story():
    try:
        if 'story_segments' in session:
            full_story = "\n\n".join(session['story_segments'])
            output = io.StringIO()
            output.write(f"Story Weaver Adventure\nTheme: {session.get('theme', 'a magical world')}\n")
            output.write(f"Character: {session.get('character', 'a brave adventurer')}\n")
            output.write(f"Mood: {session.get('mood', 'neutral')}\n\n")
            output.write(full_story)
            output.seek(0)
            return send_file(
                io.BytesIO(output.getvalue().encode()),
                as_attachment=True,
                download_name=f"story_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mimetype='text/plain'
            )
        return "No story to save. Start a new story!", 404
    except Exception as e:
        return f"Error saving story: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)