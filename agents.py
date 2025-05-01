"""
Minimal implementation of the Agents SDK to make the example run.
"""
import asyncio
import uuid
from dataclasses import dataclass
from typing import Any, Callable, List, Optional, Type, TypeVar, Union
from contextlib import contextmanager

T = TypeVar('T')

def gen_trace_id() -> str:
    """Generate a unique trace ID."""
    return str(uuid.uuid4())

@contextmanager
def trace(name: str, trace_id: str = None):
    """Context manager for tracing operations."""
    if trace_id is None:
        trace_id = gen_trace_id()
    print(f"Starting trace: {name} (ID: {trace_id})")
    try:
        yield trace_id
    finally:
        print(f"Ending trace: {name} (ID: {trace_id})")

@contextmanager
def custom_span(name: str):
    """Context manager for custom spans within a trace."""
    print(f"Starting span: {name}")
    try:
        yield
    finally:
        print(f"Ending span: {name}")

@dataclass
class RunResult:
    """Result of running an agent."""
    final_output: Any
    
    def final_output_as(self, cls: Type[T]) -> T:
        """Convert the final output to the specified type."""
        if isinstance(self.final_output, cls):
            return self.final_output
        # For demonstration, assume we can just create a new instance
        # This is a simplification and may not work for all cases
        try:
            return cls(**vars(self.final_output))
        except:
            return self.final_output  # Fallback
    
    @classmethod
    def create_streaming_result(cls, final_output: Any):
        """Create a streaming run result."""
        result = cls(final_output=final_output)
        result.stream_events = lambda: _stream_events_generator(final_output)
        return result

async def _stream_events_generator(final_output):
    """Generate stream events for streaming results."""
    # Simulate some streaming activity
    for _ in range(3):
        await asyncio.sleep(1)
        yield {"type": "thinking"}

class Agent:
    """Base class for agents."""
    def __init__(self, name: str, instructions: str = "", model: str = "gpt-4", output_type=None, description: str = "", tools=None, model_settings=None):
        self.name = name
        self.instructions = instructions
        self.model = model
        self.output_type = output_type
        self.description = description
        self.tools = tools if tools is not None else []
        self.model_settings = model_settings
        # Make __name__ available for identification in Runner
        self.__name__ = name
        
    def as_tool(self, tool_name: str, tool_description: str, custom_output_extractor=None):
        """Convert this agent to a tool that can be used by other agents."""
        return AgentTool(self, tool_name, tool_description, custom_output_extractor)
        
    def clone(self, tools=None):
        """Create a clone of this agent with the specified tools."""
        new_agent = Agent(
            name=self.name, 
            instructions=self.instructions,
            model=self.model,
            output_type=self.output_type,
            description=self.description
        )
        new_agent.tools = tools if tools is not None else []
        return new_agent

class AgentTool:
    """A tool created from an agent."""
    def __init__(self, agent: Any, name: str, description: str, output_extractor=None):
        self.agent = agent
        self.name = name
        self.description = description
        self.output_extractor = output_extractor

class WebSearchTool:
    """A tool for web searching."""
    def __init__(self):
        self.name = "web_search"
        self.description = "Search the web for financial information"
    
    def __call__(self, query: str) -> str:
        """Simulate a web search."""
        print(f"Searching the web for: {query}")
        return f"Search results for: {query}\n\nKey financial metrics show strong performance in the latest quarter. Revenue increased by 15% year-over-year, exceeding analyst expectations. Operating margin improved to 28.7%, up from 27.2% in the previous quarter. The company also announced a new share buyback program."

