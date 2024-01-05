import os
import requests

# The tool configuration with assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "send_direct_message",
        "description": "Send a direct message to a user in a chat platform.",
        "parameters": {
            "type": "object",
            "properties": {
                "message_content": {
                    "type": "string",
                    "description": "Content of the message to be sent."
                },
                "recipient_role": {
                    "type": "string",
                    "description": "Role of the recipient user."
                }
            },
            "required": ["message_content", "recipient_role"]
        }
    },
    "assistant_id":
    "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Set the Lead Assistant ID here
}


# The callback function (Sends direct message to user in chat platform)
def send_direct_message(arguments):
  """
    Send a direct message to a user in a chat platform.

    :param arguments: dict, Contains the necessary information for sending a direct message.
    Expected keys: message_content, recipient_role.
    :return: dict or str, Response from the API or error message.
    """
  # Extracting information from arguments
  message_content = arguments.get('message_content')
  recipient_role = arguments.get('recipient_role')

  # Validating the presence of required information
  if not all([message_content, recipient_role]):
    return "Missing required information. Please provide message content and recipient role."

  # Simulate sending a direct message (Replace this with actual API call)
  # In this example, we'll just print the message to the console
  print(f"Sent a direct message to {recipient_role}: {message_content}")

  # Return a success message (Replace with actual API response handling)
  return "Direct message sent successfully."


# Example usage of send_direct_message
# Replace 'message_content' and 'recipient_role' with actual values
message_args = {
    'message_content': 'This is a test message.',
    'recipient_role': 'customer'  # Replace with the actual recipient role
}

# Send direct message
response = send_direct_message(message_args)
print(response)  # Print the response
