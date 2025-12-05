"use client";

import { motion } from "framer-motion";
import { memo } from "react";
import { GuidanceResult } from "@/lib/api";

interface GuidanceCardProps {
  result: GuidanceResult;
  index: number;
}

const TYPE_COLORS = {
  Quran: "bg-islamic-primary text-white",
  Hadith: "bg-islamic-secondary text-white",
  Dua: "bg-islamic-gold text-black",
} as const;

function GuidanceCard({ result, index }: GuidanceCardProps) {
  const typeColor = TYPE_COLORS[result.type] || "bg-gray-500 text-white";
  const matchPercentage = Math.round(result.similarity_score * 100);

  return (
    <motion.article
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.1 }}
      className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition-shadow duration-300"
      role="article"
      aria-label={`${result.type} guidance`}
    >
      <header className="flex items-center justify-between mb-4">
        <span
          className={`px-3 py-1 rounded-full text-sm font-semibold ${typeColor}`}
          role="status"
        >
          {result.type}
        </span>
        <span className="text-sm text-gray-500" aria-label="Similarity score">
          {matchPercentage}% match
        </span>
      </header>

      <div className="mb-4">
        <p
          className="text-right text-2xl font-arabic leading-loose text-islamic-primary mb-3"
          lang="ar"
          dir="rtl"
        >
          {result.arabic_text}
        </p>
      </div>

      <div className="border-t border-gray-200 pt-4">
        <p className="text-gray-700 leading-relaxed mb-3">
          {result.translation}
        </p>
        <cite className="text-sm text-islamic-secondary font-semibold not-italic">
          — {result.citation}
        </cite>
      </div>
    </motion.article>
  );
}

export default memo(GuidanceCard);
