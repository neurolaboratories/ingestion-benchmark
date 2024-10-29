import { startImageRecognition } from "./utils/imageRecognition.js";
import { IR_TASK_UUID, BATCH_SIZE, BENCHMARK_TIMING_IN_SECONDS, NUM_REQUESTS_PER_SECOND } from "./utils/env.js";
import { getRandomElementsFromArray } from "./utils/random.js";

const IMAGE_URLS = JSON.parse(open('./images.json'));

export const options = {
  scenarios: {
    default: {
      // Constant number of request tests
      executor: 'constant-arrival-rate',
      duration: `${BENCHMARK_TIMING_IN_SECONDS}s`,
      timeUnit: '1s',
      rate: NUM_REQUESTS_PER_SECOND, // to test with different number of requests, update the NUM_REQUESTS_PER_SECOND in the env file
      preAllocatedVUs: 1000

    }
  },
  thresholds: {
    "http_req_duration{scenario:default}": [{ threshold: "max>0" }],
  },
  noConnectionReuse: true,
};


export default async function () {
  const imagesList = getRandomElementsFromArray(IMAGE_URLS, BATCH_SIZE);

  console.log(`Sending ${imagesList.length} images`)
  await startImageRecognition(IR_TASK_UUID, imagesList);
}
