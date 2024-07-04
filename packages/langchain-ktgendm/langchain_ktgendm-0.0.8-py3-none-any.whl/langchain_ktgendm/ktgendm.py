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

def create_payload(prompt: str, agent_id: str, session_id: str, status: str, temperature: float, streaming: str) -> dict:
    """
    Create the payload for the request.

    Args:
        prompt (str): The user input prompt.
        agent_id (str): The application ID.
        session_id (str): The session ID.
        status (str): The status of the dialog.
        temperature (float): The temperature for response generation.
        streaming (str): Whether to use streaming response.

    Returns:
        dict: The payload for the request.
    """
    now_id = datetime.datetime.now().strftime("%Y%m%d_%H%M_%S%f")[:-3]
    if status == "":
        status = "SU:027"
    if session_id == "":
        session_id = str(random.randint(1, 1000000))

    message = {
        "role": "user",
        "content": prompt
    }
    if isinstance(prompt, list) and len(prompt) > 0 and "content" in prompt[0]:
        message["content"] = prompt[0]["content"]

    payload = {
        "input": prompt,
        "appid": agent_id,
        "id": f"{now_id}",
        "dialog": {
            "session_id": session_id,
            "status": status,
            "messages": []
        },
        "streaming": streaming,
        "temperature": str(temperature)
    }
    return payload

