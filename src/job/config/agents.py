import os
import warnings
from crewai import Agent
from langchain_anthropic import ChatAnthropic
from src.job.config.tools import (
    scrape_tool,
    search_tool,
    read_resume,
    semantic_search_resume,
)


warnings.filterwarnings("ignore")

# Agent 1: Researcher
researcher = Agent(
    role="Tech Job Researcher",
    goal="Make sure to do amazing analysis on " "job posting to help job applicants",
    tools=[scrape_tool, search_tool],
    verbose=True,
    backstory=(
        "As a Job Researcher, your prowess in "
        "navigating and extracting critical "
        "information from job postings is unmatched."
        "Your skills help pinpoint the necessary "
        "qualifications and skills sought "
        "by employers, forming the foundation for "
        "effective application tailoring."
    ),
    llm=ChatAnthropic(model=os.environ["ANTHROPIC_MODEL"]),
)

# Agent 2: Profiler
profiler = Agent(
    role="Personal Profiler for Engineers",
    goal="Do increditble research on job applicants "
    "to help them stand out in the job market",
    tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
    verbose=True,
    backstory=(
        "Equipped with analytical prowess, you dissect "
        "and synthesize information "
        "from diverse sources to craft comprehensive "
        "personal and professional profiles, laying the "
        "groundwork for personalized resume enhancements."
    ),
    llm=ChatAnthropic(model=os.environ["ANTHROPIC_MODEL"]),
)

# Agent 3: Resume Strategist
resume_strategist = Agent(
    role="Resume Strategist for Engineers",
    goal="Find all the best ways to make a " "resume stand out in the job market.",
    tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
    verbose=True,
    backstory=(
        "With a strategic mind and an eye for detail, you "
        "excel at refining resumes to highlight the most "
        "relevant skills and experiences, ensuring they "
        "resonate perfectly with the job's requirements."
    ),
    llm=ChatAnthropic(model=os.environ["ANTHROPIC_MODEL"]),
)
