"use client";

import { useState } from "react";
import { AnimatePresence } from "framer-motion";
import { ErrorBoundary } from "@/components/ErrorBoundary";
import Header from "@/components/Header";
import Navigation from "@/components/Navigation";
import SearchSection from "@/components/SearchSection";
import LoadingState from "@/components/LoadingState";
import ErrorMessage from "@/components/ErrorMessage";
import ResultsSection from "@/components/ResultsSection";
import QuranTab from "@/components/QuranTab";
import Footer from "@/components/Footer";
import { useGuidance } from "@/hooks/useGuidance";

export default function Home() {
  const [activeTab, setActiveTab] = useState<"guidance" | "quran">("guidance");
  const { results, loading, error, fetchGuidance, reset } = useGuidance();

  return (
    <ErrorBoundary>
      <main className="min-h-screen bg-gradient-to-b from-islamic-light to-white flex flex-col">
        <Header />
        <Navigation activeTab={activeTab} onTabChange={setActiveTab} />

        {activeTab === "guidance" ? (
          <>
            <SearchSection onSearch={fetchGuidance} isLoading={loading} />

            <AnimatePresence mode="wait">
              {loading && <LoadingState key="loading" />}
              {error && <ErrorMessage key="error" message={error} onDismiss={reset} />}
              {results && results.results.length > 0 && (
                <ResultsSection key="results" results={results} />
              )}
            </AnimatePresence>
          </>
        ) : (
          <QuranTab />
        )}

        <Footer />
      </main>
    </ErrorBoundary>
  );
}
