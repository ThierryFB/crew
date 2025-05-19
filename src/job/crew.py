import warnings
from crewai import Crew
from src.job.config.agents import researcher, profiler, resume_strategist
from src.job.config.tasks import profile_task, research_task, resume_strategy_task

warnings.filterwarnings("ignore")

crew = Crew(
    agents=[researcher, profiler, resume_strategist],
    tasks=[research_task, profile_task, resume_strategy_task],
    verbose=True,
)


def kickoff():

    job_application_inputs = {
        "job_posting_url": "https://jobs.ashbyhq.com/kraken.com/a4d4b116-ef70-45f8-950b-e2192fc56cb2",
        "linkedin_url": "https://www.linkedin.com/in/thierryferland/",
        "personal_writeup": """Experienced technology leader transitioning from a CTO role to pursue hands-on
        development in the web3 space. Combining a strong background in FullStack
        development, software architecture, and DevOps with a growing passion for
        blockchain, cryptocurrency, and DeFi. Eager to apply extensive technical expertise
        and leadership experience to innovative projects in the decentralized ecosystem.
        Actively expanding proficiency in web3 technologies to drive cutting-edge solutions
        in this rapidly evolving field.""",
    }
    output = crew.kickoff(inputs=job_application_inputs)
    print(output.raw)
    return output.raw
