"""Choice selects from a set of options you define, such as billing or technical support.
This example routes a support ticket and prints the selected team, option probabilities, and confidence.

Uses the Laya System 1 decision model: https://huggingface.co/convaiinnovations/laya
"""

import laya
from laya import Router

# --------------------------------------------------------------
# Step 0: Set up the router (preloaded for fast, sub-35ms routing)
# --------------------------------------------------------------

router = Router(preload=True)

# --------------------------------------------------------------
# Step 1: Give Laya the ticket and the possible answers
# --------------------------------------------------------------

ticket = "I was charged twice for order A-104. Please refund the duplicate."

questions = {
    "team": {
        "type": "choice",
        "instructions": "Which team should handle this support ticket?",
        "criteria": {
            "billing": "Payments, charges, or refunds.",
            "technical": "Errors, bugs, or login failures.",
            "other": "Anything else.",
        },
    },
}

# --------------------------------------------------------------
# Step 2: Make the call and read the typed answer
# --------------------------------------------------------------

response = router.predict(ticket, questions)

answer = response["answers"]["team"]
print("Team:", answer["choice"])
print("Probabilities:", answer["probabilities"])
print("Confidence:", answer["confidence"])
