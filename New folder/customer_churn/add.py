from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
print("Running in DEMO MODE - No pickle needed")
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received:", data)

        creditScore = int(float(data.get('creditScore', 650)))
        age = int(float(data.get('age', 35)))
        balance = float(data.get('balance', 0))
        isActive = int(float(data.get('activeMember', 1)))

        # Simple logic for demo - viva ku pothum
        score = 0
        if creditScore < 600: score += 2
        if age > 45: score += 2
        if balance < 50000: score += 1
        if isActive == 0: score += 2

        is_churn = 1 if score >= 3 else 0

        result_text = "Customer is likely to Churn 😟 (High Risk)" if is_churn == 1 else "Customer is likely to STAY 😊 (Low Risk)"

        return jsonify({'result': result_text, 'prediction': is_churn})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)