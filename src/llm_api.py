from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct"
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