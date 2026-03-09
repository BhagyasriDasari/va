from agent.tools import tool_check_availability, tool_book
from memory.session_memory import save_session, get_session


def process_request(user_text, session_id="123"):

    text = user_text.lower()

    session = get_session(session_id)

    # if user says book but doctor not specified
    if "book" in text and "doctor" not in text:

        save_session(session_id, {"intent": "book_pending"})

        return "Which doctor would you like to see?"

    # user answers doctor
    if session and session.get("intent") == "book_pending":

        data = {
            "intent": "book",
            "doctor": text
        }

        slots = tool_check_availability(data)

        result = tool_book(data)

        save_session(session_id, None)

        return {
            "available_slots": slots,
            "booking_result": result
        }

    if "cancel" in text:
        return {"intent": "cancel"}

    if "reschedule" in text:
        return {"intent": "reschedule"}

    return {"intent": "unknown"}