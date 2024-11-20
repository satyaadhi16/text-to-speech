import cohere
import streamlit as st
import pyttsx3

# Ensure you have your Cohere API key
api_key = 'Mrh9BFF0YcKhl4jp5JC7ijKj0JwpQXdKFiz2aWm4'  # Replace this with your actual API key from Cohere
co = cohere.Client(api_key)

# Initialize the TTS engine
engine = pyttsx3.init()

# Set up Streamlit layout
st.title('Text-to-Speech and Cohere Integration')
st.write('Enter some text and let Cohere process it for you! Then listen to the output using TTS.')

# Streamlit input: Text box for user input
user_input = st.text_area("Type your text here:")

# Button for processing text with Cohere and converting it to speech
if st.button("Generate and Speak"):
    if user_input:
        try:
            # Step 1: Use Cohere to process the input (e.g., text generation or summarization)
            response = co.generate(
                model='xlarge',  # Use a valid model like 'xlarge' or any available model for your use
                prompt=user_input,
                max_tokens=100
            )

            generated_text = response.text.strip()

            # Step 2: Display the generated text in Streamlit
            st.subheader("Processed Text (from Cohere):")
            st.write(generated_text)

            # Step 3: Use pyttsx3 to convert generated text to speech
            engine.say(generated_text)
            engine.runAndWait()

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to process.")
