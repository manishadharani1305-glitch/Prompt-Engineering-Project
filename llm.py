from transformers import pipeline

MODEL_NAME = "HuggingFaceTB/SmolLM2-360M-Instruct"

generator = pipeline(
    "text-generation",
    model=MODEL_NAME
)


def generate_answer(prompt, temperature=0.7, max_tokens=500):

    result = generator(
        prompt,
        max_new_tokens=max_tokens,
        temperature=temperature,
        do_sample=True,
        return_full_text=False
    )

    return result[0]["generated_text"]