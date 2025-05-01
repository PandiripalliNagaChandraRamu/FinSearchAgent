# FinSearch Agent - An Expert Agent for Financial Research

[![Project Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/your-org/FinSearchAgent)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**FinSearch Agent** is a sophisticated financial research agent that leverages a multi-agent system architecture to provide comprehensive and insightful financial analysis. By orchestrating specialized agents, the system efficiently gathers information, performs in-depth analysis, and generates well-structured reports to address a wide range of financial queries.

## Key Features

* **Multi-Agent Architecture:** Employs a collaborative network of specialized agents for planning, information retrieval, analysis, report generation, and verification.
* **Intelligent Planning:** The `FinancialPlannerAgent` intelligently identifies relevant search terms based on the user's request, ensuring targeted information gathering.
* **Comprehensive Information Gathering:** Utilizes tools like `WebSearchTool` and potentially `FileSearchTool` to retrieve concise summaries from diverse sources.
* **Specialized Sub-Analysis:** Integrates specialist agents such as `FundamentalsAnalystAgent` and `RiskAnalystAgent` (exposed as tools) for focused analysis on specific financial aspects.
* **Structured Report Generation:** The `FinancialWriterAgent` synthesizes findings into a comprehensive long-form markdown report, including an executive summary and potential follow-up questions.
* **Rigorous Verification:** The `VerificationAgent` audits the generated report for consistency, clear sourcing, and factual accuracy.
* **Versatile Query Handling:** Supports a wide array of financial research questions, including company analysis, industry trends, investment strategies, market analysis, risk assessment, economic impact, and comparative studies.

## Getting Started

### Prerequisites

* **Python 3.x**
* **pip** (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-org/FinSearchAgent.git](https://github.com/your-org/FinSearchAgent.git)
    cd FinSearchAgent
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    # On Windows PowerShell:
    .venv\Scripts\Activate.ps1
    # On macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt  # Assuming a requirements.txt file exists
    ```
    *(Note: The `requirements.txt` file is not explicitly shown in the provided example. You will need to create one listing the necessary Python packages.)*

### Running the Agent

1.  **Navigate to the project's root directory:**
    ```bash
    cd FinSearchAgent
    ```

2.  **Execute the main script:**
    ```bash
    python main.py
    ```

3.  **Enter your financial research query when prompted:**
    ```
    Write up an analysis of Apple Inc.'s most recent quarter.
    ```

## Example Queries

The FinSearch Agent is designed to handle a variety of financial research inquiries:

### Company Analysis

* "Provide a detailed financial analysis of Tesla, including recent performance and future outlook."
* "Analyze Apple's competitive position against other tech giants and assess its long-term growth potential."

### Industry/Sector Analysis

* "Give me a comprehensive overview of the renewable energy sector, focusing on growth trends and major players."
* "Research the pharmaceutical industry's current challenges and identify emerging growth areas."

### Investment Strategy

* "What are the best dividend stocks to invest in during high inflation periods?"
* "Analyze the potential impact of rising interest rates on tech growth stocks and recommend an investment strategy."

### Market Trend Analysis

* "Assess the current state of the global semiconductor market and forecast trends for the next 18 months."
* "Analyze how ESG investing trends are reshaping investment patterns in traditional energy companies."

### Risk Assessment

* "What are the main geopolitical risks affecting international technology supply chains?"
* "Evaluate the regulatory risks facing major fintech companies in the next 2-3 years."

### Economic Impact Analysis

* "How will ongoing inflation impact consumer discretionary stocks in the next quarter?"
* "Analyze the potential effects of the Federal Reserve's policy changes on emerging market investments."

### Comparison Queries

* "Compare the financial health and growth prospects of the top three cloud computing providers."
* "Analyze and compare the risk-return profiles of major cryptocurrency investments versus traditional gold."

## Project Structure
FinSearchAgent/
├── main.py             # Main script to run the agent
├── agents/             # Directory containing the definitions for each agent
│   ├── init.py
│   ├── financial_planner_agent.py
│   ├── financial_search_agent.py
│   ├── fundamentals_analyst_agent.py
│   ├── risk_analyst_agent.py
│   ├── financial_writer_agent.py
│   └── verification_agent.py
├── tools/              # Directory containing the definitions for various tools
│   ├── init.py
│   ├── web_search_tool.py
│   └── file_search_tool.py
├── config/             # (Optional) Directory for configuration files
│   └── config.yaml
├── data/               # (Optional) Directory for storing data or outputs
├── docs/               # Directory for documentation
│   ├── README.md
│   └── CONTRIBUTING.md
├── tests/              # Directory for unit and integration tests
├── requirements.txt    # List of Python dependencies
├── LICENSE             # Project license
└── CODE_OF_CONDUCT.md  # Code of conduct for contributors


## Contributors

* [PandiripalliNagaChandraRamu](https://github.com/PandiripalliNagaChandraRamu)
* [Aadil -Shaikl](https://github.com/Aadil-Shaik)
* [Rahul Ramesh](https://github.com/Rahulramesh97)
* [Sejal Sanjay Kaul](https://github.com/Sejal-Sanjay-Kaul)

We welcome contributions from the open-source community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## Future Scope

* **File Search Integration:** Implement the `FileSearchTool` to enable analysis of local documents (PDFs, DOCX, TXT) such as annual reports (10-Ks) and earnings call transcripts.
* **Database Integration:** Connect to financial databases (e.g., Bloomberg, Refinitiv, Alpha Vantage) for structured financial data retrieval and analysis.
* **Improved Error Handling:** Enhance error handling mechanisms throughout the agent execution process for greater robustness.
* **User Feedback Loop:** Integrate a system for users to provide feedback on generated reports, allowing for continuous improvement of analysis quality.
* **Caching:** Implement caching strategies for search results and potentially agent responses to optimize performance and reduce resource consumption.
* **Streaming Enhancements:** Improve the streaming output of the report generation process for a more interactive and real-time user experience.
* **UI Development:** Develop a user-friendly web-based interface (e.g., using Streamlit, Flask, or Django) to facilitate easier interaction with the FinSearch Agent.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Code of Conduct

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) in all interactions within the project.

## Support

For any questions, issues, or suggestions, please open an issue on [GitHub](https://github.com/your-org/FinSearchAgent/issues).

## Contributing

We encourage open-source collaboration and welcome contributions. Please read our [Contributing Guidelines](CONTRIBUTING.md) to learn how you can get involved.

