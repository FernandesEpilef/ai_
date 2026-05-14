from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct"
)
# outro modelo: TinyLlama/TinyLlama-1.1B-Chat-v1.0
def ask_llm(context, question):

    prompt = f"""
<|system|>
Você é um assistente de perguntas e respostas.
Responda em português.
Use somente o contexto fornecido.
Se a resposta não estiver no contexto, diga: "Não encontrei essa informação no texto."
Não repita a pergunta.
Não invente informações.
</s>

<|user|>
Contexto:
{context}

Pergunta:
{question}

Responda com base apenas nas frases do contexto.
</s>

<|assistant|>
"""

    response = generator(
        prompt,
        max_new_tokens=150,
        do_sample=False,
        temperature=0.5,
        top_p=0.85,
        repetition_penalty=1.2,
        return_full_text=False
    )

    return response[0]["generated_text"].strip()