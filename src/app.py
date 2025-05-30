import os
import tempfile
import streamlit as st
from streamlit_chat import message
from chat_pdf import RAGChat

# import os
# import tempfile
# import streamlit as st
# from streamlit_chat import message
# from chat_pdf import RAGChat

# st.set_page_config(page_title="ChatPDF")


# def display_messages():
#     st.subheader("Chat")
#     for i, (msg, is_user) in enumerate(st.session_state["messages"]):
#         message(msg, is_user=is_user, key=str(i))
#     st.session_state["thinking_spinner"] = st.empty()


# def process_input():
#     if st.session_state["user_input"] and len(st.session_state["user_input"].strip()) > 0:
#         user_text = st.session_state["user_input"].strip()
#         with st.session_state["thinking_spinner"], st.spinner(f"Thinking"):
#             agent_text = st.session_state["assistant"].ask_query(user_text)

#         st.session_state["messages"].append((user_text, True))
#         st.session_state["messages"].append((agent_text, False))


# def read_and_save_file():
#     st.session_state["assistant"].clear()
#     st.session_state["messages"] = []
#     st.session_state["user_input"] = ""

#     for file in st.session_state["file_uploader"]:
#         with tempfile.NamedTemporaryFile(delete=False) as tf:
#             tf.write(file.getbuffer())
#             file_path = tf.name

#         with st.session_state["ingestion_spinner"], st.spinner(f"Ingesting {file.name}"):
#             st.session_state["assistant"].ingest_data(file_path)
#         os.remove(file_path)


# def page():
#     if len(st.session_state) == 0:
#         st.session_state["messages"] = []
#         st.session_state["assistant"] = RAGChat()

#     st.header("ChatPDF")

#     st.subheader("Upload a document")
#     st.file_uploader(
#         "Upload document",
#         type=["pdf"],
#         key="file_uploader",
#         on_change=read_and_save_file,
#         label_visibility="collapsed",
#         accept_multiple_files=True,
#     )

#     st.session_state["ingestion_spinner"] = st.empty()

#     display_messages()
#     st.text_input("Message", key="user_input", on_change=process_input)


# if __name__ == "__main__":
#     page()

def set_individual_parameters():
    #Set Individual Parameters
    #Define user parameters in terms of their profiles
    tone_parameters = ["Friendly", "Formal", "Casual", "Professional"]
    goal_parameters = ["Informational", "Transactional", "Advisory"]
    personality_parameters = ["Empathetic", "Humorous", "Serious"]
    answer_style_parameters = ["Concise", "Detailed", "Step-by-Step"]
    st.set_page_config(page_title="Personalized ChatBot")

    st.write("Set your preferences for chatbot")
    tone = st.selectbox("Select Tone", tone_parameters)
    goal = st.selectbox("Select Goal", goal_parameters)
    personality = st.selectbox("Select Personality", personality_parameters)
    answer_style = st.selectbox("Select Answer Style", answer_style_parameters)

    #Start the chatbot with used preference in terms of individual parameters
    user_profile = {
        "tone":tone,
        "goal": goal,
        "personality": personality,
        "answer_style": answer_style
    }

    st.write("Personalized Chatbot is ready! You can start asking questions.")

    #User input for the chatbot
    user_input = st.text_input("You: ","")
    
    return user_input

def display_messages():
    # for message in st.session_state["messages"]:
    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])
    st.subheader("Chat")
    for i, (msg, is_user) in enumerate(st.session_state["messages"]):
        message(msg, is_user=is_user, key=str(i))
    st.session_state["thinking_spinner"] = st.empty()


def process_input():
    

    if st.session_state["user_input"] and len(st.session_state["user_input"].strip()) > 0:
        user_text = st.session_state['user_input'].strip() 
        print(user_text)
        with st.session_state["thinking_spinner"], st.spinner(f"Thinking"):
            agent_text = st.session_state["assistant"].ask_query(user_text)

        st.session_state["messages"].append((user_text, True))
        st.session_state["messages"].append((agent_text, True))

def read_and_save_file():
    st.session_state["assistant"].clear()
    st.session_state["messages"] = []
    st.session_state["user_input"] = ""

    for file in st.session_state["file_uploader"]:
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(file.getbuffer())
            file_path = tf.name

        with st.session_state["ingestion_spinner"], st.spinner(f"Ingesting {file.name}"):
            st.session_state["assistant"].ingest_data(file_path)
        os.remove(file_path)


def page():
    # Define the user profile parameters
    tone_options = ["Friendly", "Formal", "Casual", "Professional"]
    goal_options = ["Informational", "Transactional", "Advisory"]
    personality_options = ["Empathetic", "Humorous", "Serious"]
    answer_style_options = ["Concise", "Detailed", "Step-by-Step"]
    
    if len(st.session_state) == 0:
        st.session_state["messages"] = []
        st.session_state["assistant"] = RAGChat()
    if "user_profile" not in st.session_state:
        st.session_state["user_profile"] = {
            "tone": tone_options[0],
            "goal": goal_options[0],
            "personality": personality_options[0],
            "answer_style": answer_style_options[0],
            
        }

    st.header("Personalized Chatbot")

    # User interface for setting preferences in the sidebar
    st.sidebar.title("Set your preferences")
    tone = st.sidebar.selectbox(
        "Select Tone",
        tone_options,
        index=tone_options.index(st.session_state["user_profile"]["tone"])
    )
    goal = st.sidebar.selectbox(
        "Select Goal",
        goal_options,
        index=goal_options.index(st.session_state["user_profile"]["goal"])
    )
    personality = st.sidebar.selectbox(
        "Select Personality",
        personality_options,
        index=personality_options.index(st.session_state["user_profile"]["personality"])
    )
    answer_style = st.sidebar.selectbox(
        "Select Answer Style",
        answer_style_options,
        index=answer_style_options.index(st.session_state["user_profile"]["answer_style"])
    )
    
  
    # Update user profile in session state
    st.session_state["user_profile"] = {
        "tone": tone,
        "goal": goal,
        "personality": personality,
        "answer_style": answer_style,
        
    }
    st.header("ChatPDF")

    st.subheader("Upload a document")
    st.file_uploader(
        "Choose files",
        type=['pdf', 'docx', 'txt','xlsx', 'csv'],
        key="file_uploader",
        on_change=read_and_save_file,
        label_visibility="collapsed",
        accept_multiple_files=True,
    )

    st.session_state["ingestion_spinner"] = st.empty()
    # Display the chat messages
    display_messages()
    
    # User input for the chatbot
    st.text_input("Message", key="user_input", on_change=process_input)

    
if __name__ == "__main__":
    page()