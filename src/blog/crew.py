# Warning control
import warnings
warnings.filterwarnings('ignore')
from crewai import Crew
from blog.agents import planner, writer, editor
from blog.tasks import plan, write, edit

topic = "Web3 Social Network"

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

def kickoff(inputs):
  return crew.kickoff(inputs)
