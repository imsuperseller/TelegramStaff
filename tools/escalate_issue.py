import os
import openai

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
USER_CHAT_ID = "user_chat_id"  # Replace with the actual user chat ID

# The tool configuration with assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "escalate_issue",
        "description":
        "Identify and escalate issues to the user when necessary.",
        "parameters": {
            "type": "object",
            "properties": {
                "issue_details": {
                    "type": "string",
                    "description": "Detailed information about the issue."
                },
                "urgency_level": {
                    "type": "string",
                    "description": "The level of urgency of the issue."
                },
                "task_identifier": {
                    "type":
                    "string",
                    "description":
                    "Identifier of the affected task, if applicable."
                }
            },
            "required": ["issue_details", "urgency_level"]
        }
    },
    "assistant_id":
    "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Set the Lead Assistant ID here
}


# The callback function (Identifies and escalates issues)
def escalate_issue(arguments):
  """
    Identifies and escalates issues to the user using the OpenAI API.

    :param arguments: dict, Contains the issue details, urgency level, and optional task identifier.
                    Expected keys: issue_details, urgency_level, task_identifier.
    :return: str, Message indicating the escalation status.
    """

  # Extracting information from arguments
  issue_details = arguments.get('issue_details')
  urgency_level = arguments.get('urgency_level')
  task_identifier = arguments.get('task_identifier')

  # Validating the presence of required information
  if not all([issue_details, urgency_level]):
    return "Missing required information. Please provide detailed issue information and urgency level."

  # Using OpenAI API to craft a clear and concise escalation message
  openai.api_key = OPENAI_API_KEY
  response = openai.ChatCompletion.create(
      model="text-davinci-003",
      messages=[{
          "role":
          "system",
          "content":
          f"Craft a clear and concise escalation message for the following issue:\n{issue_details}\nUrgency level: {urgency_level}"
      }])
  escalation_message = response.choices[0].message.content.strip()

  # Sending the escalation message to the user (replace this with your actual method)
  send_direct_message(escalation_message,
                      USER_CHAT_ID)  # Replace with your message sending method

  # Optionally linking the issue to the affected task (if task_identifier is provided)
  if task_identifier:
    # Your code to link the issue to the affected task goes here
    pass

  return "Issue has been escalated successfully."


# Placeholder for sending a direct message to the user
def send_direct_message(message, chat_id):
  # Replace this with your actual method to send messages to the user
  print(f"Sending message to user (Chat ID: {chat_id}): {message}")


# Example usage of escalate_issue
# Replace 'issue_details' and 'urgency_level' with actual values
issue_args = {
    'issue_details': 'There is a critical bug in the system.',
    'urgency_level': 'High'  # Replace with the actual urgency level
}

# Escalate the issue to the user
response = escalate_issue(issue_args)
print(response)  # Print the escalation response
