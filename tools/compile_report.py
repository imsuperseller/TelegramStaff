import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def compile_report(task_responses):
    if not task_responses:
        return "Missing task responses. Please provide task_responses to compile the report."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Compile a comprehensive report based on the provided task responses."}] +
                     [{"role": "user", "content": task_response} for task_response in task_responses],
            max_tokens=1000
        )
        compiled_report = response.choices[0].message.content.strip()
        return {"status": "Completed", "report": compiled_report}
    except Exception as e:
        return f"An error occurred: {str(e)}"

task_responses = ["Task 1 response", "Task 2 response", "Task 3 response"]
report = compile_report(task_responses)
print(report)