class Runner:
    """Static class for running agents."""
    @staticmethod
    async def run(agent: Any, input_data: str) -> RunResult:
        """Run an agent with the given input."""
        agent_name = getattr(agent, "__name__", "unnamed")
        print(f"Running agent: {agent_name}")
        print(f"Input: {input_data}")
        print(f"Using model: {getattr(agent, 'model', 'unknown')}")
        
        # For demonstration, create a simple output based on the agent type
        if agent_name == "FinancialPlannerAgent":
            from agents.planner_agent import FinancialSearchPlan, FinancialSearchItem
            output = FinancialSearchPlan(
                searches=[
                    FinancialSearchItem(
                        query="Recent quarterly earnings report", 
                        reason="To understand current financial performance"
                    ),
                    FinancialSearchItem(
                        query="Revenue growth year-over-year", 
                        reason="To track growth trajectory"
                    ),
                    FinancialSearchItem(
                        query="Industry outlook and trends", 
                        reason="To understand market context"
                    ),
                    FinancialSearchItem(
                        query="Competitive landscape", 
                        reason="To assess competitive position"
                    ),
                    FinancialSearchItem(
                        query="Recent product launches", 
                        reason="To evaluate innovation pipeline"
                    ),
                    FinancialSearchItem(
                        query="Regulatory changes affecting the company", 
                        reason="To identify regulatory risks or opportunities"
                    ),
                    FinancialSearchItem(
                        query="Analyst ratings and forecasts", 
                        reason="To understand market sentiment"
                    )
                ]
            )
        elif agent_name == "search_agent":
            output = f"Search results for: {input_data}\n\nKey financial metrics show strong performance in the latest quarter. Revenue increased by 15% year-over-year, exceeding analyst expectations. Operating margin improved to 28.7%, up from 27.2% in the previous quarter. The company also announced a new share buyback program."
        elif agent_name == "financials_agent":
            output = type("AnalysisSummary", (), {"summary": "The company shows strong financial performance with 15% YoY revenue growth, operating margins of 28.7% (up 1.5 percentage points), and a healthy cash position of $45B. Return on invested capital (ROIC) stands at 22%, outperforming the industry average of 18%."})()
        elif agent_name == "risk_agent":
            output = type("AnalysisSummary", (), {"summary": "Potential risks include intensifying competition in the core market, regulatory scrutiny in key regions, and supply chain disruptions affecting production capacity. The company's high concentration in a single product line (60% of revenue) presents additional vulnerability."})()
        elif agent_name == "FinancialWriterAgent":
            from agents.writer_agent import FinancialReportData
            output = FinancialReportData(
                markdown_report=(
                    "# Financial Analysis Report\n\n"
                    "## Executive Summary\n\n"
                    "The company demonstrates strong financial performance with 15% year-over-year revenue growth and improved operating margins of 28.7%. However, there are notable risks from competition, regulatory scrutiny, and supply chain vulnerabilities that warrant monitoring.\n\n"
                    "## Financial Performance\n\n"
                    "Revenue growth of 15% year-over-year exceeded analyst expectations, demonstrating robust demand for the company's products and services. Operating margins improved to 28.7%, up from 27.2% in the previous quarter, reflecting enhanced operational efficiency and economies of scale. The company maintains a strong cash position of $45 billion, providing ample resources for strategic investments and shareholder returns.\n\n"
                    "The return on invested capital (ROIC) stands at an impressive 22%, outperforming the industry average of 18%. This indicates effective capital allocation and value creation for shareholders.\n\n"
                    "## Risk Assessment\n\n"
                    "While the financial metrics are strong, several risk factors require attention:\n\n"
                    "- **Competitive Intensity**: The market is experiencing increased competition, potentially pressuring future pricing and market share.\n"
                    "- **Regulatory Environment**: Heightened regulatory scrutiny in key markets could impact operational flexibility and compliance costs.\n"
                    "- **Supply Chain Vulnerabilities**: Ongoing disruptions affect production capacity and could constrain growth if unresolved.\n"
                    "- **Product Concentration**: With 60% of revenue derived from a single product line, the company faces concentration risk.\n\n"
                    "## Market Outlook\n\n"
                    "Industry trends remain favorable, with digital transformation driving sustained demand. Analyst sentiment is predominantly positive, with 75% of analysts maintaining 'buy' ratings despite acknowledging competitive and regulatory challenges.\n\n"
                    "## Conclusion\n\n"
                    "The company's financial strength provides a solid foundation for navigating identified risks. Management's strategic focus on diversification and supply chain resilience should help mitigate key vulnerabilities going forward."
                ),
                short_summary="The company shows strong financial performance with 15% revenue growth and improved margins, while facing manageable risks from competition, regulation, and supply chain challenges.",
                follow_up_questions=[
                    "What specific initiatives is management implementing to diversify the product portfolio?",
                    "How is the company addressing supply chain vulnerabilities?",
                    "What is the expected impact of regulatory changes on the next fiscal year?",
                    "How does the capital allocation strategy compare to industry peers?"
                ]
            )
        elif agent_name == "verifier_agent":
            from agents.verifier_agent import VerificationResult
            output = VerificationResult(
                issues=["No major inconsistencies found in the report."],
                overall_assessment="The report presents a balanced view of both strong financial performance and key risks. Financial metrics are presented accurately, and conclusions are well-supported by the provided data."
            )
        else:
            output = type("GenericOutput", (), {"summary": f"Generated output for {input_data}"})()
            
        return RunResult(final_output=output)
    
    @staticmethod
    def run_streamed(agent: Any, input_data: str) -> RunResult:
        """Run an agent and stream the results."""
        agent_name = getattr(agent, "__name__", "unnamed")
        print(f"Running streamed agent: {agent_name}")
        print(f"Input: {input_data}")
        print(f"Using model: {getattr(agent, 'model', 'unknown')}")
        
        # For demonstration, create a simple output
        if hasattr(agent, "tools") and agent.tools:
            from agents.writer_agent import FinancialReportData
            output = FinancialReportData(
                markdown_report=(
                    "# Financial Analysis Report\n\n"
                    "## Executive Summary\n\n"
                    "The company demonstrates strong financial performance with 15% year-over-year revenue growth and improved operating margins of 28.7%. However, there are notable risks from competition, regulatory scrutiny, and supply chain vulnerabilities that warrant monitoring.\n\n"
                    "## Financial Performance\n\n"
                    "Revenue growth of 15% year-over-year exceeded analyst expectations, demonstrating robust demand for the company's products and services. Operating margins improved to 28.7%, up from 27.2% in the previous quarter, reflecting enhanced operational efficiency and economies of scale. The company maintains a strong cash position of $45 billion, providing ample resources for strategic investments and shareholder returns.\n\n"
                    "The return on invested capital (ROIC) stands at an impressive 22%, outperforming the industry average of 18%. This indicates effective capital allocation and value creation for shareholders.\n\n"
                    "## Risk Assessment\n\n"
                    "While the financial metrics are strong, several risk factors require attention:\n\n"
                    "- **Competitive Intensity**: The market is experiencing increased competition, potentially pressuring future pricing and market share.\n"
                    "- **Regulatory Environment**: Heightened regulatory scrutiny in key markets could impact operational flexibility and compliance costs.\n"
                    "- **Supply Chain Vulnerabilities**: Ongoing disruptions affect production capacity and could constrain growth if unresolved.\n"
                    "- **Product Concentration**: With 60% of revenue derived from a single product line, the company faces concentration risk.\n\n"
                    "## Market Outlook\n\n"
                    "Industry trends remain favorable, with digital transformation driving sustained demand. Analyst sentiment is predominantly positive, with 75% of analysts maintaining 'buy' ratings despite acknowledging competitive and regulatory challenges.\n\n"
                    "## Conclusion\n\n"
                    "The company's financial strength provides a solid foundation for navigating identified risks. Management's strategic focus on diversification and supply chain resilience should help mitigate key vulnerabilities going forward."
                ),
                short_summary="The company shows strong financial performance with 15% revenue growth and improved margins, while facing manageable risks from competition, regulation, and supply chain challenges.",
                follow_up_questions=[
                    "What specific initiatives is management implementing to diversify the product portfolio?",
                    "How is the company addressing supply chain vulnerabilities?",
                    "What is the expected impact of regulatory changes on the next fiscal year?",
                    "How does the capital allocation strategy compare to industry peers?"
                ]
            )
        else:
            from agents.writer_agent import FinancialReportData
            output = FinancialReportData(
                markdown_report="# Financial Report\n\nThis is a sample report.",
                short_summary="This is a short summary of the financial report.",
                follow_up_questions=["What about next quarter?", "Any risks to consider?"]
            )
            
        return RunResult.create_streaming_result(output)