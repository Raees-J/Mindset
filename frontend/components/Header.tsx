"use client";

import { motion } from "framer-motion";

export default function Header() {
  return (
    <header className="pt-8 pb-4 text-center">
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <h1 className="text-4xl md:text-5xl font-bold text-islamic-primary mb-2">
          Islamic Guidance
        </h1>
        <p className="text-gray-600 text-lg">
          Find peace through the wisdom of Quran and Sunnah
        </p>
      </motion.div>
    </header>
  );
}
