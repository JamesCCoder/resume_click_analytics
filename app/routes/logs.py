from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
import os
import logging

router = APIRouter()

class ClickEvent(BaseModel):
    buttonId: str
    buttonName: str
    timestamp: str
    ipAddress: str
    sourceUrl: str

click_events_file = 'click_events.json'

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/logClickEvent")
async def log_click_event(event: ClickEvent):
    try:
        # 检查文件是否存在和是否为空
        if not os.path.exists(click_events_file) or os.path.getsize(click_events_file) == 0:
            with open(click_events_file, 'w') as f:
                json.dump([], f)
        
        # 读取文件内容并追加新的事件
        with open(click_events_file, 'r+') as f:
            f.seek(0)
            content = f.read()
            events = json.loads(content) if content else []
            events.append(event.dict())
            f.seek(0)
            f.truncate()
            json.dump(events, f, indent=4)
        
        return {"message": "Click event logged successfully"}
    except Exception as e:
        logger.error(f"Error logging click event: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
