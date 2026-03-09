from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from agent.agent import process_request
from services.stt import speech_to_text
from services.tts import text_to_speech
import time

router = APIRouter()

@router.websocket("/voice")

async def voice_agent(websocket: WebSocket):

    await websocket.accept()

    try:
        while True:

            start_time = time.time()

            audio_data = await websocket.receive_text()

            text = speech_to_text(audio_data)

            agent_response = process_request(text)

            voice_output = text_to_speech(agent_response)

            end_time = time.time()

            latency = (end_time - start_time) * 1000

            print(f"Latency: {latency:.2f} ms")

            await websocket.send_text(str(voice_output))

    except WebSocketDisconnect:

        print("Client disconnected")