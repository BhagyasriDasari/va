appointments = []

doctor_schedule = {
    "cardiologist": ["10:00", "11:00", "14:00", "16:00"],
    "dermatologist": ["09:30", "11:30", "15:00"]
}


def check_availability(doctor):

    if doctor in doctor_schedule:
        return doctor_schedule[doctor]

    return []


def book_appointment(patient, doctor, time):

    # check if slot already booked
    for appt in appointments:
        if appt["doctor"] == doctor and appt["time"] == time:
            return "Slot already booked"

    appointment = {
        "patient": patient,
        "doctor": doctor,
        "time": time
    }

    appointments.append(appointment)

    return "Appointment booked successfully"


def get_appointments():
    return appointments