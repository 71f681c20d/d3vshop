# Architecture Design

How do you go about designing powerful multi-agent AI applications?
- Conversational workflows can be broken down in to 2 denominations:
    - Group chat; many-to-many conversation between agents
    - Sequential chat; one-to-one conversation between agents
- An agent in a conversation could be an entire conversation itself. The message sent to that agent would be the input task of the nested conversation. The final output of that conversation would be the response from the agent in the larger conversation. This allows for composability.
- Group chats might be better for collaborating across diverse domains of expertise, while sequential chats may be better for accomplishing specified tasks.
- Both of these can be implmented together so that very fine-grained expertise can be included in technical implmentations

Configuration
- There are multiple types of configuration
    - Agent configuration
        - AI model selection, and runtime parameters like temperature
        - "System message"; A prompt describing the agent's role, expertise, behaviors, and characteristics
        - Which environment configuration to use
        - Termination messages
    - Environment configuration
        - Stuff that the agents use to do their work
        - Reusable docker containers (development environments) with preinstalled software and specific versions of dependencies
        - Reference documentation an agent may use to do their work
        - Tools (python functions) an agent may invoke to interact with the outside world
    - Conversation configuration
        - Each conversation can be configured differently to produce different types of behaviors
        - A group chat could have each agent take turns speaking, or some speaking and some agents only listening, or agents allowed to chime in whenever they want
        - Each conversation has specific details that describe the flow of that conversation, and changing them will change the behavior

