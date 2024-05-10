import autogen

def ask_manager(message):
    po.initiate_chat(manager, message=message)
    # return the last message received from the planner
    return po.last_message()["content"]


''' Agent declarations '''
user_proxy = autogen.UserProxyAgent( # Work with the PO to refine requirements; Human
   name="Manager",
   system_message="A human admin.",
   code_execution_config={"last_n_messages": 2, "work_dir": "devshop", "use_docker": True},
   is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
   human_input_mode="ALWAYS",
   max_consecutive_auto_reply=10,
   function_map={"ask_manager": ask_manager},
#    is_termination_msg=lambda x: "content" in x and x["content"] is not None and x["content"].rstrip().endswith("TERMINATE"),
)

po = autogen.AssistantAgent( # Represents the manager and the set of requirements; GPT3.5
    name="Product Owner",
    llm_config={"config_list": config_list_gpt35, "seed": 42, "temperature": 0, "request_timeout": 120, "use_cache": True},
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    # code_execution_config={"last_n_messages": 2, "work_dir": "devshop"},
    system_message="""Product Owner. Reply TERMINATE if the task has been completed to full satisfaction. You are a helpful assistant highly skilled in representing business requirements and business users for the purposes of software development. Your job is to provide business requirements for software teams, clarify those requirements is needed, and scrutinize the finished software to assure the requirements are satisfied.

    Do not suggest code.
    When unit tests are presented to you by the Engineering Analyst, you need to make sure that the test functions contain code which will fail until the appropriate software implementation is built.
    """,
)

engineer = autogen.AssistantAgent( # By default already good at coding; GPT4
    name="Engineer", 
    llm_config={"config_list": config_list_gpt4, "seed": 42, "temperature": 0, "request_timeout": 120, "use_cache": True},
    code_execution_config={"last_n_messages": 2, "work_dir": "devshop"},
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
)
''' End agent declarations'''
