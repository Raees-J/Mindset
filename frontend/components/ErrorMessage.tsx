"use client";

import { motion } from "framer-motion";
import { XCircle } from "lucide-react";

interface ErrorMessageProps {
  message: string;
  onDismiss?: () => void;
}

export default function ErrorMessage({ message, onDismiss }: ErrorMessageProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0 }}
      className="max-w-2xl mx-auto px-4 py-8"
      role="alert"
      aria-live="assertive"
    >
      <div className="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start gap-3">
        <XCircle className="h-5 w-5 text-red-600 flex-shrink-0 mt-0.5" />
        <div className="flex-1">
          <p className="text-red-700">{message}</p>
        </div>
        {onDismiss && (
          <button
            onClick={onDismiss}
            className="text-red-600 hover:text-red-800 transition-colors"
            aria-label="Dismiss error"
          >
            ×
          </button>
        )}
      </div>
    </motion.div>
  );
}
