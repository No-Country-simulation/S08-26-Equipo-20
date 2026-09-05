"use client";

import { useRouter } from "next/navigation";
import { LogOut } from "lucide-react";

import { clearToken } from "@/lib/auth";

export default function LogoutButton() {
  const router = useRouter();

  function handleLogout() {
    clearToken();
    router.push("/login");
  }

  return (
    <button
      type="button"
      onClick={handleLogout}
      className="inline-flex items-center gap-2 rounded-md border border-zinc-800 px-4 py-2 text-sm text-zinc-300 hover:bg-zinc-900 hover:text-white transition-colors"
    >
      <LogOut className="h-4 w-4" />
      Cerrar Sesión
    </button>
  );
}