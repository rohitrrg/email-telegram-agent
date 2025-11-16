from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
from hf_llm import llm
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

prompt = PromptTemplate(
    input_variables=["subject", "body"],
    template="""
Summarize the following email into **clear bullet points** (2–5 points maximum).  
Each point should be short, concise and informative — no repetition of this instruction.

Format the output as:
• Point 1

• Point 2

...

Subject: {subject}
Body: {body}

Bullet-point summary:
"""
)

chain = prompt | llm | parser

def summarize_email(body, subject):
    result = chain.invoke({"subject": subject, "body": body})
    summary = result

    # If the model echoed the word "Summary:" again, cut it off
    if "Summary:" in summary:
        summary = summary.split("Summary:")[-1].strip()

    return summary