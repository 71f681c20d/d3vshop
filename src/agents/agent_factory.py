'''
    Factory pattern for constructing new agents based on JSON configs. 
    Configuration includes:
    - API service configuration (loaded from OAI_CONFIG_LIST)
    - LLM configuration (temperature, seed, etc...)
    - Code execution configuration (use_docker, work_dir, etc...)
    - System message for the agent (defines the role of the agent)
    - Termination message (defines the string patterns that will terminate the agent)

    TODO:
    - Load a specific docker container to be used as the execution environment for the agent
    - Load a set of tools that the agent can use to interact with the environment (outside world)
'''
import os
import json
import autogen


class AgentFactory:
    def __init__(self):
        self.config_file = "OAI_CONFIG_LIST"
    
    def get_api_config(self, provider, tag):
        # Load API configuration data (from OAI_CONFIG_LIST)
        return autogen.config_list_from_json(
            env_or_file="OAI_CONFIG_LIST",
            filter_dict={
                "provider": provider,
                "tag": tag
            }
        )

    def create_agents_from_json(self):
        with open('./devshop_agents.json') as f:
            json_objects = json.load(f)
            # TODO check against schema
            agents = []
            for agent in json_objects:
                # Load API configuration data (from OAI_CONFIG_LIST)
                agent['llm_config']['config_list'] = self.get_api_config(agent['provider'], agent['tag'])
                # Initialize the agent
                autogen.AssistantAgent(
                    name=agent['name'],
                    llm_config=agent['llm_config'],
                    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith(agent['termination_message']),
                    code_execution_config=agent['code_execution_config'],
                    system_message=agent['system_message'],
                )
                print('Agent created: '+agent['name'])
                agents.append(agent)
        return agents


agent_factory = AgentFactory()
agent_factory.create_agents_from_json()


