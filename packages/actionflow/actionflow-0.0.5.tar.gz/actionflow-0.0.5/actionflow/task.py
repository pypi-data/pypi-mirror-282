# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
part of the code from https://github.com/phidatahq/phidata
"""
import json
import os
from typing import List, Any, Optional, Dict, Union, Iterator
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, field_validator, Field

from actionflow.assistant import Assistant


class Task(BaseModel):
    # -*- Task settings
    # Task name
    name: Optional[str] = None
    # Task UUID (autogenerated if not set)
    task_id: Optional[str] = Field(None, validate_default=True)
    # Task description
    description: Optional[str] = None

    # Assistant to run this task
    assistant: Optional[Assistant] = None
    # Reviewer for this task. Set reviewer=True for a default reviewer
    reviewer: Optional[Union[Assistant, bool]] = None

    # -*- Task Output
    # Final output of this Task
    output: Optional[Any] = None
    # If True, shows the output of the task in the actionflow.run() function
    show_output: bool = True
    # Output directory to save the output file
    output_dir: str = "outputs"
    # Save the output to a file
    output_file_name: Optional[str] = None

    # Cached values: do not set these directly
    _assistant: Optional[Assistant] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @field_validator("task_id", mode="before")
    def set_task_id(cls, v: Optional[str]) -> str:
        return v if v is not None else str(uuid4())

    @property
    def streamable(self) -> bool:
        return self.get_assistant().streamable

    def get_task_output_as_str(self) -> Optional[str]:
        if self.output is None:
            return None

        if isinstance(self.output, str):
            return self.output

        if issubclass(self.output.__class__, BaseModel):
            # Convert current_task_message to json if it is a BaseModel
            return self.output.model_dump_json(exclude_none=True, indent=2)

        try:
            return json.dumps(self.output, indent=2, ensure_ascii=False)
        except Exception:
            return str(self.output)
        finally:
            return None

    def get_assistant(self) -> Assistant:
        if self._assistant is None:
            self._assistant = self.assistant or Assistant()
        return self._assistant

    def _run(
            self,
            message: Optional[Union[List, Dict, str]] = None,
            *,
            stream: bool = True,
            **kwargs: Any,
    ) -> Iterator[str]:
        assistant = self.get_assistant()
        assistant.task = self.description

        assistant_output = ""
        if stream and self.streamable:
            for chunk in assistant.run(message=message, stream=True, **kwargs):
                assistant_output += chunk if isinstance(chunk, str) else ""
                if self.show_output:
                    yield chunk if isinstance(chunk, str) else ""
        else:
            assistant_output = assistant.run(message=message, stream=False, **kwargs)  # type: ignore

        self.output = assistant_output
        if self.output_file_name:
            os.makedirs(self.output_dir, exist_ok=True)
            save_file = os.path.join(self.output_dir, self.output_file_name)
            with open(save_file, "w") as f:
                f.write(self.output)

        # -*- Yield task output if not streaming
        if not stream:
            if self.show_output:
                yield self.output
            else:
                yield ""

    def run(
            self,
            message: Optional[Union[List, Dict, str]] = None,
            *,
            stream: bool = True,
            **kwargs: Any,
    ) -> Union[Iterator[str], str, BaseModel]:
        if stream and self.streamable:
            resp = self._run(message=message, stream=True, **kwargs)
            return resp
        else:
            resp = self._run(message=message, stream=False, **kwargs)
            return next(resp)
