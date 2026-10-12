import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Email Generator",
    page_icon="✉️",
    layout="centered"
)

st.title("✉️ AI Professional Email Generator")
st.caption("Generate clear, tailored professional emails using local Ollama LLMs.")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Model Settings")
    model_name = st.text_input("Ollama Model", value="tinyllama:latest", help="Ensure this model is pulled locally via 'ollama pull <model>'")
    
    tone_options = [
        "Professional",
        "Formal",
        "Friendly & Warm",
        "Direct & Concise",
        "Persuasive",
        "Urgent",
        "Apologetic",
        "Custom"
    ]
    selected_tone = st.selectbox("Tone", tone_options)
    if selected_tone == "Custom":
        tone = st.text_input("Custom Tone", value="Constructive and Polite")
    else:
        tone = selected_tone

    st.markdown("---")
    st.markdown(
        """
        **Prerequisites:**
        1. [Install Ollama](https://ollama.com)
        2. Run Ollama service (`ollama serve`)
        3. Pull model: `ollama run tinyllama`
        """
    )

# Email Input Form
with st.form("email_form"):
    recipient = st.text_input(
        "Recipient",
        placeholder="e.g., Hiring Manager, Dr. Smith, Project Team",
        help="Who is this email addressed to?"
    )
    
    purpose = st.text_input(
        "Purpose",
        placeholder="e.g., Requesting a project status update, Follow-up on interview",
        help="What is the primary goal of this email?"
    )
    
    points = st.text_area(
        "Important Points / Key Details",
        placeholder="e.g.:\n- Completed phase 1 deliverables\n- Awaiting budget sign-off for phase 2\n- Need feedback by Thursday at 5 PM",
        height=140,
        help="List key facts or points that must be included."
    )
    
    submit_btn = st.form_submit_button("✨ Generate Email", use_container_width=True)

if submit_btn:
    if not recipient.strip():
        st.warning("⚠️ Please provide a recipient.")
    elif not purpose.strip():
        st.warning("⚠️ Please specify the purpose of the email.")
    elif not points.strip():
        st.warning("⚠️ Please provide the key points to include.")
    else:
        prompt = f"""Write a professional email.

Recipient:
{recipient}

Purpose:
{purpose}

Tone:
{tone}

Important points:
{points}

Requirements:
- Write a clear subject line.
- Keep sentences reasonably short.
- Be polite and professional.
- Do not invent information.
- Include a clear closing.
"""

        with st.spinner(f"Generating email using '{model_name}'..."):
            try:
                response = ollama.chat(
                    model=model_name,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a professional email writing assistant."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
                
                email_content = response.get("message", {}).get("content", "")
                
                if email_content:
                    st.success("✅ Email generated successfully!")
                    st.subheader("Generated Email")
                    st.text_area("Email Output", value=email_content, height=300)
                    
                    st.download_button(
                        label="📥 Download Email (.txt)",
                        data=email_content,
                        file_name="generated_email.txt",
                        mime="text/plain"
                    )
                else:
                    st.error("No content received from the model.")
            except Exception as e:
                st.error(f"Failed to communicate with Ollama: {str(e)}")
                st.info(
                    "💡 **Troubleshooting Tip:** Make sure Ollama is installed and running on your system, "
                    f"and that you have pulled the `{model_name}` model by running `ollama run {model_name}`."
                )
