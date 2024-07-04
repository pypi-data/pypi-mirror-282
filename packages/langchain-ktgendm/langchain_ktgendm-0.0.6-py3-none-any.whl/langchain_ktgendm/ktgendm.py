import requests
import datetime
import random
import json
import asyncio
import httpx
from typing import Any, List, Mapping, Optional, Generator
from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun
from concurrent.futures import ThreadPoolExecutor

class ChatKTGenDM(LLM):
    api_key: str = ""
    url: str = ""

    @property
    def _llm_type(self) -> str:
        return "custom_ktgendm"

    def _call(
        self,
        prompt: str,
        session_id: Optional[str] = "",
        temperature: Optional[float] = 0.7,
        app_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:

        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")

        if status == "":
            status = "SU:027"

        now_id = datetime.datetime.now().strftime("%Y%m%d_%H%M_%S%f")[:-3]
        message = {
            "role": "user",
            "content": prompt
        }
        if isinstance(prompt, list):
            if len(prompt) > 0:
                tmp_prompt = prompt[0]
                if "content" in tmp_prompt:
                    message["content"] = tmp_prompt["content"]

        payload = {
            "input": prompt,
            "appid": app_id,
            "id": f"{now_id}",
            "dialog": {
                "session_id": session_id,
                "status": status,
                "messages": [
                ]
            },
            "streaming": "false",
            "temperature": str(temperature)
        }
        headers = {
            "Content-Type": "application/json",
            "Charset": "utf-8"
        }
        response = requests.post(self.url+"/v1/chat/completions", json=payload, headers=headers)
        if response.status_code == 200:
            try:
                return response.json()["system"]
            except Exception as e:
                raise ValueError(f"Error: {e}")
        else:
            raise ValueError(f"Error: {response.status_code}, {response.text}")

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"api_key": self.api_key, "url": self.url}

class ChatKTGenDMTask(ChatKTGenDM):
    api_key: str = ""
    url: str = ""

    def invoke(self, prompt: str, session_id: Optional[str] = "", temperature: Optional[float] = 0.7, app_id: Optional[str] = "", status: Optional[str] = "", stop: Optional[List[str]] = None, run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")

        if session_id == "":
            session_id = str(random.randint(1, 1000000))

        if status == "":
            status = "SU:027"

        now_id = datetime.datetime.now().strftime("%Y%m%d_%H%M_%S%f")[:-3]
        message = {
            "role": "user",
            "content": prompt
        }
        if isinstance(prompt, list):
            if len(prompt) > 0:
                tmp_prompt = prompt[0]
                if "content" in tmp_prompt:
                    message["content"] = tmp_prompt["content"]

        payload = {
            "input": prompt,
            "appid": app_id,
            "id": f"{now_id}",
            "dialog": {
                "session_id": session_id,
                "status": status,
                "messages": [
                ]
            },
            "streaming": "false",
            "temperature": str(temperature)
        }
        headers = {
            "Content-Type": "application/json",
            "Charset": "utf-8"
        }
        response = requests.post(self.url+"/v1/chat/completions", json=payload, headers=headers)
        if response.status_code == 200:
            try:
                obj=response.json()
                output=obj["output"]
                return obj["system"], output["intent"], output["sysAct"], output["serviceId"]

            except Exception as e:
                raise ValueError(f"Error: {e}")
        else:
            raise ValueError(f"Error: {response.status_code}, {response.text}")

class ChatKTGenDMStream(LLM):
    api_key: str = ""
    url: str = ""

    @property
    def _llm_type(self) -> str:
        return "ktgendm"

    async def _stream(
        self,
        prompt: str,
        session_id: Optional[str] = "",
        temperature: Optional[float] = 0.7,
        app_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ):
        try:
            if stop is not None:
                raise ValueError("stop kwargs are not permitted.")

            if session_id == "":
                session_id = str(random.randint(1, 1000000))

            if status == "":
                status = "SU:027"

            now_id = datetime.datetime.now().strftime("%Y%m%d_%H%M_%S%f")[:-3]
            message = {
                "role": "user",
                "content": prompt
            }
            if isinstance(prompt, list):
                if len(prompt) > 0:
                    tmp_prompt = prompt[0]
                    if "content" in tmp_prompt:
                        message["content"] = tmp_prompt["content"]

            payload = {
                "input": prompt,
                "appid": app_id,
                "id": f"{now_id}",
                "dialog": {
                    "session_id": session_id,
                    "status": status,
                    "messages": [
                    ]
                },
                "streaming": "true",
                "temperature": str(temperature)
            }
            headers = {
                "Content-Type": "application/json",
                "Charset": "utf-8"
            }

            async with httpx.AsyncClient() as client:
                async with client.stream("POST", self.url + "/v1/chat/completions", json=payload, headers=headers) as response:
                    if response.status_code == 200:
                        async for chunk in response.aiter_text():
                            if chunk.startswith("data: "):
                                chunk = chunk[6:]
                                chunk = chunk.strip()
                                chunk = json.loads(chunk)
                                if "system" in chunk:
                                    yield chunk["system"]
                    else:
                        raise ValueError(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            raise ValueError(f"Error: {e}")

    def stream(
        self,
        prompt: str,
        session_id: Optional[str] = "",
        temperature: Optional[float] = 0.7,
        app_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Generator[str, None, None]:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def run_stream():
            async for chunk in self._stream(prompt, session_id, temperature, app_id, status, stop, run_manager, **kwargs):
                yield chunk

        with ThreadPoolExecutor() as executor:
            stream_generator = run_stream()
            while True:
                future = executor.submit(loop.run_until_complete, stream_generator.__anext__())
                try:
                    yield future.result()
                except StopAsyncIteration:
                    break


    async def _acall(
        self,
        prompt: str,
        session_id: Optional[str] = "",
        temperature: Optional[float] = 0.7,
        app_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        try:
            if stop is not None:
                raise ValueError("stop kwargs are not permitted.")

            if session_id == "":
                session_id = str(random.randint(1, 1000000))

            if status == "":
                status = "SU:027"

            now_id = datetime.datetime.now().strftime("%Y%m%d_%H%M_%S%f")[:-3]
            message = {
                "role": "user",
                "content": prompt
            }
            if isinstance(prompt, list):
                if len(prompt) > 0:
                    tmp_prompt = prompt[0]
                    if "content" in tmp_prompt:
                        message["content"] = tmp_prompt["content"]

            payload = {
                "input": prompt,
                "appid": app_id,
                "id": f"{now_id}",
                "dialog": {
                    "session_id": session_id,
                    "status": status,
                    "messages": [
                    ]
                },
                "streaming": "true",
                "temperature": str(temperature)
            }
            headers = {
                "Content-Type": "application/json",
                "Charset": "utf-8"
            }


            async with httpx.AsyncClient() as client:
                async with client.stream("POST", self.url + "/v1/chat/completions", json=payload, headers=headers) as response:
                    if response.status_code == 200:
                        tmp = ""
                        async for chunk in response.aiter_text():
                            if chunk.startswith("data: "):
                                chunk = chunk[6:]
                                chunk = chunk.strip()
                                chunk = json.loads(chunk)
                                if "system" in chunk:
                                    tmp=chunk["system"]
                                    print(tmp)
                        return tmp
                    else:
                        raise ValueError(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            raise ValueError(f"Error: {e}")

    def _call(
        self,
        prompt: str,
        session_id: Optional[str] = "",
        temperature: Optional[float] = 0.7,
        app_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        return asyncio.run(self._acall(prompt, session_id, temperature, app_id, status, stop, run_manager, **kwargs))

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"api_key": self.api_key, "url": self.url}
