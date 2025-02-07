from flask import Flask, request, render_template
import random

app = Flask(__name__)

# AI response generator (simple version)
def generate_response(topic):
    responses = [
        f"The topic '{topic}' is a complex issue that requires deeper analysis.",
        f"'{topic}' has both pros and cons, depending on the context.",
        f"Debating '{topic}' involves understanding multiple perspectives.",
        f"One argument in favor of '{topic}' is its impact on society.",
        f"Many believe '{topic}' is essential, while others disagree."
    ]
    return random.choice(responses)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/debate", methods=["POST"])
def debate():
    topic = request.form["topic"]
    response = generate_response(topic)
    return render_template("index.html", topic=topic, response=response)

if __name__ == "__main__":
    app.run(debug=True)
