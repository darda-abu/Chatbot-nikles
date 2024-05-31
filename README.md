# Conversational Chatbot
![image](https://github.com/darda-abu/Chatbot-nikles/assets/167751588/7b8ec20d-da54-48bf-9b1e-a6ede5d97efb)
## To run the backend
```bash
uvicorn app.main:app --reload
```
## To run the frontend
Make sure backend is running
```bash
streamlit run frontend/app.py
```
## To update database/ urls/ warranty
```bash
python Data/loader.py
```
The following table outlines the default values for the arguments specified in the code:

| Argument | Flag | Description | Default Value |
|----------|------|-------------|---------------|
| `--url` | `-u` | Urls Path | `Data/urls.txt` |
| `--pdf` | `-p` | Pdf Path | `Data/Warranty.pdf` |
| `--host` | `-ht` | Host | `127.0.0.1` |
| `--user` | `-n` | User | `root` |
| `--password` | `-ps` | Password | `""` (empty) |
| `--database` | `-d` | Database | `products` |
| `--table` | `-t` | Table | `cb_products` |

# Schema for `cb_products` Table

In order to load the `products` database it has to contain these columns.

- **name**
- **description**
- **url**
- **image_url**
- **category_names**
- **category_label**
- **tag_names**


