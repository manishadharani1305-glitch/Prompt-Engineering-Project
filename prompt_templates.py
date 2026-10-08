def zero_shot_prompt(task):
    return f"""
Answer the following task directly and clearly.

Task:
{task}
"""


def one_shot_prompt(task):
    return f"""
You are an AI assistant.

Example:
Task: What is photosynthesis?
Answer: Photosynthesis is the process by which green plants use sunlight, water, and carbon dioxide to produce food and oxygen.

Now answer the new task in the same style.

Task:
{task}
"""


def few_shot_prompt(task):
    return f"""
You are an AI assistant. Follow the pattern shown in the examples.

Example 1:
Task: What is AI?
Answer: AI is the ability of machines to perform tasks that normally require human intelligence.

Example 2:
Task: What is a database?
Answer: A database is an organized collection of data that can be stored, managed, and retrieved easily.

Example 3:
Task: What is Python?
Answer: Python is a high-level programming language known for its simple syntax and wide range of applications.

Now answer the following task using the same clear pattern.

Task:
{task}
"""


def cot_prompt(task):
    return f"""
Solve the following task carefully.

Think through the important steps internally and provide a concise explanation
of the key steps. Do not reveal private or hidden chain-of-thought.

Task:
{task}
"""


def manual_cot_prompt(task):
    return f"""
Solve the following task using this explicit structure:

Step 1: Understand the task.
Step 2: Identify the important information.
Step 3: Work through the solution.
Step 4: Give the final answer.

Task:
{task}
"""


def tot_prompt(task):
    return f"""
Solve the following task by considering multiple possible approaches.

Approach 1:
Find one possible way to solve the task.

Approach 2:
Find another possible way to solve the task.

Approach 3:
Find a third possible way if useful.

Compare the approaches briefly and select the most suitable one.
Then provide the final answer.

Task:
{task}
"""