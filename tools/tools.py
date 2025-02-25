from smolagents import tool
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
    """A tool that reads and store the job description.
    Args:
        arg1: the first argument
    """
    
    return str(arg1)


#Resume Optimizer
@tool
def resume_optimizer(arg1:str,arg2:str)-> str: # it's important to specify the return type
    # Keep this format for the tool description / args description but feel free to modify the tool
    """A tool that combine a job description and a the user skill json string to be treated by the model to generate the experiece section.
    Args:
        arg1: the first argument
        arg2: the second argument
    """
    
    return "Job Description : \n"+arg1+"\n"+"User Skills : \n"+arg2


from smolagents import tool

@tool
def generate_experience( arg1: str) -> str:
    """
    A tool that takes user data and a job description as input, and generates an optimized experience
    section for a resume using text generation.
    
    Args:
        arg1: the first argument
    
    Returns:
        A string representing the optimized experience section.
    """
    data_path="data/cv.json"
    with open(data_path) as f:
        d = json.load(f)
    # Extract skills from the user_data dictionary.
    skills = d.get("skills", [])
    # Convert the skills list to a comma-separated string.
    skills_str = ", ".join(skills) if isinstance(skills, list) else str(skills)
    
    # Build the prompt for text generation.
    prompt = (
        f"Job Description:\n{arg1}\n\n"
        f"User Skills:\n{skills_str}\n\n"
        "Based on the above, generate an optimized experience section for a resume that highlights relevant work experience."
    )
    
    # Here you would call your text generation model (e.g., via HfApiModel or another method).
    # For demonstration purposes, we'll simulate the output.
    generated_experience = f"[Generated Experience Section based on prompt]:\n{prompt}"
    
    return generated_experience



