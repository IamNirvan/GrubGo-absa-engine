from setfit import AbsaModel
import os

class ABSAModelV1:
    def load_model(self) -> AbsaModel:
        return AbsaModel.from_pretrained(
        os.path.join(os.path.dirname(__file__), "models\\setfit-absa-model-aspect"),
        os.path.join(os.path.dirname(__file__), "models\\setfit-absa-model-polarity"),
        spacy_model="en_core_web_lg",
        local_files_only=True
        )
