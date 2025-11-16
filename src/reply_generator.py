from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
from hf_llm import llm
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

prompt = PromptTemplate(
    input_variables=["context", "shorthand"],
    template="""
You are Rohit, replying to an email you have received. 
Your goal is to expand Rohit’s shorthand message into a short, professional, and natural-sounding reply.

Guidelines:
- Do NOT repeat or paraphrase the sender’s original email content.
- Use proper line spacing if required.
- Keep it concise (2–4 sentences maximum).
- Maintain a polite and professional tone.
- Address the sender directly by name if available.
- Add a simple closing like “Best regards, Rohit”.
- The reply should sound human, not AI-generated.

Original email (for context only, do not restate or quote):
{context}

Rohit's shorthand reply:
{shorthand}

Now write Rohit’s final reply email:
"""
)

# chain = LLMChain(llm=llm, prompt=prompt)
chain = prompt | llm | parser

def generate_reply(context, shorthand):
    result = chain.invoke({"context": context, "shorthand": shorthand})
    reply = result#.get("text", "").strip()

    # Clean up if model echoes the header
    if "Now write Rohit’s final reply email:" in reply:
        reply = reply.split("Now write Rohit’s final reply email:")[-1].strip()
    if "Final professional reply:" in reply:
        reply = reply.split("Final professional reply:")[-1].strip()

    return reply
