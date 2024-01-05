import os
import openai  # Import the OpenAI API library

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
LEAD_ASSISTANT_ID = "asst_pkTOfztu8IdvPCssMbSz5NTh"

# The tool configuration with Lead Assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "compile_report",
        "description":
        "Compiles comprehensive reports on the status of tasks, outcomes, and insights/recommendations.",
        "parameters": {
            "type": "object",
            "properties": {
                "task_responses": {
                    "type":
                    "array",
                    "description":
                    "Collection of task responses and data from various assistants."
                }
            },
            "required": ["task_responses"]
        }
    },
    "assistant_id":
    LEAD_ASSISTANT_ID  # Set the Lead Assistant ID here in the tool configuration
}


# The callback function (Compiles report based on task responses)
def compile_report(arguments):
  """
    Compiles a comprehensive report based on the gathered task responses,
    leveraging the Lead Assistant's "compile_report" function.

    :param arguments: dict, Contains the task responses and data from various assistants.
                    Expected key: task_responses.
    :return: dict or str, Compiled report or error message.
    """
  # Extracting task responses from arguments
  task_responses = arguments.get('task_responses')

  # Validating the presence of task responses
  if not task_responses:
    return "Missing task responses. Please provide task_responses to compile the report."

  # Communicate with the Lead Assistant to compile the report
  openai.api_key = OPENAI_API_KEY
  response = openai.ChatCompletion.create(
      model="text-davinci-003",
      messages=[{
          "role":
          "system",
          "content":
          f"Delegate the following task to the Lead Assistant: Compile a comprehensive report based on the provided task responses."
      }, *[{
          "role": "user",
          "content": f"Task Response {i + 1}:\n{task_response}"
      } for i, task_response in enumerate(task_responses)], {
          "role":
          "assistant",
          "id":
          LEAD_ASSISTANT_ID,
          "content":
          "I'm ready to compile the report. Please provide the task responses."
      }])
  lead_assistant_response = response.choices[0].message.content.strip()

  # Extract the compiled report from the Lead Assistant's response
  # (Adjust the extraction logic based on the Lead Assistant's output format)
  compiled_report = {
      "status":
      "Completed",  # Assuming successful compilation
      "insights":
      lead_assistant_response.split("Insights:")[1].strip(),
      "recommendations":
      lead_assistant_response.split("Recommendations:")[1].strip()
  }

  return compiled_report


# Example usage of compile_report
# Replace 'task_responses' with actual task responses
task_responses = [
    "Task 1 response",
    "Task 2 response",
    "Task 3 response",
]

report = compile_report({"task_responses": task_responses})
print(report)  # Print the compiled report
