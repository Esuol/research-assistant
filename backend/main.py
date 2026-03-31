import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="research-assistant-backend")

def _get_openai_client() -> OpenAI:
    """
    延迟创建 client，避免在 import 时就因为缺少环境变量而报错。
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="缺少环境变量 OPENAI_API_KEY（请写到 .env 或在 shell 中 export）。",
        )

    base_url = os.getenv("OPENAI_BASE_URL")
    return OpenAI(api_key=api_key, base_url=base_url)


class ChatRequest(BaseModel):
    message: str
    model: str = "gpt-4o-mini"


@app.get("/")
def health():
    return {"ok": True, "message": "hello"}


@app.post("/chat")
def chat(req: ChatRequest):
    client = _get_openai_client()
    try:
        res = client.chat.completions.create(
            model=req.model,
            messages=[{"role": "user", "content": req.message}],
        )
        return {"text": res.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)