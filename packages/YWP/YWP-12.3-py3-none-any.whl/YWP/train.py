class AI:
    def __init__(self):
        self.intents = []

    def train(self, jsonfile="intents.json", picklefile="data.pickle", h5file="model.h5"):
        import nltk
        from nltk.stem.lancaster import LancasterStemmer
        import numpy as np
        import tensorflow as tf
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense
        import json
        import pickle

        nltk.download('punkt')
        stemmer = LancasterStemmer()

        try:
            with open(jsonfile, encoding='utf-8') as file:
                data = json.load(file)
        except:
            return 'error:jsonnotfound'

        try:
            with open(picklefile, "rb") as f:
                words, labels, training, output = pickle.load(f)
        except:
            words = []
            labels = []
            docs_x = []
            docs_y = []
            for intent in data["intents"]:
                for pattern in intent["patterns"]:
                    wrds = nltk.word_tokenize(pattern)
                    words.extend(wrds)
                    docs_x.append(wrds)
                    docs_y.append(intent["tag"])

                if intent["tag"] not in labels:
                    labels.append(intent["tag"])

            words = [stemmer.stem(w.lower()) for w in words if w != "?"]
            words = sorted(list(set(words)))

            labels = sorted(labels)

            training = []
            output = []

            out_empty = [0 for _ in range(len(labels))]

            for x, doc in enumerate(docs_x):
                bag = []

                wrds = [stemmer.stem(w) for w in doc]

                for w in words:
                    if w in wrds:
                        bag.append(1)
                    else:
                        bag.append(0)

                output_row = out_empty[:]
                output_row[labels.index(docs_y[x])] = 1

                training.append(bag)
                output.append(output_row)

            training = np.array(training)
            output = np.array(output)

            with open(picklefile, "wb") as f:
                pickle.dump((words, labels, training, output), f)

        model = Sequential()
        model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(len(output[0]), activation='softmax'))

        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        try:
            model.load_weights(h5file)
        except:
            model.fit(training, output, epochs=1000, batch_size=8, verbose=1)
            model.save(h5file)

        return 'done'

    @staticmethod
    def bag_of_words(s, words):
        import nltk
        from nltk.stem.lancaster import LancasterStemmer
        nltk.download('punkt')
        stemmer = LancasterStemmer()
        import numpy as np

        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return np.array(bag)

    def process(self, message="", picklefile="data.pickle", h5file="model.h5", jsonfile="intents.json", sleeptime=0):
        import nltk
        from nltk.stem.lancaster import LancasterStemmer
        nltk.download('punkt')
        stemmer = LancasterStemmer()

        import numpy as np
        import tensorflow as tf
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense
        import random
        import json
        import pickle
        from time import sleep

        try:
            with open(jsonfile, encoding='utf-8') as file:
                data = json.load(file)
        except:
            return 'error:jsonnotfound'

        try:
            with open(picklefile, "rb") as f:
                words, labels, training, output = pickle.load(f)
        except:
            return 'error:picklenotfound'

        model = Sequential()
        model.add(Dense(8, input_shape=(len(training[0]),), activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(len(output[0]), activation='softmax'))

        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        try:
            model.load_weights(h5file)
        except:
            return 'h5notfound'

        bag = self.bag_of_words(message, words)
        results = model.predict(np.array([bag]))[0]
        results_index = np.argmax(results)
        tag = labels[results_index]
        if results[results_index] > 0.8:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            sleep(sleeptime)
            Bot = random.choice(responses)
            return Bot
        else:
            return "I don't understand!"

    def json_creator(self, jsonfile="intents.json", tag="", patterns=[], responses=[]):
        import json
        intents = self.intents

        intents.append({
            "tag": tag,
            "patterns": patterns,
            "responses": responses
        })

        with open(jsonfile, 'w', encoding='utf-8') as f:
            json.dump({"intents": intents}, f, indent=4, ensure_ascii=False)
