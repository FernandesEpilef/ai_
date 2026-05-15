from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Ajuste este bloco para testar outros modelos ou temperaturas.
MODEL_ID = "microsoft/Phi-3-mini-4k-instruct"
TEMPERATURE = 0.3

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

device = "cuda" if torch.cuda.is_available() else "cpu"

model_kwargs = {}
if device == "cuda":
    model_kwargs["torch_dtype"] = torch.float16
    print("[INFO] GPU detectada. Forçando o modelo para a Placa de Vídeo.")
else:
    model_kwargs["torch_dtype"] = torch.float32
    print("[WARNING] GPU não detectada. Usando CPU (mais lento).")

model = AutoModelForCausalLM.from_pretrained(MODEL_ID, **model_kwargs).to(device)
model.eval()

"""""
def _model_device():
    try:
        return next(model.parameters()).device
    except StopIteration:
        return torch.device("cpu")
""" 
def ask_llm(context, question, history=None):
    history_text = ""
    if history:
        history_lines = []
        for turn in history:
            history_lines.append(
                f"Pergunta: {turn['question']}\nResposta: {turn['answer']}"
            )
        history_text = "\n\nHistórico de conversa:\n" + "\n\n".join(history_lines)

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
            "content": (
                f"Contexto:\n{context}\n\n"
                f"{history_text}\n\n"
                "Pergunta:\n"
                f"{question}\n\n"
                "Responda de forma objetiva e curta."
            )
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = inputs.to(device)

    try:
        output_ids = model.generate(
            **inputs,
            max_new_tokens=120,
            temperature=TEMPERATURE,
            do_sample=True,
            top_p=0.85,
            repetition_penalty=1.15,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id,
            use_cache=True
        )

        generated_ids = output_ids[0][inputs["input_ids"].shape[1]:]
        text = tokenizer.decode(
            generated_ids,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False
        )

        return text.strip()

    except Exception as exc:
        return f"Erro na geração de resposta: {exc}"
