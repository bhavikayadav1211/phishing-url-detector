
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer


# Rule-based detection function
def rule_based_check(url):

    if "@" in url:
        return "malicious"

    if len(url) > 75:
        return "malicious"

    if "bit.ly" in url or "tinyurl" in url:
        return "suspicious"

    return "unknown"


# load dataset
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

train["label"] = train["label"].map({"benign":0,"malicious":1})
test["label"] = test["label"].map({"benign":0,"malicious":1})

X_train = train["url"]
y_train = train["label"]

X_test = test["url"]
y_test = test["label"]

vectorizer = TfidfVectorizer()

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = RandomForestClassifier()
model.fit(X_train_vec, y_train)

pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, pred))
from sklearn.metrics import classification_report
print(classification_report(y_test, pred))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, pred)
print("Confusion Matrix:")
print(cm)