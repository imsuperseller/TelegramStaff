import os
import requests

# The tool configuration
tool_config = {
    "type": "function",
    "function": {
        "name": "debug_run",
        "description":
        "Retrieves detailed steps the assistant took during a run, providing insights into the code execution and decision-making process.",
        "parameters": {
            "type": "object",
            "properties": {
                "run_id": {
                    "type": "string",
                    "description": "The unique identifier of the run to debug."
                }
            },
            "required": ["run_id"]
        }
    }
}


# The callback function (Retrieves detailed steps during a run)
def debug_run(arguments):
  """
    Retrieves detailed steps the assistant took during a run, providing insights into the code execution and decision-making process.

    :param arguments: dict, Contains the necessary information for debugging a run.
                     Expected keys: run_id.
    :return: dict or str, Detailed steps taken during the run or error message.
    """
  # Extracting information from arguments
  run_id = arguments.get('run_id')

  # Validate the presence of the required run_id
  if not run_id:
    return "Missing required information. Please provide the run ID to debug."

  # Implement the logic to retrieve detailed steps of the specified run
  # Example:
  # detailed_steps = get_detailed_steps(run_id)

  # Placeholder response for demonstration purposes
  detailed_steps = {
      "step_1": "Assistant received user query.",
      "step_2": "Assistant processed the query.",
      "step_3": "Assistant generated a response.",
      "step_4": "Response sent to the user."
  }

  return detailed_steps
