import openai
import os
import json

# Retrieve the OpenAI API key from Replit secrets
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Initialize the OpenAI API client
openai.api_key = OPENAI_API_KEY

# The tool configuration for delegate_task with the Lead Assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "delegate_task",
        "description":
        "Delegate a task to the Lead Assistant for decision support analysis.",
        "parameters": {
            "type": "object",
            "properties": {
                "report_id": {
                    "type": "string",
                    "description": "Identifier for the report to analyze."
                },
                "analysis_type": {
                    "type": "string",
                    "enum": ["trend", "issue", "opportunity"],
                    "description": "Type of analysis to perform on the report."
                }
            },
            "required": ["report_id", "analysis_type"]
        }
    },
    "assistant_id":
    "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Set the Lead Assistant ID here
}


# The callback function for delegate_task (Delegates task to the Lead Assistant)
def delegate_task(arguments):
  """
    Delegate the task of analyzing reports to the Lead Assistant for decision support analysis.

    :param arguments: dict, Contains the necessary information for analyzing reports.
                    Expected keys: report_id, analysis_type.
    :return: dict or str, Response from the Lead Assistant or error message.
    """
  # Extracting information from arguments
  report_id = arguments.get('report_id')
  analysis_type = arguments.get('analysis_type')

  # Validating the presence of required information
  if not all([report_id, analysis_type]):
    return "Missing required information. Please provide report ID and analysis type."

  # Delegate the task to the Lead Assistant
  response = {
      "task_details": {
          "action": "Analyze report",
          "target": "Lead Assistant",
          "report_id": report_id,
          "analysis_type": analysis_type
      },
      "assistant_id":
      "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Replace with the Lead Assistant's ID
  }

  return response  # Return the task delegation details


# Example usage of delegate_task
# Replace 'report_id' and 'analysis_type' with actual values
task_args = {
    'report_id': '12345',  # Replace with the actual report ID
    'analysis_type': 'trend'  # Replace with the actual analysis type
}

# Delegate the task to the Lead Assistant
response = delegate_task(task_args)
print(json.dumps(response, indent=2))  # Print the task delegation response
