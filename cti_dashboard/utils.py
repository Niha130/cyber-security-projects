def format_result(data):
    try:
        return {
            "ip": data["data"]["ipAddress"],
            "score": data["data"]["abuseConfidenceScore"],
            "country": data["data"]["countryCode"]
        }
    except:
        return {"error": "Invalid response"}
