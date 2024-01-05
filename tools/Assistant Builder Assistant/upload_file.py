import os
import requests

# The tool configuration with assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "upload_file",
        "description": "Uploads a new file to be used by the assistant.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_content": {
                    "type": "string",
                    "description": "The content of the file being uploaded."
                },
                "purpose": {
                    "type":
                    "string",
                    "description":
                    "The purpose of the file, such as 'assistants' or 'answers'."
                }
            },
            "required": ["file_content", "purpose"]
        }
    },
    "assistant_id":
    "asst_azHS6bnqbwP1kvbTtchEgU7A"  # Set the Assistant ID here
}


# The callback function (Uploads a new file)
def upload_file(arguments):
  """
    Uploads a new file to be used by the assistant.

    :param arguments: dict, Contains the necessary information for uploading a file.
                     Expected keys: file_content, purpose.
    :return: dict or str, Response from the API or error message.
    """
  # Extracting information from arguments
  file_content = arguments.get('file_content')
  purpose = arguments.get('purpose')

  # Validating the presence of required information
  if not all([file_content, purpose]):
    return "Missing required information. Please provide file content and purpose."

  # Implement the logic to upload the file for the specified purpose
  # Example:
  # response = upload_file_to_assistant(file_content, purpose)

  # Placeholder response for demonstration purposes
  uploaded_file_info = {"file_name": "sample_file.txt", "file_size": "1024 KB"}

  return uploaded_file_info
