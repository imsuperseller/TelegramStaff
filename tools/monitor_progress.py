import os
import requests

OPENAI_API_KEY = os.environ.get(
    'OPENAI_API_KEY'
)  # Ensure you have set the OPENAI_API_KEY environment variable

# The tool configuration
tool_config = {
    "type": "function",
    "function": {
        "name": "monitor_progress",
        "description":
        "Regularly monitor the progress of delegated tasks. Keep track of the status of ongoing projects and initiatives, providing timely updates.",
        "parameters": {
            "type": "object",
            "properties": {
                "assistant_id": {
                    "type": "string",
                    "description":
                    "The ID of the assistant whose task progress is being monitored.",
                    "default":
                    "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Set default assistant ID to Lead Assistant
                },
                "task_id": {
                    "type":
                    "string",
                    "description":
                    "The unique identifier of the task being monitored."
                }
            },
            "required":
            ["task_id"
             ]  # Only task_id is required, as assistant_id has a default value
        }
    }
}


# The callback function (Monitors task progress using OpenAI API)
def monitor_progress(arguments):
  """
    Monitor the progress of a delegated task using the OpenAI API.

    :param arguments: dict, Contains the necessary information for monitoring task progress.
                    Expected keys: assistant_id (optional), task_id.
    :return: dict or str, Response from the API or error message.
    """
  # Extracting information from arguments
  assistant_id = arguments.get(
      'assistant_id'
  ) or "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Use default assistant ID if not provided
  task_id = arguments.get('task_id')

  # Validating the presence of required information
  if not task_id:
    return "Missing required information. Please provide the task ID."

  # Making the API request to monitor task progress using OpenAI API
  response = requests.get(
      f"https://api.openai.com/v1/tasks/{task_id}",
      headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
      params={"assistant_id": assistant_id})

  if response.status_code == 200:
    return response.json()  # Return the full task details
  else:
    return f"Failed to monitor task progress: {response.text}"
