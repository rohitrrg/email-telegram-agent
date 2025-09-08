from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from hf_llm import llm

prompt = PromptTemplate(
    input_variables=["context", "shorthand"],
    template="""
You are an AI email assistant. 
The user gives very short shorthand replies (e.g., "yes confirm", "send tomorrow", "not attending"). 
Your job is to convert the shorthand into a short, polite, professional email reply.

Rules:
- Do NOT repeat the original email context in detail.
- Keep it concise (1–2 sentences max).
- Address the sender politely.
- Expand shorthand into a clear response.

Email context:
{context}

User shorthand reply:
{shorthand}

Final professional reply:
"""
)

chain = LLMChain(llm=llm, prompt=prompt)

def generate_reply(context, shorthand):
    result = chain.invoke({"context": context, "shorthand": shorthand})
    # Extract only the model's reply text
    reply = result.get("text", "").strip()

    # Sometimes models echo the instruction; cut that off
    if "Final professional reply:" in reply:
        reply = reply.split("Final professional reply:")[-1].strip()

    return reply
