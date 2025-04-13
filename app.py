from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyBh0IsCNehhVFnkHZQPl5BF5yiUZm2Cgbc"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def get_ai_response(user_message):
    try:
        # Create a prompt that emphasizes supportive and de-escalating responses
        prompt = f"""You are a Crisis-to-Calm AI Responder. The user is experiencing distress. 
        Please provide a supportive, empathetic, and calming response. Focus on:
        1. Acknowledging their feelings
        2. Offering reassurance
        3. Suggesting calming techniques
        4. Providing helpful resources if appropriate
        
        User message: {user_message}
        
        Response:"""
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"I apologize, but I'm having trouble processing your message right now. Please try again later. If you're in immediate danger, please call emergency services."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    ai_response = get_ai_response(user_message)
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True, port=5001) 