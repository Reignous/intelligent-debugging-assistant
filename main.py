import subprocess
import sys
import google.generativeai as genai
from error_knowledge_base import ERROR_DATABASE

genai.configure(api_key="AIzaSyDUMD5LnBlnW-4uxWLtWWLXTFy5Xm8QcLU")
model = genai.GenerativeModel("gemini-2.0-flash")

def run_user_code(file_path):
    try:
        subprocess.run(
            [sys.executable, file_path],
            check=True,
            capture_output=True,
            text=True
        )
        return "✅ No errors detected. Your code ran successfully!"
    except subprocess.CalledProcessError as e:
        return analyze_error(e.stderr, file_path)


def analyze_error(error_output, file_path):
    lines = error_output.strip().split("\n")
    last_line = lines[-1]

    error_type = last_line.split(":")[0] if ":" in last_line else last_line

    result = f"❌ Error Detected!\n\n🔎 Error Type: {error_type}\n"

    for line in lines:
        if "File" in line and "line" in line:
            result += f"\n📍 Location: {line.strip()}\n"

    if error_type in ERROR_DATABASE:
        result += "\n🧠 Explanation:\n"
        result += ERROR_DATABASE[error_type]["explanation"]
        result += "\n\n💡 Suggested Fix:\n"
        result += ERROR_DATABASE[error_type]["suggestion"]
    else:
        result += "\n⚠️ No predefined explanation available."

    # ✨ Claude AI suggestion
    result += "\n\n" + get_claude_suggestion(error_output, file_path)

    return result


def get_claude_suggestion(error_output, file_path):
    try:
        with open(file_path, "r") as f:
            code = f.read()

        response = model.generate_content(
            f"Here is a Python file that produced an error:\n\n"
            f"```python\n{code}\n```\n\n"
            f"Error:\n{error_output}\n\n"
            "Please explain what caused this error in 2-3 sentences, "
            "then show the corrected code snippet."
        )
        return f"🤖 AI Suggestion:\n{response.text}"
    except Exception as e:
        return f"🤖 AI Suggestion: (unavailable — {str(e)})"