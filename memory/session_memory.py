sessions = {}

def save_session(session_id, data):

    sessions[session_id] = data


def get_session(session_id):

    return sessions.get(session_id)