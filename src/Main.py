from ABSA_model.ABSAModelV1 import ABSAModelV1


if __name__ == '__main__':
    model = ABSAModelV1().load_model()
    preds = model.predict([
       "The service at this restaurant was outstanding, and the dishes were a delight to the palate. Every bite of the seafood pasta was bursting with flavor, and the dessert, a classic tiramisu, was the perfect end to a wonderful dining experience. Highly recommend!",
       "I don't like the sushi!"
    ])
    print(preds)