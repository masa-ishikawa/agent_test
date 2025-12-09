from typing import Dict
from oci.addons.adk import Agent, AgentClient, tool

# Use @tool to signal that this Python function is a function tool.
# Apply standard docstring to provide function and parameter descriptions.
@tool
def get_weather(location: str) -> Dict[str, str]:
    """
    指定した場所の天気を取得します。


    Args:
      location(str): 天気情報を取得する場所
    """
    return {"location": location, "temperature": 72, "unit": "F"}


def main():
    # Create an agent client with your authentication and region details
    # Replace the auth_type with your desired authentication method.
    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="us-chicago-1",
    )

    # Create a local agent object with the client, instructions, and tools.
    # You also need the agent endpoint id. To obtain the OCID, follow Step 1.
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint.oc1.us-chicago-1.xxxxxxxxxxxx",
        instructions="ツールを使用して天気予報のクエリを実行します。",
        tools=[get_weather]
    )

    # Sync local instructions and tools to the remote agent resource
    # You only need to invoke setup() when you change instructions and tools
    agent.setup()

    # Run the agent. You can embed this method in your webapp, slack bot, etc.
    # You invoke the run() when you need to handle your user's request.
    input = "シアトルは寒いですか？"
    response = agent.run(input)

    # Print the response
    response.pretty_print()

if __name__ == "__main__":
    main()