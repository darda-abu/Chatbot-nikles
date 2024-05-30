from langchain_community.document_loaders import SeleniumURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
from langchain_community.llms import Ollama
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_community.document_loaders import DataFrameLoader
from langchain_community.document_loaders import PyPDFLoader
import mysql.connector
import pandas as pd

def get_urls(file):
        f = open(file,'r').read()
        return f.split('\n')

def split_embed_save(loader):
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits = text_splitter.split_documents(docs)
    db = FAISS.from_documents(all_splits, OpenAIEmbeddings())
    return db

def load_urls(file):
    urls = get_urls(file)
    loader = SeleniumURLLoader(urls=urls)
    return split_embed_save(loader)

def load_pdf(file):
    loader=PyPDFLoader(file)
    return split_embed_save(loader)

def load_db(host, user, password, database, table):
    # conn = mysql.connector.connect(
    #     host='127.0.0.1',
    #     user='root',
    #     password='',
    #     database='products'
    # )
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    query = f"SELECT name, description, url, image_url, category_names, category_label, tag_names FROM {table}"  
    df = pd.read_sql(query, conn)
    conn.close()
    loader = DataFrameLoader(df, page_content_column="name")
    return split_embed_save(loader)



# def load_db(file):

def make_db(urls, pdf):
    db = load_db('127.0.0.1', 'root', '', 'products', 'cb_products')
    url_db = load_urls(urls)
    pdf_db = load_pdf(pdf)
    db.merge_from(url_db)
    db.merge_from(pdf_db)
    db.save_local("embedded_knowledge_base")

if __name__ == "__main__":
    make_db("Data/urls.txt", "Data/Warranty.pdf")