def post_request(url: str, payload: dict, api_key: str) -> dict:
    """
    Send a POST request with the given payload.

    Args:
        url (str): The URL to send the request to.
        payload (dict): The payload for the request.

    Returns:
        dict: The response from the server.

    Raises:
        ValueError: If the response status code is not 200.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "Charset": "utf-8"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Error: {response.status_code}, {response.text}")

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
        agent_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """
        Make a call to the KTGenDM API.

        Args:
            prompt (str): The user input prompt.
            session_id (Optional[str]): The session ID.
            temperature (Optional[float]): The temperature for response generation.
            agent_id (Optional[str]): The application ID.
            status (Optional[str]): The status of the dialog.
            stop (Optional[List[str]]): List of stop words.
            run_manager (Optional[CallbackManagerForLLMRun]): The callback manager for LLM run.
            **kwargs: Additional keyword arguments.

        Returns:
            str: The system response.
        
        Raises:
            ValueError: If stop is not None or there is an error in the response.
        """
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        payload = create_payload(prompt, agent_id, session_id, status, temperature, streaming="false")
        response = post_request(self.url + "/gendm/chain/v1", payload, self.api_key)
        try:
            return response["system"]
        except Exception as e:
            raise ValueError(f"Error: {e}")

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """
        Get the identifying parameters.

        Returns:
            Mapping[str, Any]: The identifying parameters.
        """
        return {"api_key": self.api_key, "url": self.url}

class ChatKTGenDMTask(ChatKTGenDM):
    def invoke(self, prompt: str, session_id: Optional[str] = "", temperature: Optional[float] = 0.7, agent_id: Optional[str] = "", status: Optional[str] = "", stop: Optional[List[str]] = None, run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any) -> str:
        """
        Invoke the KTGenDM API with task-based response.

        Args:
            prompt (str): The user input prompt.
            session_id (Optional[str]): The session ID.
            temperature (Optional[float]): The temperature for response generation.
            agent_id (Optional[str]): The application ID.
            status (Optional[str]): The status of the dialog.
            stop (Optional[List[str]]): List of stop words.
            run_manager (Optional[CallbackManagerForLLMRun]): The callback manager for LLM run.
            **kwargs: Additional keyword arguments.

        Returns:
            str: The system response, intent, system action, and service ID.

        Raises:
            ValueError: If stop is not None or there is an error in the response.
        """
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        payload = create_payload(prompt, agent_id, session_id, status, temperature, streaming="false")
        response = post_request(self.url + "/gendm/chain/v1", payload, self.api_key)
        try:
            output = response["output"]
            return response["system"], output["intent"], output["sysAct"], output["serviceId"]
        except Exception as e:
            raise ValueError(f"Error: {e}")

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
        agent_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ):
        """
        Stream responses from the KTGenDM API.

        Args:
            prompt (str): The user input prompt.
            session_id (Optional[str]): The session ID.
            temperature (Optional[float]): The temperature for response generation.
            agent_id (Optional[str]): The application ID.
            status (Optional[str]): The status of the dialog.
            stop (Optional[List[str]]): List of stop words.
            run_manager (Optional[CallbackManagerForLLMRun]): The callback manager for LLM run.
            **kwargs: Additional keyword arguments.

        Yields:
            str: The system response chunks.
        
        Raises:
            ValueError: If stop is not None or there is an error in the response.
        """
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        payload = create_payload(prompt, agent_id, session_id, status, temperature, streaming="true")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{self.api_key}",
            "Charset": "utf-8"
        }

        async with httpx.AsyncClient() as client:
            async with client.stream("POST", self.url + "/gendm/chain/v1", json=payload, headers=headers) as response:
                if response.status_code == 200:
                    async for chunk in response.aiter_text():
                        if chunk.startswith("data: "):
                            chunk = chunk[6:].strip()
                            chunk = json.loads(chunk)
                            if "system" in chunk:
                                yield chunk["system"]
                else:
                    raise ValueError(f"Error: {response.status_code}, {response.text}")

    def stream(
        self,
        prompt: str,
        session_id: Optional[str] = "",
        temperature: Optional[float] = 0.7,
        agent_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Generator[str, None, None]:
        """
        Stream responses synchronously using asyncio.

        Args:
            prompt (str): The user input prompt.
            session_id (Optional[str]): The session ID.
            temperature (Optional[float]): The temperature for response generation.
            agent_id (Optional[str]): The application ID.
            status (Optional[str]): The status of the dialog.
            stop (Optional[List[str]]): List of stop words.
            run_manager (Optional[CallbackManagerForLLMRun]): The callback manager for LLM run.
            **kwargs: Additional keyword arguments.

        Yields:
            str: The system response chunks.
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def run_stream():
            async for chunk in self._stream(prompt, session_id, temperature, agent_id, status, stop, run_manager, **kwargs):
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
        agent_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """
        Make an asynchronous call to the KTGenDM API.

        Args:
            prompt (str): The user input prompt.
            session_id (Optional[str]): The session ID.
            temperature (Optional[float]): The temperature for response generation.
            agent_id (Optional[str]): The application ID.
            status (Optional[str]): The status of the dialog.
            stop (Optional[List[str]]): List of stop words.
            run_manager (Optional[CallbackManagerForLLMRun]): The callback manager for LLM run.
            **kwargs: Additional keyword arguments.

        Returns:
            str: The final system response.

        Raises:
            ValueError: If stop is not None or there is an error in the response.
        """
        try:
            if stop is not None:
                raise ValueError("stop kwargs are not permitted.")
            payload = create_payload(prompt, agent_id, session_id, status, temperature, streaming="true")
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
                "Charset": "utf-8"
            }

            async with httpx.AsyncClient() as client:
                async with client.stream("POST", self.url + "/gendm/chain/v1", json=payload, headers=headers) as response:
                    if response.status_code == 200:
                        tmp = ""
                        async for chunk in response.aiter_text():
                            if chunk.startswith("data: "):
                                chunk = chunk[6:].strip()
                                chunk = json.loads(chunk)
                                if "system" in chunk:
                                    tmp = chunk["system"]
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
        agent_id: Optional[str] = "",
        status: Optional[str] = "",
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """
        Synchronously make an asynchronous call to the KTGenDM API.

        Args:
            prompt (str): The user input prompt.
            session_id (Optional[str]): The session ID.
            temperature (Optional[float]): The temperature for response generation.
            agent_id (Optional[str]): The application ID.
            status (Optional[str]): The status of the dialog.
            stop (Optional[List[str]]): List of stop words.
            run_manager (Optional[CallbackManagerForLLMRun]): The callback manager for LLM run.
            **kwargs: Additional keyword arguments.

        Returns:
            str: The final system response.
        """
        return asyncio.run(self._acall(prompt, session_id, temperature, agent_id, status, stop, run_manager, **kwargs))

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """
        Get the identifying parameters.

        Returns:
            Mapping[str, Any]: The identifying parameters.
        """
        return {"api_key": self.api_key, "url": self.url}
