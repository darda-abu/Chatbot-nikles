# Chatbot-nikles
To update data
```bash
python Data/loader.py
```
default values are 
he following table outlines the default values for the arguments specified in the code:

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


