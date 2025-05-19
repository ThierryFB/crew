# Warning control
import warnings
from crewai import Task
from src.linkedin.config.agents import (
    content_strategist,
    industry_analyst,
    audience_persona_expert,
    content_writer,
    engagement_optimizer,
    content_editor,
    domain_expert,
)

warnings.filterwarnings("ignore")

strategy_task = Task(
    description="""Develop a content strategy for the next 2 weeks based on current business
    focus (retail tech for Choclo/Obius) and audience interests. Include 3 main themes to cover
    and ideal posting frequency. Consider Thierry's experience with retail tech, ERP systems,
    and e-commerce optimization.""",
    agent=content_strategist,
    expected_output="A content strategy document with themes, frequency, and goals.",
)

research_task = Task(
    description="""Research the latest trends related to the themes identified by the
    Content Strategist. Identify 3-5 talking points for each theme, including statistics,
    recent industry developments, or noteworthy case studies that Thierry could reference.""",
    agent=industry_analyst,
    expected_output="Research report with talking points for each content theme.",
)

audience_analysis_task = Task(
    description="""For each content theme, identify which audience personas would find it most
    relevant and why. Suggest specific pain points or aspirations to address for each persona.""",
    agent=audience_persona_expert,
    expected_output="Audience relevance analysis for each theme.",
)

content_creation_task = Task(
    description="""Based on the topic, which is {topic}, the instructions,
    which are the following {instruction} and the brainstorm ideas, which are the following {brainstorm},
    create three version of the same LinkedIn posts in Thierry's authentic voice, incorporate relevant
    talking points. Follow topic, instructions and brainstorm ideas.""",
    agent=content_writer,
    expected_output="Three version of the same LinkedIn posts ready for optimization.",
    human_input=True,
)

tech_review_task = Task(
    description="""Review all three posts to make sure they are technically accurate.""",
    agent=domain_expert,
    expected_output="Technically accurate versions of all three LinkedIn posts ready for optimization.",
    context=[content_creation_task],
)

optimization_task = Task(
    description="""Optimize each post for maximum engagement. Suggest formatting improvements,
    refine hooks if needed, add appropriate emojis.""",
    agent=engagement_optimizer,
    expected_output="Optimized versions of each LinkedIn post with formatting and hashtags.",
    context=[tech_review_task],
)

final_review_task = Task(
    description="""Review and finalize all three posts. Check for grammar, clarity, brand consistency,
    and alignment with Thierry's professional image. Make final edits as needed.""",
    agent=content_editor,
    expected_output="Final versions of all three LinkedIn posts ready for publishing.",
    context=[optimization_task],
)
