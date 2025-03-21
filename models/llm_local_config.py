
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# Load Mistral 7B model (quantized version recommended for local)
def load_local_mistral():
    model_name = "mistralai/Mistral-7B-Instruct-v0.1"  # Replace with local path if downloaded

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16
    )

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )

    return pipe

# Generate response from local model
def query_local_llm(prompt):
    pipe = load_local_mistral()
    result = pipe(prompt)[0]["generated_text"]
    return result
