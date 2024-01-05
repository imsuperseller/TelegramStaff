# The tool configuration
tool_config = {
    "type": "function",
    "function": {
        "name": "log_activity",
        "description":
        "Maintain a detailed log of development activities, changes, system updates, and other relevant events. Ensure a comprehensive record for future reference and analysis.",
        "parameters": {
            "type": "object",
            "properties": {
                "activity_details": {
                    "type":
                    "object",
                    "description":
                    "Object containing details about the activity to be logged, including the type of activity, time, and any relevant notes or outcomes. This field is required and should not use a default value."
                }
            },
            "required": ["activity_details"]
        }
    }
}


# The callback function (Function Call)
def log_activity(arguments):
  """
    Maintain a detailed log of development activities, changes, system updates, and other relevant events.
    Ensure a comprehensive record for future reference and analysis.

    :param arguments: dict, Contains activity details.
                     Expected keys: activity_details (dict).
    :return: str, Confirmation message of the logged activity.
    """
  # Extracting activity details from arguments
  activity_details = arguments.get('activity_details')

  # Validate the presence of required information
  if not activity_details:
    return "Missing required activity details. Please provide activity information."

  # Implement the logic to log the activity based on provided details
  # Example:
  # log_result = log_development_activity(activity_details)

  # Placeholder response for demonstration purposes
  log_result = "Activity has been successfully logged:\n"
  for key, value in activity_details.items():
    log_result += f"{key}: {value}\n"

  return log_result
