from dotenv import load_dotenv

load_dotenv()

import os

IR_TASK_UUID = os.environ["IR_TASK_UUID"]
API_URL = os.environ["API_BASE_URL"]
API_KEY = os.environ["API_KEY"]

BATCH_SIZE = os.environ["BATCH_SIZE"]
NUM_REQUESTS_PER_SECOND = os.environ["NUM_REQUESTS_PER_SECOND"]
BENCHMARK_TIMING_IN_SECONDS = os.environ["BENCHMARK_TIMING_IN_SECONDS"]
