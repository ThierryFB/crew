# Warning control
import warnings
from crewai import Crew
from src.linkedin.config.agents import (
    content_writer,
    engagement_optimizer,
    content_editor,
    domain_expert,
)
from src.linkedin.config.tasks import (
    content_creation_task,
    tech_review_task,
    optimization_task,
    final_review_task,
)
from src.linkedin.config.knowledge import get_knowledge_sources

warnings.filterwarnings("ignore")

knowledge_sources = get_knowledge_sources()

crew = Crew(
    agents=[
        content_writer,
        domain_expert,
        engagement_optimizer,
        content_editor,
    ],
    tasks=[
        content_creation_task,
        tech_review_task,
        optimization_task,
        final_review_task,
    ],
    verbose=True,
    knowledge_sources=knowledge_sources,
)


def kickoff(inputs):
    output = crew.kickoff(inputs)
    print(output.raw)
    return output.raw
