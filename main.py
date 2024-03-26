from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
import subprocess
import uvicorn
from datetime import datetime
from DB import Session, Run

app = FastAPI()

bot_status = None
start_time = None
st_num = None


# Ручка для запуска робота
@app.post("/start/")
def start_robot(start_number: int = 0):
    global bot_status
    global start_time
    global st_num
    if bot_status is None or bot_status.poll() is not None:
        start_time = datetime.now()
        st_num = start_number
        bot_status = subprocess.Popen(["python", "robot.py", str(start_number)])
        return {"message": "Робот начал свою работу."}
    else:
        raise HTTPException(status_code=400, detail="Робот уже запущен.")


# Ручка для отключения робота
@app.post("/stop/")
async def stop_robot():
    global bot_status
    global start_time
    global st_num
    if bot_status and bot_status.poll() is None:
        bot_status.terminate()
        bot_status = None
        end_time = datetime.now()
        run_duration = (end_time - start_time).total_seconds()
        session = Session()
        run = Run(start_time=start_time, duration=run_duration, start_number=st_num)
        session.add(run)
        session.commit()
        session.close()
        return {"message": "Робот остановлен."}
    else:
        raise HTTPException(status_code=400, detail="Робот не запущен.")


# Ручка для вывода информации о запусках робота
@app.get("/runs/")
async def get_runs():
    session = Session()
    runs = session.query(Run).all()
    session.close()
    return jsonable_encoder(runs)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
