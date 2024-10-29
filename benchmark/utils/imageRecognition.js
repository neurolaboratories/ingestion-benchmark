import http from "k6/http";
import { API_BASE_URL, HEADERS } from "./env.js";

export async function startImageRecognition(irTaskUuid, urls, callbackUrl) {
  return http.post(
    `${API_BASE_URL}/v2/image-recognition/tasks/${irTaskUuid}/urls`,
    JSON.stringify({
      urls,
      callback: callbackUrl,
    }),
    { headers: HEADERS }
  );
}
