# Conversational Chatbot
![image](https://github.com/darda-abu/Chatbot-nikles/assets/167751588/7b8ec20d-da54-48bf-9b1e-a6ede5d97efb)


## Requirements
### Knowledge source:
1. SQL file [products.sql](Data\products.sql)
2. Website data (Scrape using python code.) 

    Web pages to scrape:
	
    - https://www.nikles.com/about/ (Nikles in short, History, Philosophy)

	- https://www.nikles.com/technologies/ (technology names and details)

	- https://www.nikles.com/nikles-luxury-finishes/ (all main parts of the page)

	- https://www.nikles.com/news/ (news title and details)
3. PDF data [Warranty.pdf](Data\Warranty.pdf)


### Tasks
1. Gather all the data from different sources.
2. Create a knowledge base using any vector database
3. Use OpenAI/Langchain/Llama index for creating the chatbot
4. Use FAST API for the backend.
5. Use Streamlit for the frontend.


### Non functional requirements
1. There shuold be different chains for documents and database queries.
2. Chatbot Has to be conversational. 
## Overview

Welcome to the Conversational Chatbot project! This repository contains the code and resources needed to deploy a fully functional chatbot application. The project is split into two main components: a backend server and a frontend interface.
 

## Architecture
![Untitled Diagram drawio (2)](https://github.com/darda-abu/Chatbot-nikles/assets/167751588/9b1d4f2e-a1a0-47ff-8213-e33d5b0a849c)

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. This project also requires several Python packages, which are listed in the [requirements.txt](requirements.txt) file.

### Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Running the Application

### Backend
To start the backend server, execute the following command:
```bash
uvicorn app.main:app --reload
```
## Frontend
Ensure the backend server is running before starting the frontend. Then, run:
```bash
streamlit run frontend/app.py
```
## Updating the Database/URLs/Warranty Information
To update the database, URLs, or warranty information, use the following command:
```bash
python Data/loader.py
```
The [loader.py](Data/loader.py) script accepts several arguments to specify paths and credentials. The following table outlines the default values for these arguments:

| Argument | Flag | Description | Default Value |
|----------|------|-------------|---------------|
| `--url` | `-u` | Urls Path | `Data/urls.txt` |
| `--pdf` | `-p` | Pdf Path | `Data/Warranty.pdf` |


# Schema for `cb_products` Table

In order to load the `products` database it has to contain these columns.

- **name**
- **description**
- **url**
- **image_url**
- **category_names**
- **category_label**
- **tag_names**

