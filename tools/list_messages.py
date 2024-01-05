import os
import requests

# The tool configuration with assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "list_messages",
        "description": "Retrieves the messages from a specific thread.",
        "parameters": {
            "type": "object",
            "properties": {
                "thread_id": {
                    "type":
                    "string",
                    "description":
                    "The unique identifier of the thread from which messages will be listed."
                }
            },
            "required": ["thread_id"]
        }
    },
    "assistant_id":
    "asst_azHS6bnqbwP1kvbTtchEgU7A"  # Set the Assistant ID here
}


# The callback function (Retrieves messages from a specific thread)
def list_messages(arguments):
  """
    Retrieves the messages from a specific thread.

    :param arguments: dict, Contains the necessary information for listing messages from a thread.
                     Expected key: thread_id.
    :return: dict or str, Retrieved messages from the thread or error message.
    """
  # Extracting information from arguments
  thread_id = arguments.get('thread_id')

  # Validating the presence of required information
  if not thread_id:
    return "Missing required information. Please provide the thread ID."

  # Implement the logic to retrieve messages from the specified thread
  # Example:
  # messages = get_messages_from_thread(thread_id)

  # Placeholder response for demonstration purposes
  retrieved_messages = [{
      "sender": "User",
      "message": "Hello!"
  }, {
      "sender": "Assistant",
      "message": "Hi there! How can I assist you today?"
  }]

  return retrieved_messages
