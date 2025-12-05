"use client";

import { motion } from "framer-motion";
import GuidanceCard from "@/components/GuidanceCard";
import { GuidanceResponse } from "@/lib/api";

interface ResultsSectionProps {
  results: GuidanceResponse;
}

export default function ResultsSection({ results }: ResultsSectionProps) {
  return (
    <motion.section
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="max-w-6xl mx-auto px-4 py-12"
    >
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center mb-8"
      >
        <h3 className="text-2xl font-semibold text-islamic-primary mb-2">
          Guidance for: "{results.query}"
        </h3>
        <p className="text-gray-600">
          Found {results.total_results} relevant{" "}
          {results.total_results === 1 ? "result" : "results"}
        </p>
      </motion.div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {results.results.map((result, index) => (
          <GuidanceCard key={`${result.citation}-${index}`} result={result} index={index} />
        ))}
      </div>
    </motion.section>
  );
}
