from flask import Flask, render_template, request, jsonify
import subprocess
import sys
import os
import google.generativeai as genai
from error_knowledge_base import ERROR_DATABASE

app = Flask(__name__)

genai.configure(api_key="YOUR_GEMINI_KEY_HERE")
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_error(error_output, code):
    lines = error_output.strip().split("\n")
    last_line = lines[-1]
    error_type = last_line.split(":")[0] if ":" in last_line else last_line

    result = {
        "error_type": error_type,
        "location": "",
        "explanation": "",
        "suggestion": "",
        "ai_suggestion": ""
    }

    for line in lines:
        if "File" in line and "line" in line:
            result["location"] = line.strip()

    if error_type in ERROR_DATABASE:
        result["explanation"] = ERROR_DATABASE[error_type]["explanation"]
        result["suggestion"] = ERROR_DATABASE[error_type]["suggestion"]
    else:
        result["explanation"] = "Unknown error type."
        result["suggestion"] = "Check the full traceback for details."

    try:
        response = model.generate_content(
            f"Here is a Python code snippet that produced an error:\n\n"
            f"```python\n{code}\n```\n\n"
            f"Error:\n{error_output}\n\n"
            "Explain what caused this error in 2-3 sentences, "
            "then show the corrected code snippet."
        )
        result["ai_suggestion"] = response.text
    except Exception as e:
        result["ai_suggestion"] = f"AI unavailable: {str(e)}"

    return result


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/debug", methods=["POST"])
def debug():
    code = request.json.get("code", "")
    if not code.strip():
        return jsonify({"error": "No code provided"}), 400

    # Write code to temp file and run it
    tmp_path = "/tmp/debug_temp.py"
    with open(tmp_path, "w") as f:
        f.write(code)

    try:
        subprocess.run(
            [sys.executable, tmp_path],
            check=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        return jsonify({"success": True, "message": "No errors detected! Your code ran successfully."})

    except subprocess.CalledProcessError as e:
        result = analyze_error(e.stderr, code)
        return jsonify({"success": False, **result})

    except subprocess.TimeoutExpired:
        return jsonify({"success": False, "error_type": "TimeoutError",
                        "explanation": "Your code took too long to run.",
                        "suggestion": "Check for infinite loops.",
                        "ai_suggestion": "", "location": ""})


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))