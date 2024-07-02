from typing import Dict, List, Tuple

import os
import random
from datetime import datetime

import pytz
from dotenv import load_dotenv

from parea import Parea, get_current_trace_id, trace
from parea.schemas import Completion, CompletionResponse, FeedbackRequest, LLMInputs, Message, ModelParams, Role

load_dotenv()

p = Parea(api_key=os.getenv("PAREA_API_KEY"))

# Parea SDK makes it easy to use different LLMs with the same apis structure and standardized request/response schemas.
LLM_OPTIONS = [("gpt-3.5-turbo-0125", "openai"), ("gpt-4o", "openai"), ("claude-3-haiku-20240307", "anthropic"), ("claude-3-opus-20240229", "anthropic")]
LIMIT = 1


def dump_task(task):
    d = ""
    for tasklet in task:
        d += f"\n{tasklet.get('task_name','')}"
    d = d.strip()
    return d


def call_llm(
    data: List[Message],
    model: str = "gpt-3.5-turbo",
    provider: str = "openai",
    temperature: float = 0.0,
) -> CompletionResponse:
    return p.completion(
        data=Completion(
            llm_configuration=LLMInputs(
                model=model,
                provider=provider,
                model_params=ModelParams(temp=temperature),
                messages=data,
            )
        )
    )


@trace
def expound_task(main_objective: str, current_task: str) -> List[Dict[str, str]]:
    prompt = [
        Message(
            role=Role.system,
            content=f"You are an AI who performs one task based on the following objective: {main_objective}\n" f"Your task: {current_task}\nResponse:",
        ),
    ]
    response = call_llm(prompt).content
    new_tasks = response.split("\n") if "\n" in response else [response]
    return [{"task_name": task_name} for task_name in new_tasks]


@trace
def generate_tasks(main_objective: str, expounded_initial_task: List[Dict[str, str]]) -> List[str]:
    select_llm_option = random.choice(LLM_OPTIONS)
    task_expansion = dump_task(expounded_initial_task)
    prompt = [
        Message(
            role=Role.user,
            content=(
                f"You are an AI who creates tasks based on the following MAIN OBJECTIVE: {main_objective}\n"
                f"Create tasks pertaining directly to your previous research here:\n"
                f"{task_expansion}\nResponse:"
            ),
        ),
    ]
    response = call_llm(data=prompt, model=select_llm_option[0], provider=select_llm_option[1]).content
    new_tasks = response.split("\n") if "\n" in response else [response]
    task_list = [{"task_name": task_name} for task_name in new_tasks]
    new_tasks_list: List[str] = []
    for task_item in task_list:
        task_description = task_item.get("task_name")
        if task_description:
            task_parts = task_description.strip().split(".", 1)
            if len(task_parts) == 2:
                new_task = task_parts[1].strip()
                new_tasks_list.append(new_task)

    return new_tasks_list


@trace(name=f"run_agent-{datetime.now(pytz.utc)}")  # You can provide a custom name other than the function name
def run_agent(main_objective: str, initial_task: str = "") -> Tuple[List[Dict[str, str]], str]:
    trace_id = get_current_trace_id()
    generated_tasks = []
    expounded_initial_task = expound_task(main_objective, initial_task)
    new_tasks = generate_tasks(main_objective, expounded_initial_task)
    task_counter = 0
    for task in new_tasks or []:
        task_counter += 1
        q = expound_task(main_objective, task)
        exp = dump_task(q)
        generated_tasks.append({f"task_{task_counter}": exp})
        if task_counter >= LIMIT:
            break
    return generated_tasks, trace_id


if __name__ == "__main__":
    result, trace_id = run_agent("Become a machine learning expert.", "Learn about tensors.")
    print(result)
    p.record_feedback(FeedbackRequest(trace_id=trace_id, score=0.642))
