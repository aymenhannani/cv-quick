from tools.tools import skill_parser
import json
from smolagents import CodeAgent, HfApiModel
import yaml
from tools.final_answer import FinalAnswerTool
from Gradio_UI import GradioUI
# Sample Job Description for Testing
job_description = """
Phi Partners is a leading global consultancy specialising in treasury and capital markets technology. With a dedicated workforce of over 650 professionals, we have established ourselves as experts in third-party vendor applications, notably Sophis/Fusion Invest, Summit, and Murex. Our esteemed client base includes top-tier financial institutions such as investment banks, hedge funds, private equity firms, and asset management companies. Founded in 2004, Phi Partners is headquartered in London and has a global footprint with a presence in all major continents. Our strategic nearshore delivery centers are located in Bucharest, Casablanca, Sofia, and Nicosia, enabling us to offer tailored, high-quality services across different time zones and regions.

Our consultants in the Sophis/Fusion Invest practice are primarily based in Casablanca and Bucharest. The Casablanca Centre of Excellence, located in Casablanca Finance City (CFC), employs over 80 consultants focused on Sophis/Fusion Invest and quantitative services. From CFC, we support international clients in key financial hubs such as New York, London, and Paris. Meanwhile, our Bucharest Centre of Excellence, situated in the Euro Tower Building, boasts a team of over 200 consultants specialising in various business lines, including front-toback office trading applications and risk technology services. Together, these centers enhance our ability to serve clients with expertise and efficiency in the rapidly evolving financial landscape.

About The Practice

Phi Partners is the largest consultancy in the world specialising in Sophis/Fusion Invest, with a dedicated team of over 70 consultants spread across multiple locations. Our practice is characterised by a deep understanding of the Sophis/Fusion Invest platform, enabling us to deliver exceptional value to our clients through tailored solutions and strategic insights. At Phi Partners, we pride ourselves on fostering a collegiate environment where professionals collaborate to deliver complex services to elite clients.

We offer comprehensive implementation services, guiding clients through the entire lifecycle of the Sophis/Fusion Invest platform, from initial requirements gathering to post-go-live support. Our team also provides ongoing support and maintenance to ensure optimal performance and user satisfaction. Additionally, we focus on custom development, creating tailored solutions that address specific client challenges and regulatory requirements. To empower our clients further, we conduct extensive training and knowledge transfer sessions, ensuring that their teams are well-equipped to leverage the full potential of the Sophis/Fusion Invest system. Through these practice areas, we deliver exceptional value and insights to top-tier financial institutions worldwide.

Roles and Responsibilities

At Phi Partners, our consultants play a vital role in delivering high-impact solutions across our Sophis/Fusion

Invest practice. Key responsibilities include:

Collaborating with clients to gather requirements and understand their specific needs related to the Sophis/Fusion Invest platform.
Designing, developing, and implementing tailored solutions that enhance functionality and address business challenges.
Conducting thorough testing and validation of solutions to ensure quality and compliance with industry standards.
Providing ongoing support and maintenance services to optimise system performance and user experience.
Engaging in knowledge transfer and training initiatives to empower client teams and ensure effective utilisation of the platform.
Staying updated on industry trends, regulatory changes, and advancements in technology to provide informed insights and recommendations.


Key Skills

To succeed in our Sophis/Fusion Invest practice, consultants should possess a diverse set of skills, including:

Strong understanding of Sophis/Fusion Invest’s architecture, functionalities, and capabilities.
Experience with relevant programming languages (e.g., C++, Java) and a solid grasp of software development principles.
Familiarity with front-to-back-office trading processes, risk management frameworks, and capital markets operations.
Ability to analyse complex situations, identify issues, and develop effective solutions in a fast-paced environment.
Verbal and written communication skills, with the ability to collaborate effectively with clients and team members.
Willingness to stay updated on industry trends, regulatory changes, and emerging technologies to enhance service delivery.


Next Steps

If you are passionate about leveraging your expertise in Sophis/Fusion Invest to make a significant impact in the capital markets technology landscape, we invite you to explore opportunities with Phi Partners.

By joining our firm, you will have the opportunity to work alongside industry leaders, enhancing your expertise while contributing to high-impact initiatives. We are always on the lookout for talented professionals who thrive in a dynamic, collaborative environment.
"""

data_path="data/cv.json"
with open(data_path) as f:
    d = json.load(f)
#Call the function with the correct data type
answer = skill_parser(d)
#Set up Final Answer Tool
final_answer = FinalAnswerTool()
#Construct a model
model= HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
    custom_role_conversions=None,
)
#Act-Thought Prompt
with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)


# We're creating our CodeAgent
agent = CodeAgent(
    model=model,
    tools=[final_answer,skill_parser], # add your tools here (don't remove final_answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates
)


#Launching Gradio Interface
GradioUI(agent).launch()
