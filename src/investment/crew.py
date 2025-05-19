from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from src.investment.config.agents import (
    data_analyst_agent,
    trading_strategy_agent,
    execution_agent,
    risk_management_agent,
)
from src.investment.config.tasks import (
    data_analysis_task,
    strategy_development_task,
    execution_planning_task,
    risk_assessment_task,
)

# Define the crew with agents and tasks
crew = Crew(
    agents=[
        data_analyst_agent,
        trading_strategy_agent,
        execution_agent,
        risk_management_agent,
    ],
    tasks=[
        data_analysis_task,
        strategy_development_task,
        execution_planning_task,
        risk_assessment_task,
    ],
    manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
    process=Process.hierarchical,
    verbose=True,
)


def kickoff():

    financial_trading_inputs = {
        "stock_selection": "AAPL",
        "initial_capital": "100000",
        "risk_tolerance": "Medium",
        "trading_strategy_preference": "Day Trading",
        "news_impact_consideration": True,
    }
    output = crew.kickoff(inputs=financial_trading_inputs)
    print(output.raw)
    return output.raw
