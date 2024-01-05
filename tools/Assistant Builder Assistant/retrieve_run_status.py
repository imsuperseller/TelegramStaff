import os
import requests

# The tool configuration with assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "retrieve_run_status",
        "description":
        "Checks the current status of a run (queued, in progress, completed, etc.).",
        "parameters": {
            "type": "object",
            "properties": {
                "run_id": {
                    "type":
                    "string",
                    "description":
                    "The unique identifier of the run whose status is being checked."
                }
            },
            "required": ["run_id"]
        }
    },
    "assistant_id":
    "asst_azHS6bnqbwP1kvbTtchEgU7A"  # Set the Assistant ID here
}


# The callback function (Checks the current status of a run)
def retrieve_run_status(arguments):
  """
    Checks the current status of a run (queued, in progress, completed, etc.).

    :param arguments: dict, Contains the necessary information for checking the status of a run.
                     Expected key: run_id.
    :return: dict or str, Current status of the run or error message.
    """
  # Extracting information from arguments
  run_id = arguments.get('run_id')

  # Validating the presence of required information
  if not run_id:
    return "Missing required information. Please provide the run ID."

  # Implement the logic to retrieve the current status of the specified run
  # Example:
  # status = get_run_status(run_id)

  # Placeholder response for demonstration purposes
  run_status = {"run_id": run_id, "status": "In progress"}

  return run_status
