# Warning control
import warnings
warnings.filterwarnings('ignore')
import os
from utils import get_openai_api_key, save_markdown_to_file
from IPython.display import Markdown
from linkedin.crew import kickoff

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

topic = "Web3 Social Network"
result = kickoff(inputs={"topic": topic})

# Save the result to a file
output_path = "./output/output.md"
save_markdown_to_file(result, output_path)

# Markdown(result)

