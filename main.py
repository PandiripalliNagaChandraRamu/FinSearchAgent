import asyncio

from manager import FinancialResearchManager


# Entrypoint for the financial bot example.

async def main() -> None:
    query = input("Enter a financial research query: ")
    mgr = FinancialResearchManager()
    await mgr.run(query)

if __name__ == "__main__":
    asyncio.run(main())
