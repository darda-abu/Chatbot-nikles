from langchain_community.document_loaders import SeleniumURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DataFrameLoader
from langchain_community.document_loaders import PyPDFLoader
import mysql.connector
import pandas as pd
import argparse
# from models import database

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


def make_db(urls, pdf):
    # db = load_db(db_creds.host, db_creds.user, db_creds.password, db_creds.database, db_creds.table)
    # url_db = load_urls(urls)
    # pdf_db = load_pdf(pdf)
    # db.merge_from(url_db)
    # db.merge_from(pdf_db)
    # db.save_local("Data/embedded_knowledge_base")
    # pkl = db.serialize_to_bytes()
    # pkl.save("Data/knoiwledge_base_serials.pkl")

    url_db = load_urls(urls)
    db = url_db
    pdf_db = load_pdf(pdf)
    db.merge_from(pdf_db)
    db.save_local("Data/embedded_knowledge_base")
    # pkl = db.serialize_to_bytes()
    # pkl.save("Data/knowledge_base_serials")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help = "Urls Path", default="Data/urls.txt")
    parser.add_argument("-p", "--pdf", help = "Pdf Path", default="Data/Warranty.pdf")
    # parser.add_argument("-ht", "--host", help = "Host", default="127.0.0.1")
    # parser.add_argument("-n", "--user", help = "User", default="root")
    # parser.add_argument("-ps", "--password", help = "Password", default="")
    # parser.add_argument("-d", "--database", help = "Database", default="products")
    # parser.add_argument("-t", "--table", help = "Table", default="cb_products")
    args = parser.parse_args()
    # db_creds = database(args.host, args.user, args.password, args.database, args.table)
    url_path ="Data/urls.txt" 
    pdf_path = "Data/Warranty.pdf"
    if args.url: url_path = args.url
    if args.pdf: pdf_path = args.pdf
    make_db(url_path, pdf_path)
