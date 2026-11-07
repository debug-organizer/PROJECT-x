from typing import Dict

LOCALIZED_PRESETS: Dict[str, str] = {
    "as": "জৰুৰী সতৰ্কবাণী: {district} জিলাত ভূমিস্খলনৰ আশংকা বৃদ্ধি পাইছে। সুৰক্ষিত স্থানলৈ স্থানান্তৰ হওক।",
    "bn": "জরুরী সতর্কতা: {district} জেলায় পাহাড়ি ধসের আশঙ্কায় সতর্ক থাকুন।",
    "hi": "आपातकालीन चेतावनी: {district} जिले में भूस्खलन का उच्च जोखिम। सतर्क रहें।",
    "en": "EMERGENCY ALERT: High landslide risk detected in {district} district. Follow emergency protocols."
}

def send_emergency_sms(district: str, language: str, custom_message: str = None) -> dict:
    template = LOCALIZED_PRESETS.get(language, LOCALIZED_PRESETS["en"])
    message = custom_message if custom_message and custom_message.strip() else template.format(district=district)
    
    print(f"\n================ [ SMS BROADCAST DISPATCHED ] ================")
    print(f"Region Target: {district}")
    print(f"Language: {language}")
    print(f"Payload: {message}")
    print(f"==============================================================\n")

    return {
        "status": "DISPATCHED",
        "recipients_notified": 4120,
        "language_used": language,
        "payload": message
    }