"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronLeft, ChevronRight, Calendar, Search, BookOpen } from "lucide-react";
import { SURAHS, searchSurahs, SurahData } from "@/lib/surahData";

interface QuranVerse {
  surah_number: number;
  ayah_number: number;
  arabic_text: string;
  translation: string;
  surah_name: string;
  tafsir: string;
}

export default function QuranTab() {
  const [viewMode, setViewMode] = useState<"daily" | "surah">("daily");
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedSurah, setSelectedSurah] = useState<SurahData | null>(null);
  const [currentDay, setCurrentDay] = useState(1);
  const [dailyVerse, setDailyVerse] = useState<QuranVerse | null>(null);

  // Sample daily verses
  const sampleVerses: QuranVerse[] = [
    {
      surah_number: 1,
      ayah_number: 1,
      arabic_text: "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
      translation: "In the name of Allah, the Entirely Merciful, the Especially Merciful.",
      surah_name: "Al-Fatihah (The Opening)",
      tafsir: "This verse, known as the Bismillah, is the opening of the Quran. It emphasizes Allah's mercy and compassion."
    },
    {
      surah_number: 2,
      ayah_number: 153,
      arabic_text: "يَا أَيُّهَا الَّذِينَ آمَنُوا اسْتَعِينُوا بِالصَّبْرِ وَالصَّلَاةِ",
      translation: "O you who have believed, seek help through patience and prayer.",
      surah_name: "Al-Baqarah (The Cow)",
      tafsir: "This verse teaches believers two essential tools: patience (Sabr) and prayer (Salah)."
    }
  ];

  useEffect(() => {
    const today = new Date();
    const start = new Date(today.getFullYear(), 0, 0);
    const diff = today.getTime() - start.getTime();
    const oneDay = 1000 * 60 * 60 * 24;
    const dayOfYear = Math.floor(diff / oneDay);
    
    const verseIndex = dayOfYear % sampleVerses.length;
    setDailyVerse(sampleVerses[verseIndex]);
    setCurrentDay(dayOfYear);
  }, []);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;

    const results = searchSurahs(searchQuery);
    if (results.length > 0) {
      setSelectedSurah(results[0]);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="max-w-4xl mx-auto px-4 py-8"
    >
      {/* View Mode Toggle */}
      <div className="flex justify-center gap-4 mb-8">
        <button
          onClick={() => setViewMode("daily")}
          className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold transition-all ${
            viewMode === "daily"
              ? "bg-islamic-primary text-white"
              : "bg-white text-gray-700 hover:bg-gray-50"
          }`}
        >
          <Calendar className="w-4 h-4" />
          Daily Verse
        </button>
        <button
          onClick={() => setViewMode("surah")}
          className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold transition-all ${
            viewMode === "surah"
              ? "bg-islamic-primary text-white"
              : "bg-white text-gray-700 hover:bg-gray-50"
          }`}
        >
          <BookOpen className="w-4 h-4" />
          Search Surah
        </button>
      </div>

      {/* Search Bar */}
      {viewMode === "surah" && (
        <form onSubmit={handleSearch} className="mb-8">
          <div className="relative">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search for a Surah (e.g., 'Al-Fatihah', 'Ikhlas', or '1')"
              className="w-full px-4 py-3 pr-12 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-islamic-primary"
            />
            <button
              type="submit"
              className="absolute right-2 top-1/2 -translate-y-1/2 p-2 bg-islamic-primary text-white rounded-lg hover:bg-islamic-secondary transition-colors"
            >
              <Search className="w-5 h-5" />
            </button>
          </div>
          <p className="text-sm text-gray-500 mt-2 text-center">
            Available: Al-Fatihah (1), Al-Ikhlas (112), Al-Falaq (113)
          </p>
        </form>
      )}

      <AnimatePresence mode="wait">
        {/* Daily Verse View */}
        {viewMode === "daily" && dailyVerse && (
          <motion.div
            key="daily"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            <div className="text-center mb-8">
              <div className="flex items-center justify-center gap-2 text-islamic-secondary mb-2">
                <Calendar className="w-5 h-5" />
                <span className="text-sm font-medium">Daily Quran Reflection</span>
              </div>
              <h2 className="text-3xl font-bold text-islamic-primary mb-2">
                {dailyVerse.surah_name}
              </h2>
              <p className="text-gray-600">
                Surah {dailyVerse.surah_number}, Ayah {dailyVerse.ayah_number}
              </p>
            </div>

            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="mb-8 text-center">
                <p className="text-4xl font-arabic leading-loose text-islamic-primary" lang="ar" dir="rtl">
                  {dailyVerse.arabic_text}
                </p>
              </div>

              <div className="border-t border-gray-200 pt-6 mb-6">
                <h3 className="text-sm font-semibold text-gray-500 uppercase mb-3">
                  Translation
                </h3>
                <p className="text-xl text-gray-800 leading-relaxed">
                  {dailyVerse.translation}
                </p>
              </div>

              <div className="border-t border-gray-200 pt-6">
                <h3 className="text-sm font-semibold text-gray-500 uppercase mb-3">
                  Tafsir (Explanation)
                </h3>
                <p className="text-gray-700 leading-relaxed">
                  {dailyVerse.tafsir}
                </p>
              </div>
            </div>
          </motion.div>
        )}

        {/* Surah View */}
        {viewMode === "surah" && selectedSurah && (
          <motion.div
            key="surah"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            <div className="text-center mb-8">
              <h2 className="text-4xl font-bold text-islamic-primary mb-2">
                {selectedSurah.english_name}
              </h2>
              <p className="text-2xl font-arabic text-islamic-secondary mb-2" dir="rtl">
                {selectedSurah.name}
              </p>
              <p className="text-gray-600">
                Surah {selectedSurah.number} • {selectedSurah.verses.length} Verses
              </p>
            </div>

            <div className="bg-islamic-light rounded-lg p-6 mb-8">
              <h3 className="text-lg font-semibold text-islamic-primary mb-3">
                Overview
              </h3>
              <p className="text-gray-700 leading-relaxed">
                {selectedSurah.overview}
              </p>
            </div>

            <div className="space-y-6">
              {selectedSurah.verses.map((verse, index) => (
                <motion.div
                  key={verse.ayah_number}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.05 }}
                  className="bg-white rounded-lg shadow-lg p-6"
                >
                  <div className="flex items-center justify-between mb-4">
                    <span className="text-sm font-semibold text-islamic-secondary">
                      Ayah {verse.ayah_number}
                    </span>
                  </div>

                  <div className="mb-4">
                    <p className="text-3xl font-arabic leading-loose text-islamic-primary text-right" lang="ar" dir="rtl">
                      {verse.arabic_text}
                    </p>
                  </div>

                  <div className="border-t border-gray-200 pt-4 mb-4">
                    <h4 className="text-xs font-semibold text-gray-500 uppercase mb-2">
                      Translation
                    </h4>
                    <p className="text-gray-800 leading-relaxed">
                      {verse.translation}
                    </p>
                  </div>

                  <div className="border-t border-gray-200 pt-4">
                    <h4 className="text-xs font-semibold text-gray-500 uppercase mb-2">
                      Tafsir
                    </h4>
                    <p className="text-gray-700 leading-relaxed text-sm">
                      {verse.tafsir}
                    </p>
                  </div>
                </motion.div>
              ))}
            </div>

            <div className="mt-8 text-center">
              <button
                onClick={() => {
                  setSelectedSurah(null);
                  setSearchQuery("");
                }}
                className="px-6 py-3 bg-white text-islamic-primary font-semibold rounded-lg shadow hover:shadow-md transition-shadow"
              >
                Search Another Surah
              </button>
            </div>
          </motion.div>
        )}

        {/* Empty State */}
        {viewMode === "surah" && !selectedSurah && (
          <motion.div
            key="empty"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="text-center py-12"
          >
            <BookOpen className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <p className="text-gray-600 text-lg mb-2">
              Search for a Surah to read with Tafsir
            </p>
            <p className="text-gray-500 text-sm">
              Available: Al-Fatihah (1), Al-Ikhlas (112), Al-Falaq (113)
            </p>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
