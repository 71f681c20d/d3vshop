'''
    An implementation of an expert-designed software development shop
'''

import json
import autogen

'''
Conversation Phases:
- Verification (Manager, PO, EA)
- Coding (EA, Engineer)
- Validation (EA, PO, Manager)
'''


''' Chat Chain '''
def refine_requirements(initial_task):
    # PO converse with Mgr to come up with requirements
    manager.initiate_chat(po, message=initial_task)
    # Save requirements to disk
    file = open('Requirements.md', 'w')
    file.write(po.last_message()["content"])
    file.close()
    # return the last message received from the PO
    return po.last_message()["content"]

def write_tests(testing_task):
    # Read requirements from disk
    requirements = open('Requirements.md', 'r').read()
    # PO and EA come up with unit tests
    po.initiate_chat(ea, message=testing_task+requirements) 
    # Save requirements to disk
    file = open('Tests.py', 'w')
    file.write(ea.last_message()["content"])
    file.close()
    # return the last message received from the planner
    return manager.last_message()["content"]

autogen.ChatCompletion.start_logging()


# Requirements
initial_task = 'I want you to gather all of the market data that would have allowed you to predict the collapse of FTX when it happened. I want to develop an application that subscribes to a minimal set of data sources and identifies a major exchange collapse. Then, the application can trigger an order to respond to the collapse. \n Do not sound sonversational in your response. Do not provide greetings, warnings, or other small-talk. Only provide the requirements.'

refine_requirements(initial_task)

# Write tests
# TODO: The unit tests don't have function bodies
testing_task = 'Write a set of unit tests in Python which cover all the requirements. These tests will be used to guide software development in a TDD system. Here is the Requirements.md file:\n'
write_tests(testing_task)

# Develop Code
''' Steps:
- Read unit tests from disk
- EA and Eng come up with code
- Save code to disk
'''
development_task = 'Write the code that passes all these tests. Save the code to disk.'
ea.initiate_chat(engineer, message=development_task)

# Validation
''' Steps: 
- Read docs from disk
- EA present PO with completed project for sign-off
- Save report to disk
'''
validation_task = 'Make sure the finished code is up to snuff.'
ea.initiate_chat(po, message=development_task)

# Final Approval
''' Steps:
- Prompt Mgr for final approval
- Mark for completion; or request change
'''
approval_task = 'The solution is completed and has been validated. Please check our work and approve if satisfactory'
po.initiate_chat(manager, message=approval_task)

''' Things to add:
- Documenting
- pipeline
'''

''' End Chat Chain '''

json.dump(autogen.ChatCompletion.logged_history, open('conversations.json', 'w'), indent=2)


