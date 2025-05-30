from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.vectorstores.utils import filter_complex_metadata


class RAGChat:
    
    # vector_store = None
    # retriever = None
    # chain = None
    def __init__(self,llm_model:str="mistral"):
        self.model = ChatOllama(model=llm_model, temperature=0.7,  # Control randomness
                                                    top_p=0.7,       # Control diversity based on probability
                                                    top_k=50 )
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1024, chunk_overlap=100)
        # self.user_profile = user_profile
        self.prompt = PromptTemplate.from_template("""
        <s> [INST]
        You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful,
        unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
        \n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.
        If you don't know the answer to a question, please don't share false information.
        You must handle the user's query dynamically as per their requirements in efficient way to generate desired response with respect to user's query.
            
                                                   
                                                   

        [/INST] </s> 
        [INST] Question: {question} 
        Context: {context} 
        Answer: [/INST]
        """)

        self.vector_store = None
        self.retriever = None
        self.chain = None

    def ingest_data(self, pdf_file_path):
        docs = PyPDFLoader(file_path=pdf_file_path).load()
        print(f"PDF file loaded successfully {pdf_file_path}")
        chunks = self.text_splitter.split_documents(docs)
        chunks = filter_complex_metadata(chunks)

        #Load vector store
        vector_store = Chroma.from_documents(documents=chunks, embedding=FastEmbedEmbeddings(), persist_directory='chromadb')
        self.retriever = vector_store.as_retriever(
            search_type = "similarity_score_threshold",
            search_kwargs={
                "k": 3,
                "score_threshold": 0.5,
            },
        )

        self.chain = ({"context": self.retriever, "question": RunnablePassthrough()}
                      | self.prompt
                      | self.model
                      | StrOutputParser())
        

    def ask_query(self, query:str):
        if not self.chain:
            return "Please uplaod PDF file first"
        return self.chain.invoke(query)
    
    def clear(self):
        self.vector_store = None
        self.retriever = None
        self.chain = None

    # def generate_response(self, query):
    #     return f"This is the placeholder for query: '{query}' with following individual parameters {self.user_profile}"

# rag_bot = RAGChat()
# load_pdf = rag_bot.ingest_data('../data/transformer.pdf')
# query = rag_bot.ask_query("Can you explain me transformer architecture in layman terms?")
