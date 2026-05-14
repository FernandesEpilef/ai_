from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct"
)
# outro modelo: TinyLlama/TinyLlama-1.1B-Chat-v1.0
def ask_llm(context, question):

    prompt = f"""
<|system|>
Você é um sistema RAG.

REGRAS IMPORTANTES:
- Responda em português.
- Responda SOMENTE usando o contexto.
- NÃO invente conceitos.
- NÃO faça interpretações psicológicas profundas.
- NÃO use termos genéricos como:
  "diferenças individuais",
  "aspectos sociais",
  "dinâmicas humanas".
- Seja direto.
- Responda em no máximo 5 tópicos.
- Cada tópico deve ter no máximo 1 frase curta.
- Se não houver informação suficiente, diga:
"Não encontrei informação suficiente nos textos."
</s>

<|user|>
Contexto:
{context}

Pergunta:
{question}

Liste a resposta de forma clara e objetiva e em no máximo 5 tópicos.
</s>

<|assistant|>
"""

    response = generator(
        prompt,
        max_new_tokens=300,
        do_sample=False,
        temperature=0.2,
        top_p=0.85,
        repetition_penalty=1.3,
        return_full_text=False
    )

    return response[0]["generated_text"].strip()