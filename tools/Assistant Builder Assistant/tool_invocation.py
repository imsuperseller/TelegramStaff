import os
import requests

# The tool configuration with assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "tool_invocation",
        "description":
        "Directly invokes tools like Code Interpreter or Knowledge Retrieval with specified input.",
        "parameters": {
            "type": "object",
            "properties": {
                "tool_type": {
                    "type":
                    "string",
                    "description":
                    "Specifies the type of tool to be invoked, such as 'code_interpreter' or 'retrieval'."
                },
                "input_data": {
                    "type": "string",
                    "description": "The input data or query for the tool."
                },
                "assistant_id": {
                    "type":
                    "string",
                    "description":
                    "The unique identifier of the assistant that will use the tool."
                }
            },
            "required": ["tool_type", "input_data", "assistant_id"]
        }
    },
    "assistant_id":
    "asst_azHS6bnqbwP1kvbTtchEgU7A"  # Set the Assistant ID here
}


# The callback function (Directly invokes tools)
def tool_invocation(arguments):
  """
    Directly invokes tools like Code Interpreter or Knowledge Retrieval with specified input.

    :param arguments: dict, Contains the necessary information for tool invocation.
                     Expected keys: tool_type, input_data, assistant_id.
    :return: dict or str, Response from the tool or error message.
    """
  # Extracting information from arguments
  tool_type = arguments.get('tool_type')
  input_data = arguments.get('input_data')
  assistant_id = arguments.get('assistant_id')

  # Validating the presence of required information
  if not all([tool_type, input_data, assistant_id]):
    return "Missing required information. Please provide tool type, input data, and assistant ID."

  # Implement the logic to invoke the specified tool with the provided input data and assistant ID
  # Example:
  # response = invoke_tool(tool_type, input_data, assistant_id)

  # Placeholder response for demonstration purposes
  tool_response = f"Tool '{tool_type}' invoked with input data: '{input_data}' by Assistant ID: '{assistant_id}'"

  return tool_response
