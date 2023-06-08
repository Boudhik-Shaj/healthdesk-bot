from flask import Flask, render_template, request
import openai


API_KEY = 'Paste-your-API-key-here'
openai.api_key = API_KEY

app = Flask(__name__)

CONDITIONS = ['cold', 'fever', 'headache', 'stomachache']
SEVERITY = ['mild', 'moderate', 'severe']
# Homepage
@app.route('/')
def index():
    return render_template('chat.html', conditions=CONDITIONS, severity=SEVERITY)

# Chatbot endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    condition = request.form['condition']
    severity = request.form['severity']
    print(condition, severity)

    response = get_chatbot_response(condition, severity)
    
    return {'response': response}

# Function to interact with ChatGPT API
def get_chatbot_response(condition, severity):
    message = f"I have {severity} {condition}."

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you're a doctor and don't ask further questions"},
        {"role": "user", "content": message}
        ]
    )
    # print(completion.choices[0].message.content) # type: ignore
    chatbot_response = completion.choices[0].message.content # type: ignore
    return chatbot_response

if __name__ == '__main__':
    app.run(debug=True)
