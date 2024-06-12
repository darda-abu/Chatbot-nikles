from langchain_community.document_loaders import SeleniumURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
import argparse


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


def make_db(urls, pdf):
    url_db = load_urls(urls)
    db = url_db
    pdf_db = load_pdf(pdf)
    db.merge_from(pdf_db)
    db.save_local("Data/embedded_knowledge_base")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help = "Urls Path", default="Data/urls.txt")
    parser.add_argument("-p", "--pdf", help = "Pdf Path", default="Data/Warranty.pdf")
    args = parser.parse_args()

    make_db(args.url, args.pdf)
