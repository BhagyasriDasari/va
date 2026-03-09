import time

patients = [
    {"name": "Rahul", "appointment": "tomorrow"},
    {"name": "Anita", "appointment": "tomorrow"}
]

def run_campaign():

    print("Starting reminder campaign...")

    for patient in patients:

        message = f"Hello {patient['name']}, this is a reminder for your appointment {patient['appointment']}."

        print("Outbound Call →", message)

        time.sleep(2)

    print("Campaign completed")