from langchain_community.document_loaders import SeleniumURLLoader


def get_urls(file):
    f = open(file,'r').read()
    return f.split('\n')

# print(get_urls("Data\\url_loader\\urls.txt"))


    