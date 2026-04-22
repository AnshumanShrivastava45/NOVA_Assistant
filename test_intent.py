from core.intent_classifier import predict_intent

while True:

    text = input("Enter command: ")

    intent = predict_intent(text)

    print("Predicted Intent:", intent)