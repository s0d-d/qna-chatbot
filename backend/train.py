"""Dependencies that need to be installed:
pip install pypdf
pip install python-dotenv
pip install -q transformers einops accelerate langchain bitsandbytes
pip install -q transformers einops accelerate langchain bitsandbytes
pip install llama-index
pip install llama-index-llms-huggingface
pip install llama-index-embeddings-langchain
pip install sentence-transformers
"""

import logging
import sys
import torch
import os

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.prompts.prompts import SimpleInputPrompt
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index.core.service_context import ServiceContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from huggingface_hub import login

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

access_token_read = "hf_123"
login(token = access_token_read)

script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the data folder
data_folder = os.path.join(script_dir, "data")
documents = SimpleDirectoryReader(data_folder).load_data()

system_prompt = "You are a Q&A assistant. Your goal is to answer questions as accurately as possible based on the instructions and context provided."

query_wrapper_prompt = SimpleInputPrompt("{query_str}")

llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.0, "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="meta-llama/Llama-2-7b-chat-hf",
    model_name="meta-llama/Llama-2-7b-chat-hf",
    device_map="auto",
    model_kwargs={"torch_dtype": torch.float16} #, "load_in_8bit": True
)

embed_model = LangchainEmbedding(
  HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
)

service_context = ServiceContext.from_defaults(
    chunk_size=1024,
    llm=llm,
    embed_model=embed_model
)

index = VectorStoreIndex.from_documents(documents, service_context=service_context)
query_engine = index.as_query_engine()

response = query_engine.query("What international study opportunities are there for students?")
print(response)
