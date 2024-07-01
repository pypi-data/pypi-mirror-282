import os

import mammoth
from catalogue.dataset_loaders.autocsv import data_csv
from catalogue.model_loaders.onnx import model_onnx
from catalogue.metrics.model_card import model_card


def test_bias_exploration():
    with mammoth.testing.Env(data_csv, model_onnx, model_card) as env:
        numeric = ["age", "duration", "campaign", "pdays", "previous"]
        categorical = [
            "job",
            "marital",
            "education",
            "default",
            "housing",
            "loan",
            "contact",
            "poutcome",
        ]
        sensitive = ["marital"]
        dataset_uri = (
            "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip/bank/bank.csv"
        )
        dataset = env.data_csv(
            dataset_uri, categorical=categorical, numeric=numeric, labels="y", delimiter=";"
        )

        model_path = "file://localhost//" + os.path.abspath("./data/model.onnx")
        print(model_path)
        model = env.model_onnx(model_path)

        analysis_outcome = env.model_card(dataset, model, sensitive)
        print(analysis_outcome.text)

test_bias_exploration()
