from setfit import AbsaModel, TrainingArguments, AbsaTrainer
from datasets import load_dataset
from transformers import EarlyStoppingCallback

class ABSAModelV1:
    def load_model(self):
        print("loading model...")
        model = AbsaModel.from_pretrained(
            "sentence-transformers/all-MiniLM-L6-v2",
            "sentence-transformers/all-mpnet-base-v2",
            spacy_model="en_core_web_sm",
        )
        print("model loaded")
        return model
    
    def prepare_data(self): 
        print("preparing data...")
        # The training/eval dataset must have `text`, `span`, `label`, and `ordinal` columns
        dataset = load_dataset("tomaarsen/setfit-absa-semeval-restaurants", split="train")
        train_dataset = dataset.select(range(128))
        eval_dataset = dataset.select(range(128, 256))
        print("data prepared")
        return train_dataset, eval_dataset


    def train(self, model, train_dataset, eval_dataset): 
        print("training model...")
        args = TrainingArguments(
            output_dir="models",
            num_epochs=5,
            use_amp=True,
            batch_size=16,
            evaluation_strategy="steps",
            eval_steps=50,
            save_steps=50,
            load_best_model_at_end=True,
        )

        trainer = AbsaTrainer(
            model,
            args=args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=5)],
        )
        trainer.train()
        print("model trained")

    def save(self, model: AbsaModel):
        print("saving model...")
        model.save_pretrained(
            "models/setfit-absa-model-aspect",
            "models/setfit-absa-model-polarity",
        )
        print("model saved")


if __name__ == "__main__":
    model = ABSAModelV1()
    absa_model = model.load_model()
    train_dataset, eval_dataset = model.prepare_data()
    model.train(absa_model, train_dataset, eval_dataset)
    model.save(absa_model)