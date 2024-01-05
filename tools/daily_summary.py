import requests

# The tool configuration with the Lead Assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "generate_daily_summary",
        "description":
        "Generate a daily report by delegating to the Lead Assistant.",
        "parameters": {
            "type": "object",
            "properties": {
                "task_summary": {
                    "type":
                    "array",
                    "items": {
                        "type": "object",
                        "description": "Individual summaries of each task."
                    },
                    "description":
                    "A collection of summaries for all tasks undertaken during the day. Required."
                },
                "achievement_highlights": {
                    "type":
                    "array",
                    "items": {
                        "type":
                        "string",
                        "description":
                        "Notable achievements or milestones reached during the day."
                    },
                    "description":
                    "A list of highlights and key achievements from the day's work. Optional."
                },
                "pending_tasks": {
                    "type":
                    "array",
                    "items": {
                        "type":
                        "object",
                        "description":
                        "Details of tasks that are ongoing or have not yet been started."
                    },
                    "description":
                    "A list of tasks that are pending or require further action. Optional."
                }
            },
            "required": ["task_summary"]
        }
    },
    "assistant_id":
    "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Set the Lead Assistant ID here
}


# The callback function (Delegates to Lead Assistant for daily summary)
def generate_daily_summary(arguments):
  """
    Delegates to the Lead Assistant to generate a daily summary report.

    :param arguments: dict, Contains the information for the daily summary.
    Expected keys: task_summary, achievement_highlights, pending_tasks.
    :return: dict, Response from the Lead Assistant containing the daily summary.
    """

  # Extract required information from arguments
  task_summary = arguments.get('task_summary')

  # Prepare data for delegation
  data = {
      "task_summary": task_summary,
      "achievement_highlights": arguments.get('achievement_highlights', []),
      "pending_tasks": arguments.get('pending_tasks', [])
  }

  # Delegate to the Lead Assistant for daily summary generation
  assistant_id = "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Replace with the actual assistant ID
  response = requests.post(
      f"https://api.assistant.com/assistants/{assistant_id}/functions/generate_daily_summary",
      json=data)

  # Handle response from the Lead Assistant
  response.raise_for_status()  # Raise an exception if the request failed
  return response.json(
  )  # Return the JSON response containing the daily summary


# Example usage of generate_daily_summary
task_summary = [{
    "task": "Complete coding task",
    "status": "Completed",
    "notes": "Completed ahead of schedule"
}, {
    "task": "Attend project meeting",
    "status": "Completed",
    "notes": "Discussed design requirements"
}]
achievement_highlights = [
    "Resolved critical bug", "Received positive feedback from client"
]
pending_tasks = [{
    "task": "Write unit tests",
    "expected_completion": "Tomorrow"
}, {
    "task": "Prepare presentation",
    "expected_completion": "Next week"
}]

report = generate_daily_summary({
    "task_summary": task_summary,
    "achievement_highlights": achievement_highlights,
    "pending_tasks": pending_tasks
})
print(report)  # Print the generated daily summary
