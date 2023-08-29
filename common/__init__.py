import pickle

def load_model(model_filename):
    with open(model_filename, "rb") as f:
        model = pickle.load(f)
    return model