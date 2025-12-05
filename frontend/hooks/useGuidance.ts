import { useState, useCallback } from "react";
import { getGuidance, GuidanceResponse } from "@/lib/api";

interface UseGuidanceReturn {
  results: GuidanceResponse | null;
  loading: boolean;
  error: string | null;
  fetchGuidance: (query: string) => Promise<void>;
  reset: () => void;
}

export function useGuidance(): UseGuidanceReturn {
  const [results, setResults] = useState<GuidanceResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchGuidance = useCallback(async (query: string) => {
    if (!query.trim()) {
      setError("Please enter a valid query");
      return;
    }

    setLoading(true);
    setError(null);
    setResults(null);

    try {
      const data = await getGuidance(query);
      setResults(data);
    } catch (err: any) {
      const errorMessage =
        err.response?.data?.detail ||
        err.message ||
        "Failed to fetch guidance. Please try again.";
      setError(errorMessage);
      console.error("Error fetching guidance:", err);
    } finally {
      setLoading(false);
    }
  }, []);

  const reset = useCallback(() => {
    setResults(null);
    setError(null);
    setLoading(false);
  }, []);

  return {
    results,
    loading,
    error,
    fetchGuidance,
    reset,
  };
}
