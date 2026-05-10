from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

def ask_llm(context, question):
    prompt = f"""
Responda em português usando apenas o contexto.

Contexto:
{context}

Pergunta:
{question}

Resposta:
"""

    result = generator(
        prompt,
        max_new_tokens=120,
        do_sample=False
    )

    return result[0]["generated_text"].strip()