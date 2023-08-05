import json

# Öffne die JSON-Datei und lade den Inhalt
with open("training_set.json", "r") as file:
    data = json.load(file)

normal_count = 0
anomaly_count = 0

# Iteriere über die Tripletten und zähle die Anzahl von normalen und anormalen Tripletten
for triplet in data:
    if triplet["label"] == "normal":
        normal_count += 1
    else:
        anomaly_count += 1

print("Anzahl der normalen Tripletten:", normal_count)
print("Anzahl der anormalen Tripletten:", anomaly_count)
