import axios, { AxiosError } from "axios";
import { API_CONFIG, ROUTES } from "./constants";

// Types
export interface GuidanceResult {
  type: "Quran" | "Dua" | "Hadith";
  arabic_text: string;
  translation: string;
  citation: string;
  similarity_score: number;
}

export interface GuidanceResponse {
  results: GuidanceResult[];
  query: string;
  total_results: number;
}

export interface GuidanceRequest {
  emotion_query: string;
}

// Custom error class
export class ApiError extends Error {
  constructor(
    message: string,
    public statusCode?: number,
    public originalError?: unknown
  ) {
    super(message);
    this.name = "ApiError";
  }
}

// Axios instance with default config
const apiClient = axios.create({
  baseURL: API_CONFIG.BASE_URL,
  timeout: API_CONFIG.TIMEOUT,
  headers: {
    "Content-Type": "application/json",
  },
});

// Request interceptor
apiClient.interceptors.request.use(
  (config) => {
    // Add any auth tokens or custom headers here
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
apiClient.interceptors.response.use(
  (response) => response,
  (error: AxiosError) => {
    const message = error.response?.data?.detail || error.message || "An error occurred";
    throw new ApiError(message, error.response?.status, error);
  }
);

/**
 * Fetch Islamic guidance based on emotional query
 * @param query - User's emotional state description
 * @returns Promise with guidance results
 */
export const getGuidance = async (
  query: string,
  excludeQuran: boolean = true
): Promise<GuidanceResponse> => {
  if (!query || query.trim().length === 0) {
    throw new ApiError("Query cannot be empty", 400);
  }

  const requestData: GuidanceRequest = {
    emotion_query: query.trim(),
  };

  const response = await apiClient.post<GuidanceResponse>(
    ROUTES.GUIDANCE,
    requestData
  );

  // Filter out Quran results if excludeQuran is true
  if (excludeQuran) {
    response.data.results = response.data.results.filter(
      (result) => result.type !== "Quran"
    );
    response.data.total_results = response.data.results.length;
  }

  return response.data;
};

/**
 * Get daily Quran verse with Tafsir
 * @returns Promise with daily Quran verse
 */
export const getDailyQuran = async (): Promise<any> => {
  // For now, return a random verse
  // In production, this would be based on date
  const response = await apiClient.get("/api/v1/daily-quran");
  return response.data;
};

/**
 * Check API health status
 * @returns Promise with health status
 */
export const checkHealth = async (): Promise<{ status: string }> => {
  const response = await apiClient.get(ROUTES.HEALTH);
  return response.data;
};
