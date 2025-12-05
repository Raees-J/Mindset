export const API_CONFIG = {
  BASE_URL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000",
  TIMEOUT: 30000, // 30 seconds
  RETRY_ATTEMPTS: 3,
} as const;

export const ROUTES = {
  GUIDANCE: "/api/v1/guidance",
  HEALTH: "/api/v1/health",
} as const;

export const THEME_COLORS = {
  PRIMARY: "#1a5f3f",
  SECONDARY: "#2d8659",
  GOLD: "#d4af37",
  LIGHT: "#f5f5dc",
} as const;

export const ANIMATION_DURATIONS = {
  FAST: 0.2,
  NORMAL: 0.3,
  SLOW: 0.5,
} as const;
