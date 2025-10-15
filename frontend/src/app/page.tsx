"use client";

import { useState } from "react";
import { pingHealth } from "@/lib/api";

export default function Home() {
  const [pantry, setPantry] = useState("eggs, spinach, rice, yogurt");
  const [health, setHealth] = useState<string>("(not checked)");

  async function checkBackend() {
    try {
      const data = await pingHealth();
      setHealth(JSON.stringify(data));
    } catch (e: any) {
      setHealth(`error: ${e?.message || "unknown"}`);
    }
  }

  return (
    <main className="max-w-2xl mx-auto p-6 space-y-6">
      <h1 className="text-2xl font-bold">Savorly</h1>

      <div className="space-y-2">
        <label className="text-sm font-medium">What do you have?</label>
        <textarea
          className="w-full p-3 border rounded-xl"
          rows={3}
          value={pantry}
          onChange={(e) => setPantry(e.target.value)}
        />
        <p className="text-xs text-gray-500">
          (We’ll only use what you list. No shopping—yet.)
        </p>
      </div>

      <div className="flex items-center gap-3">
        <button
          onClick={checkBackend}
          className="px-3 py-2 bg-black text-white rounded-xl text-sm"
        >
          Check backend health
        </button>
        <span className="text-sm text-gray-600">Health: {health}</span>
      </div>
    </main>
  );
}
