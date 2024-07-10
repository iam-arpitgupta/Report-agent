from crewai import Task
from tools import tool
from agents import news_researcher,news_writer
#research Task
research_task=Task(
    description=(
        "identify the next big trend in {topic}"
        "focus on identifying the pros and cons and narrative"
        "your final report should clearly articulate the key points"
        "its market opportunities and potential risk"
    ),
    expected_output='A comphrensive 3 paragraph report addressing the lastest AI trends',
    tools=[tool],
    agent=news_researcher,
)

#writing tasl with language model configration
write_task=Task(
    description=(
        "Compose an insightful article on {topic}"
        "focus on lastest trends and hpw to optimize them"
        "the article should be easy to understand"
    ),
    expected_output='A 4 paragraph  article on {topic] advancement formatted as markdown',
    tools=[tool],
    agent=news_writer,
    async_execution=Fasle,
    output_file='new-blog-post.md'
)
