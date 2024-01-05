import os
import openai  # Import the OpenAI API library

# Set your OpenAI API key as an environment variable
openai.api_key = os.environ['OPENAI_API_KEY']

# The tool configuration with assistant ID
tool_config = {
    "type": "function",
    "function": {
        "name": "learn_from_outcomes",
        "description":
        "Allows the system to continuously learn from interactions, feedback, and task outcomes to improve performance over time.",
        "parameters": {
            "type": "object",
            "properties": {
                "outcome_details": {
                    "type": "object",
                    "description": "Detailed information about task outcomes."
                },
                "learning_context": {
                    "type": "string",
                    "description": "Context for learning (optional)."
                },
                "outcome_id": {
                    "type":
                    "string",
                    "description":
                    "Unique identifier for specific outcomes or task instances (optional)."
                }
            },
            "required": ["outcome_details"]
        }
    },
    "assistant_id":
    "asst_pkTOfztu8IdvPCssMbSz5NTh"  # Set the Lead Assistant ID here
}


# The callback function (Learn from outcomes)
def learn_from_outcomes(arguments):
  """
    Allows the system to continuously learn from interactions, feedback, and task outcomes to improve performance over time using the OpenAI API.

    :param arguments: dict, Contains the necessary information for learning from outcomes.
    Expected keys: outcome_details, learning_context, outcome_id.
    :return: str, Confirmation message of learning from outcomes.
    """

  # Extract required information from arguments
  outcome_details = arguments.get('outcome_details')
  learning_context = arguments.get('learning_context')
  outcome_id = arguments.get('outcome_id')

  # Validate the presence of required information
  if not outcome_details:
    return "Missing required information. Please provide detailed outcome information."

  # Prepare prompt for OpenAI API
  prompt = f"""Learn from the following outcomes:\n
    - Outcome details: {outcome_details}\n
    - Learning context: {learning_context if learning_context else 'General'}\n
    - Outcome ID: {outcome_id if outcome_id else 'None'}\n
    """

  # Call OpenAI API to generate insights for learning from outcomes
  response = openai.Completion.create(
      engine="text-davinci-003",  # Use a powerful text-davinci model
      prompt=prompt,
      max_tokens=150,  # Adjust as needed for desired response length
      n=1,
      stop=None,
      temperature=0.7  # Adjust for creativity vs. coherence
  )

  # Extract generated insights from OpenAI response
  generated_insights = response.choices[0].text.strip()

  # Optionally, you can process and use the generated insights as needed

  return generated_insights  # Return the insights from learning from outcomes
