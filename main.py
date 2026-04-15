from flask import Flask, request, Response
import requests

app = Flask(__name__)

BACKEND_TRACK_URL = "https://api.leadagent.xbytedev.co/api/track"  # public backend URL

PIXEL = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'

@app.route("/track")
def track():
    track_id = request.args.get("id", "").strip()
    if track_id:
        print(f"Email opened by: {track_id}")
        try:
            # Notify LeadAgent so dashboard status updates to OPENED
            requests.get(BACKEND_TRACK_URL, params={"id": track_id}, timeout=5)
        except Exception as e:
            print(f"Forward failed: {e}")

    resp = Response(PIXEL, mimetype="image/gif")
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    resp.headers["Pragma"] = "no-cache"
    resp.headers["Expires"] = "0"
    return resp
 
