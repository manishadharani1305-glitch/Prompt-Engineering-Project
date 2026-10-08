import streamlit as st

from llm import generate_answer

from prompt_templates import (
    zero_shot_prompt,
    one_shot_prompt,
    few_shot_prompt,
    cot_prompt,
    manual_cot_prompt,
    tot_prompt
)


st.set_page_config(
    page_title="Prompt Engineering App",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.header("⚙️ LLM Settings")

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    max_tokens = st.slider(
        "Max Tokens",
        min_value=50,
        max_value=1000,
        value=500,
        step=50
    )


# -----------------------------
# MAIN TITLE
# -----------------------------

st.title("🤖 Prompt Engineering App")

st.write(
    "Explore different prompting techniques using an LLM."
)


# -----------------------------
# PROMPT TECHNIQUE
# -----------------------------

st.subheader("🎯 Select Prompting Technique")

technique = st.selectbox(
    "Choose a prompting technique:",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)


# -----------------------------
# TASK INPUT
# -----------------------------

st.subheader("📝 Enter Your Task")

task = st.text_area(
    "Enter your question or task:",
    placeholder="Example: Explain Artificial Intelligence.",
    height=150
)


# -----------------------------
# PROMPT MAPPING
# -----------------------------

prompt_functions = {
    "Zero-shot": zero_shot_prompt,
    "One-shot": one_shot_prompt,
    "Few-shot": few_shot_prompt,
    "CoT": cot_prompt,
    "Manual CoT": manual_cot_prompt,
    "ToT": tot_prompt
}


# -----------------------------
# GENERATE ANSWER
# -----------------------------

if st.button("🚀 Generate Answer", type="primary"):

    if not task.strip():

        st.warning("Please enter a task first.")

    else:

        prompt = prompt_functions[technique](task)

        st.subheader("✨ Generated Answer")

        with st.spinner("Generating answer..."):

            try:

                answer = generate_answer(
                    prompt,
                    temperature,
                    max_tokens
                )

                st.write(answer)

            except Exception as e:

                st.error(
                    f"Unable to generate response: {str(e)}"
                )


# -----------------------------
# INFORMATION
# -----------------------------

st.divider()

st.subheader("📌 How It Works")

st.write(
    "Enter a task, select a prompting technique, "
    "and generate a response using the LLM. "
    "You can change the temperature and maximum tokens "
    "to observe how they affect the generated response."
)