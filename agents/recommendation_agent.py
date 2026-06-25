def generate_recommendations(department):

    recommendations = {

        "HR": [
            "Review Attendance Policy",
            "Understand Employee Benefits",
            "Check Holiday Calendar"
        ],

        "IT": [
            "Configure Outlook Email",
            "Enable Multi-Factor Authentication",
            "Review IT Security Policy"
        ],

        "Compliance": [
            "Complete Cybersecurity Training",
            "Review Data Privacy Policy",
            "Read Code of Conduct"
        ]
    }

    return recommendations.get(
        department,
        []
    )