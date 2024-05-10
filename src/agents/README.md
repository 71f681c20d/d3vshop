# Agent Configuration

- Here is where the AI agents for the D3vshop are configured.
- These agents are reusable team members that will participate in various parts of the workflow
- The agents should cover all specializations required to complete the workflow, and represent the interests of all stakeholders in the operation

Agents are fully configurable
    - API service configuration (loaded from OAI_CONFIG_LIST)
    - LLM configuration (temperature, seed, etc...)
    - Code execution configuration (use_docker, work_dir, etc...)
    - System message for the agent (defines the role of the agent)
    - Termination message (defines the string patterns that will terminate the agent)
    - Load a specific docker container to be used as the execution environment for the agent (development environment)
    - Load a set of tools that the agent can use to interact with the environment (outside world)

This allows you to customize what each agent is able to do, and other things.
- For example, the Groq API is very fast. If the groq API is used for the agents, then the entire workflow can be executed very quickly
- You may want to develop and test your conversational workflow with a slower or local API, and then once it's running smoothly, switch out the API to groq while keeping everything else the same
- Conversely, you could update dependencies in the docker image used as a dev environment, while leaving everything else the same

