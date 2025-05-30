# **Getting Started**
1. This RAG chatbot has been developed in local machine using ollama. So it needs to be download from following link. 
It is supporting for Linux, Windows and macOs

2. Install Ollama-[Visit Ollama's website to download and install](https://ollama.com/)




# 1.Pull required models from ollama
  Open terminal and pull required llm from ollama by hitting following command
  `ollama pull mistral`

# 2.Clone Repository
  `git clone https://github.com/BadrinathMJ/RAG_Chatbot.git`

# 3. Setup environment and Install necessary dependencies
  `python -m venv venv`
  `source venv/bin/activate`  # On Windows: .\venv\Scripts\activate
  * Install dependencies
  `pip install -r requirements.txt`

# 4. Running the Streamlit Application
   * Run the application by hitting following command
  `streamlit run app.py`

  * Here are some screentshots attached responses which got from chatbot as per settings of individual parameters like (such as tone, goal, personality traits, preferred style of answers, etc.)
  Query1:"Explain transformer architecture in a fun way for a 10 years old"
  Query2:"Explain transformer architecture in a fun way for a graduate student"

  * Following are screenshots of inferences received from chatbot

  ![setting1_10years]("screen_shots\setting1_10years.png")
  ![setting2_10years]("screen_shots\setting2_10years.png")
  ![setting3_graduate]("screen_shots\setting3_graduate.png")
  ![setting4_graduate]("screen_shots\setting4_graduate.png")


# 5. Hyperparameters:
The parameters can be tune to get the desired response from LLM

  **1. temperature:** This value (typically between 0.0 and 1.0) controls the randomness of the output. Higher values lead to more diverse and potentially creative responses, while lower values result in more focused and deterministic outputs. 

  **2. top_p(Nucleaus Sampling)**:This value (between 0.0 and 1.0) determines the cumulative probability threshold for tokens to be considered. A lower value reduces diversity, focusing on the most probable tokens, while a higher value increases diversity. 

  **3. top_k**:This value (a positive integer) specifies the number of top tokens to consider. A higher value allows for more diverse responses, while a lower value makes the responses more conservative. 


