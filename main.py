from fastapi import FastAPI
import subprocess
import uvicorn


app = FastAPI()

bot_status = None

#Ручка для запуска робота
@app.post("/start/")
async def start_robot(start_number: int = 0):
    global bot_status
    if bot_status is None or bot_status.poll() is not None:
        bot_status = subprocess.Popen(["python", "robot.py", str(start_number)])
        return {"message": "Робот начал свою работу."}
    else:
        return {"message": "Робот уже запущен."}

#Ручка для отключения робота
@app.post("/stop/")
async def stop_robot():
    global bot_status
    if bot_status and bot_status.poll() is None:
        bot_status.terminate()
        bot_status = None
        return {"message": "Робот остановлен."}
    else:
        return {"message": "Робот не запущен."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    