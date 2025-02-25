from smolagents import tool, HfApiModel
import json


@tool
def skill_parser(arg1:dict)-> str: # it's important to specify the return type
    # Keep this format for the tool description / args description but feel free to modify the tool
    """A tool that returns the skills needed to create work experience blocs for the resume.
    Args:
        arg1: the first argument
    """
    
    return arg1["ExpÃ©rience"]


#Job Reader Tool
@tool
def job_reader(arg1:str)-> str: # it's important to specify the return type
    # Keep this format for the tool description / args description but feel free to modify the tool
    """A tool that reads the user prompt and store it as the job description.
    Args:
        arg1: the first argument
    """
    
    return str(arg1)


#Resume Optimizer
@tool
def resume_optimizer_prompt(arg1:str,arg2:str)-> str: # it's important to specify the return type
    # Keep this format for the tool description / args description but feel free to modify the tool
    """A tool that creates the prompt for the resume optimizer generation, inputs are user skills data and job description.
    Args:
        arg1: the first argument
        arg2: the second argument
    """
    prompt="Write Optimized Resume sections for the following job description and user skills\n\n"
    return prompt+"Job Description : \n"+arg1+"\n"+"User Skills : \n"+arg2


from smolagents import tool

@tool
def generate_experience(arg1: str) -> str:
    """
    A tool that takes a resume optimizer prompt and generates an optimized experience
    section for a resume using text generation via Hugging Face's API.
    
    Args:
        arg1: A string containing the resume optimizer prompt.
    
    Returns:
        A string representing the optimized experience section.
    """
    # Instantiate the text generation model.
    # You can adjust the model_id, max_tokens, and temperature as needed.
    model = HfApiModel(
        max_tokens=200,
        temperature=0.5,
        model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        custom_role_conversions=None,
    )
    
    # Generate text using the model with the provided prompt.
    generated_experience = model.generate(arg1)
    
    return generated_experience


