"use client";

import { useState, FormEvent, ChangeEvent } from "react";
import { motion } from "framer-motion";
import { PlaceholdersAndVanishInput } from "@/components/ui/placeholders-and-vanish-input";

interface SearchSectionProps {
  onSearch: (query: string) => void;
  isLoading: boolean;
}

const PLACEHOLDERS = [
  "I feel anxious and need comfort...",
  "Remedies for gut health...",
  "What did the Prophet eat for health?",
  "I am grateful and want to thank Allah...",
  "Foods for better sleep...",
  "I need patience and strength...",
  "Natural remedies from Sunnah...",
  "Prophetic medicine for headaches...",
  "I feel sad and need hope...",
  "Healthy lifestyle from Sunnah...",
];

export default function SearchSection({ onSearch, isLoading }: SearchSectionProps) {
  const [query, setQuery] = useState("");

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
  };

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (query.trim() && !isLoading) {
      onSearch(query.trim());
      setQuery(""); // Clear input after submit
    }
  };

  return (
    <section className="flex flex-col items-center justify-center px-4 py-20">
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5, delay: 0.2 }}
        className="w-full max-w-2xl"
      >
        <h2 className="text-center text-xl md:text-2xl text-gray-700 mb-4 font-medium">
          What guidance are you seeking?
        </h2>
        <p className="text-center text-sm text-gray-500 mb-6">
          Search for emotional support, health remedies, lifestyle guidance, and more from authentic Hadiths and Duas
        </p>
        <PlaceholdersAndVanishInput
          placeholders={PLACEHOLDERS}
          onChange={handleChange}
          onSubmit={handleSubmit}
        />
        <p className="text-center text-sm text-gray-500 mt-4">
          Describe your emotional state and receive relevant Islamic guidance
        </p>
      </motion.div>
    </section>
  );
}
