from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json(silent=True)
    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "The 'title' field is required."}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    new_id = 1
    for event in events:
        if event.id >= new_id:
            new_id = event.id + 1

    # TODO: Task 4 - Return and Handle Results
    new_event = Event(new_id, data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json(silent=True)
    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "The 'title' field is required."}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    for event in events:
        if event.id == event_id:
            # TODO: Task 4 - Return and Handle Results
            event.title = data["title"]
            return jsonify(event.to_dict()), 200

    return jsonify({"error": f"Event with id {event_id} not found."}), 404

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # TODO: Task 3 - Implement the Loop and Process Each Element
    for event in events:
        if event.id == event_id:
            # TODO: Task 4 - Return and Handle Results
            events.remove(event)
            return "", 204

    return jsonify({"error": f"Event with id {event_id} not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)