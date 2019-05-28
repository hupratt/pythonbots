import pickle, os
from nltk.classify import ClassifierI
from statistics import mode



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

classifier = open(os.path.join(BASE_DIR,"bayes","naivebayes.pickle"), "rb")
classifier = pickle.load(classifier)

NuSVC_classifier = open(os.path.join(BASE_DIR,"bayes","NuSVC_classifier.pickle"), "rb")
NuSVC_classifier = pickle.load(NuSVC_classifier)

LinearSVC_classifier = open(os.path.join(BASE_DIR,"bayes","LinearSVC_classifier.pickle"), "rb")
LinearSVC_classifier = pickle.load(LinearSVC_classifier)

SGDClassifier_classifier = open(os.path.join(BASE_DIR,"bayes","SGDClassifier_classifier.pickle"), "rb")
SGDClassifier_classifier = pickle.load(SGDClassifier_classifier)

MNB_classifier = open(os.path.join(BASE_DIR,"bayes","MNB_classifier.pickle"), "rb")
MNB_classifier = pickle.load(MNB_classifier)

BernoulliNB_classifier = open(os.path.join(BASE_DIR,"bayes","BernoulliNB_classifier.pickle"), "rb")
BernoulliNB_classifier = pickle.load(BernoulliNB_classifier)

LogisticRegression_classifier = open(os.path.join(BASE_DIR,"bayes","LogisticRegression_classifier.pickle"), "rb")
LogisticRegression_classifier = pickle.load(LogisticRegression_classifier)

word_features_f = open(os.path.join(BASE_DIR,"bayes","word_features.pickle"), "rb")
word_features = pickle.load(word_features_f)


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
        
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        # grabs the feature ie. the review and classifies it as either a negative or a positive review
        for c in self._classifiers:
            v = c.classify(features) # returns 'pos' or 'neg'
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

voted_classifier = VoteClassifier(classifier,
                                  NuSVC_classifier,
                                  LinearSVC_classifier,
                                  SGDClassifier_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)


def find_features(review):
    words = set(review.split(" "))
    #print(words)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

def reddit_classify(content):
  dic = {"Classification": voted_classifier.classify(find_features(content)), "Confidence": voted_classifier.confidence(find_features(content))*100 }
  return dic


#content = """Wasn't an unthrottled fast-lane for emergency and public services the exact example AT&T was using against net neutrality?"""

#print("Classification:", voted_classifier.classify(find_features(content)), "Confidence %:",voted_classifier.confidence(find_features(content))*100)
