from transformers import pipeline, AutoTokenizer

model_id = "microsoft/Phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)

generator = pipeline(
    "text-generation",
    model=model_id,
    tokenizer=tokenizer,
    device_map="auto"
)

def ask_llm(context, question):

    messages = [
        {
            "role": "system",
            "content": (
                "Você é um sistema RAG.\n"
                "Responda SOMENTE usando o contexto fornecido.\n"
                "NÃO invente informações.\n"
                "NÃO faça interpretações psicológicas.\n"
                "Responda em português.\n"
                "Use no máximo 5 tópicos.\n"
                "Cada tópico deve possuir apenas 1 frase curta.\n"
                "Se não houver informação suficiente, responda exatamente:\n"
                "'Não encontrei informação suficiente nos textos.'"
            )
        },
        {
            "role": "user",
            "content": f"""
Contexto:
{context}

Pergunta:
{question}

Responda de forma objetiva e curta.
"""
        }
    ]

    # Template correto para Phi-3
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    response = generator(
        prompt,
        max_new_tokens=120,
        do_sample=True,
        temperature=0.3,
        top_p=0.85,
        repetition_penalty=1.15,
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
        return_full_text=False
    )

    return response[0]["generated_text"].strip()