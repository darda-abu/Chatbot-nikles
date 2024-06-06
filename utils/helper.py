import pickle
import os

def load_chat_history(ssid=1, directory="chat_histories"):
    filename = f"Data/{directory}/{ssid}.pkl"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if not os.path.exists(filename):
        with open(filename, 'wb') as f:
            pickle.dump([], f)
        return []
    with open(filename, "rb") as f:
        chat_history = pickle.load(f)
    return chat_history

def dump_chat_history(chat_history, ssid=1, directory="chat_histories"):
    with open(f"Data/{directory}/{ssid}.pkl", "wb") as f:
        pickle.dump(chat_history, f)

def flush_chat_history(ssid = 1, directory="chat_histories"):
    filename = f"Data/{directory}/{ssid}.pkl"
    if os.path.exists(filename):
        os.remove(filename)
