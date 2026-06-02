import pickle
import cv2

# load model and vectorizer
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# read image
img = cv2.imread("qr.png")

# decode QR
detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)

print("Decoded URL:", data)

# predict
url_vec = vectorizer.transform([data])
pred = model.predict(url_vec)

if pred[0] == 1:
    print("Result: Malicious QR Code")
else:
    print("Result: Safe QR Code")
