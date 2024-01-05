# The tool configuration
tool_config = {
    "type": "function",
    "function": {
        "name": "monitor_system",
        "description":
        "Regularly check the health and performance of systems and applications. Monitor key metrics and generate alerts for any anomalies or performance issues detected.",
        "parameters": {
            "type": "object",
            "properties": {
                "system_details": {
                    "type":
                    "object",
                    "description":
                    "Object containing details about the system to be monitored, including metrics to watch, thresholds for alerts, and any specific monitoring instructions. This field is required and should not use a default value."
                }
            },
            "required": ["system_details"]
        }
    }
}


# The callback function (Function Call)
def monitor_system(arguments):
  """
    Regularly check the health and performance of systems and applications.
    Monitor key metrics and generate alerts for any anomalies or performance issues detected.

    :param arguments: dict, Contains system details.
                     Expected keys: system_details (dict).
    :return: str, Alert or status message of the monitoring process.
    """
  # Extracting system details from arguments
  system_details = arguments.get('system_details')

  # Validate the presence of required information
  if not system_details:
    return "Missing required system details. Please provide monitoring information."

  # Implement the logic to monitor the system based on provided details
  # Example:
  # monitoring_status = monitor_system_health(system_details)

  # Placeholder response for demonstration purposes
  monitoring_status = "System monitoring has been initiated successfully. Monitoring details:\n"
  for key, value in system_details.items():
    monitoring_status += f"{key}: {value}\n"

  return monitoring_status
