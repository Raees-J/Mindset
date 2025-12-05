"use client";

import { motion } from "framer-motion";

export default function LoadingState() {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="flex flex-col items-center justify-center py-12"
      role="status"
      aria-live="polite"
      aria-label="Loading guidance"
    >
      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-islamic-primary"></div>
      <p className="mt-4 text-gray-600">Searching for guidance...</p>
    </motion.div>
  );
}
