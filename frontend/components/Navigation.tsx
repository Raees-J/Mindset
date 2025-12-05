"use client";

import { motion } from "framer-motion";
import { BookOpen, Heart } from "lucide-react";

interface NavigationProps {
  activeTab: "guidance" | "quran";
  onTabChange: (tab: "guidance" | "quran") => void;
}

export default function Navigation({ activeTab, onTabChange }: NavigationProps) {
  return (
    <nav className="flex justify-center gap-4 mb-8">
      <button
        onClick={() => onTabChange("guidance")}
        className={`flex items-center gap-2 px-6 py-3 rounded-lg font-semibold transition-all ${
          activeTab === "guidance"
            ? "bg-islamic-primary text-white shadow-lg"
            : "bg-white text-gray-700 hover:bg-gray-50"
        }`}
      >
        <Heart className="w-5 h-5" />
        Emotional Guidance
      </button>
      <button
        onClick={() => onTabChange("quran")}
        className={`flex items-center gap-2 px-6 py-3 rounded-lg font-semibold transition-all ${
          activeTab === "quran"
            ? "bg-islamic-primary text-white shadow-lg"
            : "bg-white text-gray-700 hover:bg-gray-50"
        }`}
      >
        <BookOpen className="w-5 h-5" />
        Daily Quran & Tafsir
      </button>
    </nav>
  );
}
