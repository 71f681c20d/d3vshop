'''
    This contains the agent configuration for a Senior Software Engineer agent. 
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

import autogen

# Load API configuration data (from OAI_CONFIG_LIST)
api_config = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    filter_dict={
        "provider": "groq",
        "tags": ["llama3-8b"],
    },
)

# LLM configuration
llm_config = {"config_list": api_config, "seed": 42, "temperature": 0, "request_timeout": 120, "use_cache": True }

# Code execution configuration
code_execution_config={"last_n_messages": 2, "work_dir": "devshop", "use_docker": False}

# Agent system message
system_message="""Senior Software Engineer. Reply TERMINATE if the task has been completed to full satisfaction. You are a helpful assistant highly skilled in full-stack software development. Your job is to write unit tests, implement software, and validate the software implementation against the requirements.

    Engineers may reach out to you at times for questions regarding their work, but under no circumstances will you ever change requirements at the request of engineers. However, what you can do is provide feedback and advice to engineers so that they can implement the solution and pass your tests.

    All implemented functionality must be accompanied by unit tests. 
    """
# Termination message
is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE")

# Instantiate the agent
senior_engineer = autogen.AssistantAgent(
    name="Senior Software Engineer",
    llm_config=llm_config,
    is_termination_msg=is_termination_msg,
    code_execution_config=code_execution_config,
    system_message=system_message,
)

print('Agent created: '+senior_engineer.name)