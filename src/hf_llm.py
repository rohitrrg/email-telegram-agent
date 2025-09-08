# from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
# import os

# HF_TOKEN = os.getenv("HF_TOKEN")
# MODEL = "HuggingFaceH4/zephyr-7b-beta"

# llm_endpoint = HuggingFaceEndpoint(
#     repo_id=MODEL,
#     huggingfacehub_api_token=HF_TOKEN,
#     task="conversational",
#     temperature=0.3,
#     max_new_tokens=128,
# )

# llm = ChatHuggingFace(llm=llm_endpoint)


from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from langchain_huggingface import HuggingFacePipeline
import torch
import os

MODEL_PATH = "Mistral-7B-Instruct-v0.3"  # adjust to your folder

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
bnb = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=True,
                bnb_4bit_compute_dtype=torch.float16,
            )
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    device_map="auto",      # uses GPU if available
    torch_dtype="auto",
    quantization_config=bnb,
    low_cpu_mem_usage=True,
    offload_folder=os.environ.get("HF_HOME", "/tmp/offload"),
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128,
    temperature=0.3,
)

llm = HuggingFacePipeline(pipeline=pipe)
