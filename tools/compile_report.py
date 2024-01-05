import os
import openai

# Set your OpenAI API key from the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# The updated function using the new OpenAI API for chat completions
def compile_report(task_responses):
    """
    Compiles a comprehensive report based on the gathered task responses.

    :param task_responses: list, a collection of task responses and data from various assistants.
    :return: dict or str, Compiled report or error message.
    """
    if not task_responses:
        return "Missing task responses. Please provide task_responses to compile the report."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ensure you're using an appropriate model
            messages=[{"role": "system", "content": "Compile a comprehensive report based on the provided task responses."}] +
                     [{"role": "user", "content": f"{task_response}"} for task_response in task_responses],
            max_tokens=1000  # Adjust as needed
            # Add any additional parameters as necessary
        )

        # Extract and return the compiled report from the response
        compiled_report = response['choices'][0]['message']['content'].strip()
        return {"status": "Completed", "report": compiled_report}

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage of compile_report
task_responses = [
    "Task 1 response",
    "Task 2 response",
    "Task 3 response",
]

report = compile_report(task_responses)
print(report)  # Print the compiled report
