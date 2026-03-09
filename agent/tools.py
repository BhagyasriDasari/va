from scheduler.appointment_engine import (
    check_availability,
    book_appointment
)


def tool_check_availability(data):

    doctor = data.get("doctor")

    slots = check_availability(doctor)

    return slots


def tool_book(data):

    doctor = data.get("doctor")
    time = "10:00"
    patient = "Patient1"

    result = book_appointment(patient, doctor, time)

    return result