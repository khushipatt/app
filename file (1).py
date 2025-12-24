"""
🏥 Health Monitoring System
Mock City Disease Data & Constants
"""

# ============================================================
# 🌆 CITY-WISE DISEASE DATA
# ============================================================

CITY_DISEASE_DATA = {
    "Ahmedabad": {
        "diseases": {
            "Dengue": {"current": 145, "trend": "+40%", "risk": "HIGH"},
            "TB": {"current": 89, "trend": "0%", "risk": "MEDIUM"},
            "Malaria": {"current": 34, "trend": "-10%", "risk": "LOW"},
            "Typhoid": {"current": 56, "trend": "+15%", "risk": "MEDIUM"},
            "Flu": {"current": 210, "trend": "+25%", "risk": "HIGH"}
        },
        "weekly_cases": {
            "Week 1": {"Dengue": 80, "TB": 85, "Flu": 150},
            "Week 2": {"Dengue": 95, "TB": 87, "Flu": 170},
            "Week 3": {"Dengue": 120, "TB": 88, "Flu": 190},
            "Week 4": {"Dengue": 145, "TB": 89, "Flu": 210}
        },
        "alert": "🚨 Dengue outbreak in Vastrapur area"
    },
    "Mumbai": {
        "diseases": {
            "Dengue": {"current": 178, "trend": "+20%", "risk": "HIGH"},
            "TB": {"current": 156, "trend": "+5%", "risk": "MEDIUM"},
            "Malaria": {"current": 89, "trend": "+30%", "risk": "HIGH"},
            "Typhoid": {"current": 112, "trend": "+35%", "risk": "HIGH"},
            "Flu": {"current": 340, "trend": "+50%", "risk": "HIGH"}
        },
        "weekly_cases": {
            "Week 1": {"Dengue": 130, "TB": 145, "Flu": 200},
            "Week 2": {"Dengue": 145, "TB": 150, "Flu": 250},
            "Week 3": {"Dengue": 160, "TB": 153, "Flu": 300},
            "Week 4": {"Dengue": 178, "TB": 156, "Flu": 340}
        },
        "alert": "🚨 Flu peak expected next week - Monsoon season"
    },
    "Delhi": {
        "diseases": {
            "Dengue": {"current": 234, "trend": "+55%", "risk": "HIGH"},
            "TB": {"current": 198, "trend": "+10%", "risk": "HIGH"},
            "Malaria": {"current": 67, "trend": "+5%", "risk": "MEDIUM"},
            "Typhoid": {"current": 89, "trend": "+20%", "risk": "MEDIUM"},
            "Flu": {"current": 456, "trend": "+35%", "risk": "HIGH"}
        },
        "weekly_cases": {
            "Week 1": {"Dengue": 120, "TB": 175, "Flu": 300},
            "Week 2": {"Dengue": 156, "TB": 182, "Flu": 350},
            "Week 3": {"Dengue": 190, "TB": 190, "Flu": 400},
            "Week 4": {"Dengue": 234, "TB": 198, "Flu": 456}
        },
        "alert": "🚨 Air quality affecting respiratory cases"
    },
    "Surat": {
        "diseases": {
            "Dengue": {"current": 67, "trend": "+10%", "risk": "MEDIUM"},
            "TB": {"current": 45, "trend": "-5%", "risk": "LOW"},
            "Malaria": {"current": 23, "trend": "0%", "risk": "LOW"},
            "Typhoid": {"current": 34, "trend": "+8%", "risk": "LOW"},
            "Flu": {"current": 89, "trend": "+15%", "risk": "MEDIUM"}
        },
        "weekly_cases": {
            "Week 1": {"Dengue": 55, "TB": 48, "Flu": 70},
            "Week 2": {"Dengue": 58, "TB": 47, "Flu": 75},
            "Week 3": {"Dengue": 62, "TB": 46, "Flu": 82},
            "Week 4": {"Dengue": 67, "TB": 45, "Flu": 89}
        },
        "alert": "✅ Disease levels under control"
    },
    "Rajkot": {
        "diseases": {
            "Dengue": {"current": 34, "trend": "+5%", "risk": "LOW"},
            "TB": {"current": 28, "trend": "0%", "risk": "LOW"},
            "Malaria": {"current": 12, "trend": "-15%", "risk": "LOW"},
            "Typhoid": {"current": 19, "trend": "+3%", "risk": "LOW"},
            "Flu": {"current": 56, "trend": "+10%", "risk": "MEDIUM"}
        },
        "weekly_cases": {
            "Week 1": {"Dengue": 30, "TB": 28, "Flu": 45},
            "Week 2": {"Dengue": 31, "TB": 28, "Flu": 48},
            "Week 3": {"Dengue": 32, "TB": 28, "Flu": 52},
            "Week 4": {"Dengue": 34, "TB": 28, "Flu": 56}
        },
        "alert": "✅ All indicators normal"
    }
}

