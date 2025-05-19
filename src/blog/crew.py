# Warning control
import warnings
from crewai import Crew
from src.blog.config.agents import planner, writer, editor
from src.blog.config.tasks import plan, write, edit

warnings.filterwarnings("ignore")

TOPIC = "Web3 Social Network"

crew = Crew(agents=[planner, writer, editor], tasks=[plan, write, edit], verbose=2)


def kickoff(inputs):
    return crew.kickoff(inputs)
