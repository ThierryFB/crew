# Warning control
import warnings
warnings.filterwarnings('ignore')
from crewai import Crew
import os
from utils import get_openai_api_key, save_markdown_to_file
from linkedin.agents import content_strategist, industry_analyst, audience_persona_expert, content_writer, engagement_optimizer, content_editor
from linkedin.tasks import strategy_task, research_task, audience_analysis_task, content_creation_task, optimization_task, final_review_task

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

topic = "Web3 Social Network"

crew = Crew(
  agents=[
    content_strategist,
    industry_analyst,
    content_writer,
    audience_persona_expert,
    engagement_optimizer,
    content_editor
  ],
  tasks=[
    strategy_task,
    research_task,
    audience_analysis_task,
    content_creation_task,
    optimization_task,
    final_review_task
  ],  # Tasks would be defined separately
  verbose=2
)

def kickoff(inputs):
  return crew.kickoff(inputs)

