# Warning control
import warnings
import os
from src.utils import save_markdown_to_file  # ,get_openai_api_key

# from IPython.display import Markdown
from src.linkedin.crew import kickoff as linkedin_kickoff

# from blog.crew import kickoff as blog_kickoff
# from investment.crew import kickoff as investment_kickoff
from src.job.crew import kickoff as job_kickoff

# openai_api_key = get_openai_api_key()
# os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

warnings.filterwarnings("ignore")

match os.environ["APP"]:
    case "linkedin":
        TOPIC = "Web3 Social Network"
        BRAINSTORM = (
            "conventional social media are making a lot of money with your data"
            "web 1 was read, web 2 is read-write, web3 is read-write-own"
            "what if you could still own your data."
            "web3 social medial have the potential to do that."
            "isn't it the best, what is the catch?"
            "actually, you don't own your data, it's own by all users"
            "but you do get rewared when you help the network"
            "wheter it's by running a node or by providing content"
        )
        INSTRUCTION = """write a linkedpost that introduces the concept of web3
        social networks and list them along with their particularities"""
        result = linkedin_kickoff(
            inputs={
                "topic": TOPIC,
                "brainstorm": BRAINSTORM,
                "instruction": INSTRUCTION,
            }
        )
        OUTPUT_PATH = "./output/output.md"
        save_markdown_to_file(result, OUTPUT_PATH)
    case "job":
        result = job_kickoff()
    # case "investment":
    #   result = investment_kickoff()
    # case "blog":
    #   result = blog_kickoff()
