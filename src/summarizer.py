from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from hf_llm import llm

prompt = PromptTemplate(
    input_variables=["subject", "body"],
    template="""
Summarize the following email into 1–2 sentences. 
Do not repeat the instructions, only return the summary text.

Subject: {subject}
Body: {body}

Summary:
"""
)

chain = LLMChain(llm=llm, prompt=prompt)

def summarize_email(body, subject):
    result = chain.invoke({"subject": subject, "body": body})
    summary = result.get("text", "").strip()

    # If the model echoed the word "Summary:" again, cut it off
    if "Summary:" in summary:
        summary = summary.split("Summary:")[-1].strip()

    return summary
