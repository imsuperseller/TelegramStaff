import os
import requests

# The tool configuration with Assistants Builder Assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "add_message_to_thread",
        "description":
        "Appends a new message to an existing conversation thread.",
        "parameters": {
            "type": "object",
            "properties": {
                "thread_id": {
                    "type":
                    "string",
                    "description":
                    "The unique identifier of the thread to which the message will be added."
                },
                "message_content": {
                    "type":
                    "string",
                    "description":
                    "The content of the message being added to the thread."
                },
                "role": {
                    "type":
                    "string",
                    "description":
                    "The role of the message sender, typically 'user' or 'assistant'."
                }
            },
            "required": ["thread_id", "message_content", "role"]
        },
        "assistant_id":
        "asst_azHS6bnqbwP1kvbTtchEgU7A"  # Include the Assistants Builder Assistant ID here
    }
}


# The callback function (Appends a new message to an existing conversation thread)
def add_message_to_thread(arguments):
  """
    Appends a new message to an existing conversation thread.

    :param arguments: dict, Contains the necessary information for adding a message to a thread.
                     Expected keys: thread_id, message_content, role.
    :return: dict or str, Response with the added message or error message.
    """
  # Extracting information from arguments
  thread_id = arguments.get('thread_id')
  message_content = arguments.get('message_content')
  role = arguments.get('role')

  # Validating the presence of required information
  if not all([thread_id, message_content, role]):
    return "Missing required information. Please provide the thread ID, message content, and role."

  # Implement the logic to append the message to the specified thread
  # Example:
  # response = append_message_to_thread(thread_id, message_content, role)

  # Placeholder response for demonstration purposes
  added_message = {
      "thread_id": thread_id,
      "message_content": message_content,
      "role": role
  }

  return added_message
