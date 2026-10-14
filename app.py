from flask import Flask, render_template, request

app = Flask(__name__)


def check_scam(message):
    text = message.lower()

    scam_words = {
        "otp": "OTP share cheyyamani aduguthunnaru",
        "password": "Password aduguthunnaru",
        "urgent": "Urgent ani pressure chesthunnaru",
        "prize": "Fake prize offer ayye avakasam undhi",
        "click here": "Suspicious link click cheyyamani chepthunnaru",
        "registration fee": "Job kosam fee aduguthunnaru",
        "bank account": "Bank details gurinchi message undhi",
        "won": "Unexpected prize claim undhi",
        "డబ్బులు పంపండి": "Money pampamani aduguthunnaru",
        "ఓటీపీ": "OTP share cheyyamani aduguthunnaru",
        "ఉద్యోగం కోసం ఫీజు": "Job kosam fee aduguthunnaru",
        "otp cheppandi": "OTP aduguthunnaru",
        "money send": "Money pampamani aduguthunnaru",
        "job fee": "Job kosam fee aduguthunnaru",
        "pay now": "Immediate payment aduguthunnaru",
        "kyc update": "KYC details update cheyyamani aduguthunnaru",
        "account blocked": "Account block avuthundhi ani bhayapeduthunnaru",
        "claim reward": "Reward claim cheyyamani chepthunnaru",
        "send money": "Money pampamani aduguthunnaru",
        "verify account": "Account verify cheyyamani aduguthunnaru",
        "free gift": "Free gift offer suspicious ga undochu",
        "click link": "Suspicious link click cheyyamani chepthunnaru",
        "prize money": "Prize money offer suspicious ga undochu"
    }

    reasons = []

    for word, reason in scam_words.items():
        if word in text and reason not in reasons:
            reasons.append(reason)

    if len(reasons) >= 3:
        risk = "High Risk"
        score = 90
        advice = "Multiple warning signs unnayi. OTP or money share cheyyakandi."

    elif len(reasons) >= 1:
        risk = "Suspicious"
        score = 65
        advice = "Suspicious signs unnayi. Sender ni verify cheyyandi."

    else:
        risk = "Needs Review"
        score = 20
        advice = "Known warning signs match avvaledhu. Message safe ani guarantee ledhu."

    return risk, reasons, advice, score


@app.route("/", methods=["GET", "POST"])
def home():
    risk = ""
    reasons = []
    advice = ""
    message = ""
    score = 0

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if message:
            risk, reasons, advice, score = check_scam(message)
        else:
            advice = "Please message enter cheyyandi."

    return render_template(
        "index.html",
        risk=risk,
        reasons=reasons,
        advice=advice,
        message=message,
        score=score
    )


if __name__ == "__main__":
    app.run(debug=True)