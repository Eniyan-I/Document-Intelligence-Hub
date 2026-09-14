import tempfile
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser


st.title("Document Intelligence Hub")
st.write("Upload a PDF to extract insights and synthesize information via AI.")

@st.cache_resource
def process_pdf(user_file):
  with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
      tmp_file.write(user_file.getvalue())
      tmp_file_path = tmp_file.name
  loader=PyPDFLoader(tmp_file_path)
  doc=loader.load()
  text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
  document=text_splitter.split_documents(doc)
  embeddings=OllamaEmbeddings(model='nomic-embed-text')
  db=FAISS.from_documents(document,embeddings)
  return db.as_retriever()

user_file = st.file_uploader("Upload your PDF document", type=["pdf"])
if user_file is not None:
  retriver=process_pdf(user_file)
  
  prompt=ChatPromptTemplate.from_template(
    '''
    provide answers based on the given context
    <context>
    {context}
    <context>
    question:{question}
    '''
  )

  llm=OllamaLLM(model='llama3.2')

  def format_doc(docs):
    return '\n\n'.join(doc.page_content for doc in docs)
  rag_chain=(
    {'context':itemgetter('question') | retriver | format_doc,
    'question':itemgetter('question')}
    |prompt
    |llm
    |StrOutputParser()
  )

  user_input=st.text_input('Enter Your Question')
  
  if user_input:
    res=rag_chain.invoke({'question':user_input})
    st.write(res)