# ============================================================
# 🩺 SYMPTOM LIST
# ============================================================

SYMPTOM_LIST = [
    "Fever",
    "Cough", 
    "Cold",
    "Headache",
    "Body Pain",
    "Rash",
    "Fatigue",
    "Nausea",
    "Vomiting",
    "Diarrhea",
    "Breathlessness",
    "Chest Pain",
    "Joint Pain",
    "Loss of Appetite",
    "Night Sweats",
    "Weight Loss",
    "Abdominal Pain",
    "Jaundice"
]

# ============================================================
# 🏥 HOSPITAL CONTACTS
# ============================================================

HOSPITAL_CONTACTS = {
    "Ahmedabad": {
        "Civil Hospital Ahmedabad": "+917878001001",
        "VS Hospital": "+917878001002",
        "Sterling Hospital": "+917878001003",
        "Apollo Hospital": "+917878001004"
    },
    "Mumbai": {
        "KEM Hospital": "+919898001001",
        "Lilavati Hospital": "+919898001002",
        "Breach Candy Hospital": "+919898001003",
        "Hinduja Hospital": "+919898001004"
    },
    "Delhi": {
        "AIIMS Delhi": "+911198001001",
        "Safdarjung Hospital": "+911198001002",
        "Max Hospital": "+911198001003",
        "Fortis Hospital": "+911198001004"
    },
    "Surat": {
        "Civil Hospital Surat": "+912612001001",
        "SMIMER Hospital": "+912612001002",
        "Kiran Hospital": "+912612001003"
    },
    "Rajkot": {
        "Civil Hospital Rajkot": "+912812001001",
        "Synergy Hospital": "+912812001002",
        "Wockhardt Hospital": "+912812001003"
    }
}

# ============================================================
# 🗣️ VOICE PATTERNS FOR PARSING
# ============================================================

VOICE_PATTERNS = {
    "english": {
        "symptoms": {
            "fever": "Fever",
            "cough": "Cough",
            "cold": "Cold",
            "headache": "Headache",
            "body pain": "Body Pain",
            "rash": "Rash",
            "fatigue": "Fatigue",
            "tired": "Fatigue",
            "nausea": "Nausea",
            "vomiting": "Vomiting",
            "vomit": "Vomiting",
            "diarrhea": "Diarrhea",
            "loose motion": "Diarrhea",
            "breathlessness": "Breathlessness",
            "breathing problem": "Breathlessness",
            "chest pain": "Chest Pain",
            "joint pain": "Joint Pain"
        }
    },
    "hindi": {
        "symptoms": {
            "बुखार": "Fever",
            "खांसी": "Cough",
            "जुकाम": "Cold",
            "सिरदर्द": "Headache",
            "सिर दर्द": "Headache",
            "बदन दर्द": "Body Pain",
            "थकान": "Fatigue",
            "उल्टी": "Vomiting",
            "दस्त": "Diarrhea",
            "सांस": "Breathlessness",
            "छाती में दर्द": "Chest Pain"
        }
    },
    "gujarati": {
        "symptoms": {
            "તાવ": "Fever",
            "ખાંસી": "Cough",
            "શરદી": "Cold",
            "માથું દુખવું": "Headache",
            "માથાનો દુખાવો": "Headache",
            "શરીર દુખવું": "Body Pain",
            "થાક": "Fatigue",
            "ઊલટી": "Vomiting",
            "ઝાડા": "Diarrhea",
            "શ્વાસ": "Breathlessness"
        }
    }
}

# ============================================================
# 🎨 THEME COLORS
# ============================================================

THEME_COLORS = {
    "primary": "#1E3A8A",
    "primary_light": "#3B82F6",
    "background": "#FFFFFF",
    "card_bg": "#DBEAFE",
    "risk_high": "#EF4444",
    "risk_medium": "#F59E0B",
    "risk_low": "#10B981",
    "text_dark": "#1F2937",
    "text_light": "#6B7280"
}
