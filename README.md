# Financial Research Agent Example

This example demonstrates how to build a sophisticated financial research agent using a multi-agent system approach. It takes a user query, performs research, analyzes findings, and generates a structured report.

## How it Works

The system orchestrates several specialized agents in a sequence:

1.  **Planning**: The `FinancialPlannerAgent` analyzes the user's request and generates a list of relevant search terms (e.g., recent news, earnings calls, corporate filings, industry commentary).
2.  **Information Gathering**: The `FinancialSearchAgent` uses a `WebSearchTool` (and potentially `FileSearchTool` for local documents like PDFs or 10-Ks) to retrieve concise summaries for each search term.
3.  **Sub-Analysis**: Specialist agents, like `FundamentalsAnalystAgent` and `RiskAnalystAgent`, are exposed as tools. The writer agent can invoke these to get focused analysis on specific aspects (e.g., financial health, potential risks).
4.  **Report Generation**: The `FinancialWriterAgent` acts as a senior analyst. It synthesizes the search results and any sub-analysis summaries into a comprehensive, long-form markdown report, including an executive summary and suggested follow-up questions.
5.  **Verification**: Finally, the `VerificationAgent` audits the generated report for internal consistency, clear sourcing, and unsupported claims, flagging potential issues.

## Running the Example

To run the financial research agent:

1.  **Setup Environment**: Ensure you have Python installed and the necessary dependencies (likely listed in a `requirements.txt` file, though not explicitly shown). It's recommended to use a virtual environment.

2.  **Activate Virtual Environment** (if you are using one):
    *   On Windows PowerShell:
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    *(Replace `.venv` with your virtual environment's directory name if different)*

3.  **Run the Main Script**: Navigate to the project's root directory (`FinSearch Agent`) in your terminal and run:

    ```bash
    python main.py
    ```

4.  **Enter Query**: When prompted, enter a financial research query, for example:

    ```
    Write up an analysis of Apple Inc.'s most recent quarter.
    ```

## Agent Details & Prompts

### Writer Agent Prompt Example

You can ask various types of financial research questions:

### 1. Company Analysis Queries
Focus on analyzing specific companies for investment purposes.
*   *"Provide a detailed financial analysis of Tesla, including recent performance and future outlook."*
*   *"Analyze Apple's competitive position against other tech giants and assess its long-term growth potential."*

### 2. Industry/Sector Analysis Queries
Examine trends, challenges, and opportunities in specific industries.
*   *"Give me a comprehensive overview of the renewable energy sector, focusing on growth trends and major players."*
*   *"Research the pharmaceutical industry's current challenges and identify emerging growth areas."*

### 3. Investment Strategy Queries
Help with making investment decisions or developing strategies.
*   *"What are the best dividend stocks to invest in during high inflation periods?"*
*   *"Analyze the potential impact of rising interest rates on tech growth stocks and recommend an investment strategy."*

### 4. Market Trend Analysis Queries
Focus on broad market trends and economic factors.
*   *"Assess the current state of the global semiconductor market and forecast trends for the next 18 months."*
*   *"Analyze how ESG investing trends are reshaping investment patterns in traditional energy companies."*

### 5. Risk Assessment Queries
Evaluate potential risks in investments or economic developments.
*   *"What are the main geopolitical risks affecting international technology supply chains?"*
*   *"Evaluate the regulatory risks facing major fintech companies in the next 2-3 years."*

### 6. Economic Impact Analysis Queries
Analyze how economic events impact financial markets or specific investments.
*   *"How will ongoing inflation impact consumer discretionary stocks in the next quarter?"*
*   *"Analyze the potential effects of the Federal Reserve's policy changes on emerging market investments."*

### 7. Comparison Queries
Compare multiple companies, sectors, or investment options.
*   *"Compare the financial health and growth prospects of the top three cloud computing providers."*
*   *"Analyze and compare the risk-return profiles of major cryptocurrency investments versus traditional gold."*