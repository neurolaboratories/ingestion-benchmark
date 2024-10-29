import httpx
import asyncio
from tqdm import tqdm
import matplotlib.pyplot as plt

from results.env import IR_TASK_UUID, API_URL, API_KEY, BATCH_SIZE, NUM_REQUESTS_PER_SECOND, BENCHMARK_TIMING_IN_SECONDS

FETCH_RESULTS_URL = f"{API_URL}/v2/image-recognition/tasks/{IR_TASK_UUID}/results"
LIMIT = 10

NUM_RESULTS = int(NUM_REQUESTS_PER_SECOND) * int(BENCHMARK_TIMING_IN_SECONDS) * int(BATCH_SIZE)

duration_per_image = []
num_processed_succesfully = 0


headers = {
    "X-API-KEY": API_KEY,
}


def process_results(results):
    global num_processed_succesfully

    for result in results["items"]:
        if result["status"] != "PROCESSED":
            print(result["status"], result["created_at"], result["uuid"])
            continue

        duration_per_image.append(result["duration"])

        num_processed_succesfully += 1


def plot_response_time(duration_per_image):
    # reverse the list to plot the first image first
    data = duration_per_image[::-1]

    # plot response time for each image individually using bars
    plt.bar(range(len(data)), data, width=1.5)
    plt.ylabel("Processing time (s)")
    plt.xlabel("Image")
    plt.title("Processing time for each image")
    plt.savefig("processing_time_plot.png")


async def fetch_results():
    try:
        async with httpx.AsyncClient() as client:
            for offset in tqdm(range(0, NUM_RESULTS, LIMIT)):
                params = {
                    "limit": LIMIT,
                    "offset": offset,
                }
                response = await client.get(
                    FETCH_RESULTS_URL, params=params, headers=headers, timeout=60
                )
                results = response.json()
                process_results(results)

        plot_response_time(duration_per_image)
        avg_duration = sum(duration_per_image) / len(duration_per_image)
        print("Maximum duration per image:", max(duration_per_image))
        print("Minimum duration per image:", min(duration_per_image))
        print(f"Average duration per image: {avg_duration}")
        print(f"Number of images processed successfully: {num_processed_succesfully}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("offset", offset)
        print(f"Average duration per image: {avg_duration}")
        print(f"Number of images processed successfully: {num_processed_succesfully}")


asyncio.run(fetch_results())

