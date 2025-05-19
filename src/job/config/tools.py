from crewai_tools import FileReadTool, ScrapeWebsiteTool, MDXSearchTool, SerperDevTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_resume = FileReadTool(file_path="./files/resume.pdf")
semantic_search_resume = MDXSearchTool(mdx="./files/resume.pdf")
