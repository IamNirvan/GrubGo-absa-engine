from setfit import AbsaModel
import os

if __name__ == '__main__':
    model = AbsaModel.from_pretrained(
        os.path.join(os.path.dirname(__file__), "ABSA_model\\models\\setfit-absa-model-aspect"),
        os.path.join(os.path.dirname(__file__), "ABSA_model\\models\\setfit-absa-model-polarity"),
        spacy_model="en_core_web_lg",
        local_files_only=True
    )

    preds = model.predict([
       "The service at this restaurant was outstanding, and the dishes were a delight to the palate. Every bite of the seafood pasta was bursting with flavor, and the dessert, a classic tiramisu, was the perfect end to a wonderful dining experience. Highly recommend!",
       "I don't like the sushi!"
    ])
    print(preds)