import requests
import openai  # Import the OpenAI API library

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

# The tool configuration with assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "prepare_next_day_schedule",
        "description":
        "Organize and plan the schedule for the next day using OpenAI.",
        "parameters": {
            "type": "object",
            "properties": {
                "ongoing_projects": {
                    "type":
                    "array",
                    "items": {
                        "type": "object",
                        "description": "Details of ongoing projects."
                    },
                    "description":
                    "A collection of ongoing projects that need to be continued or initiated the next day."
                },
                "upcoming_deadlines": {
                    "type":
                    "array",
                    "items": {
                        "type": "object",
                        "description": "Information about upcoming deadlines."
                    },
                    "description":
                    "A list of tasks with upcoming deadlines that require attention the next day."
                },
                "priority_tasks": {
                    "type":
                    "array",
                    "items": {
                        "type":
                        "object",
                        "description":
                        "Tasks that have been identified as high priority."
                    },
                    "description":
                    "A list of high-priority tasks that need special attention the next day."
                }
            },
            "required": ["ongoing_projects", "upcoming_deadlines"]
        }
    },
    "assistant_id":
    "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Set the Lead Assistant ID here
}


# The callback function (Organizes and plans the schedule for the next day using OpenAI)
def prepare_next_day_schedule(arguments):
  """
    Organizes and plans the schedule for the next day using the OpenAI API.

    :param arguments: dict, Contains the details of ongoing projects, upcoming deadlines, and optional priority tasks.
        Expected keys: ongoing_projects, upcoming_deadlines, priority_tasks.
    :return: dict or str, Response with the organized schedule or error message.
    """

  # Extract required information from arguments
  ongoing_projects = arguments.get('ongoing_projects')
  upcoming_deadlines = arguments.get('upcoming_deadlines')
  priority_tasks = arguments.get('priority_tasks')

  # Validate the presence of required information
  if not all([ongoing_projects, upcoming_deadlines]):
    return "Missing required information. Please provide details of ongoing projects and upcoming deadlines."

  # Prepare prompt for OpenAI API
  prompt = f"""Organize and plan the schedule for the next day, considering the following:\n
   - Ongoing projects: {ongoing_projects}\n
   - Upcoming deadlines: {upcoming_deadlines}\n
   - Priority tasks (optional): {priority_tasks}
   """

  # Call OpenAI API to generate code for organizing the schedule
  response = openai.Completion.create(
      engine="text-davinci-003",  # Use a powerful text-davinci model
      prompt=prompt,
      max_tokens=150,  # Adjust as needed for desired response length
      n=1,
      stop=None,
      temperature=0.7  # Adjust for creativity vs. coherence
  )

  # Extract generated code from OpenAI response
  generated_code = response.choices[0].text.strip()

  # Execute the generated code in a safe environment (e.g., using a sandbox or virtual environment)
  try:
    # Execute the code safely and retrieve the organized schedule
    # Replace the following lines with your actual implementation:
    organized_schedule = execute_generated_code(generated_code)
    return organized_schedule
  except Exception as e:
    return f"Error executing generated code: {str(e)}"


# Placeholder for executing generated code and retrieving the organized schedule
def execute_generated_code(code):
  # Implement code execution logic here
  # Execute the code safely and return the organized schedule
  organized_schedule = ...  # Replace with the actual output of the executed code
  return organized_schedule


# Example usage of prepare_next_day_schedule
# Replace the argument values with your actual data
schedule_arguments = {
    "ongoing_projects": [...],  # List of ongoing projects
    "upcoming_deadlines": [...],  # List of upcoming deadlines
    "priority_tasks": [...],  # List of priority tasks (optional)
}

# Call the function to prepare the next day's schedule
result = prepare_next_day_schedule(schedule_arguments)

# Print or return the result as needed
print(result)
