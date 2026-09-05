"use client";

import { useEffect, type ReactNode } from "react";
import { useRouter } from "next/navigation";

import { getToken } from "@/lib/auth";

export default function AuthGuard({ children }: { children: ReactNode }) {
  const router = useRouter();

  const authenticated = Boolean(getToken());

  useEffect(() => {
    if (!authenticated) {
      router.replace("/login");
    }
  }, [authenticated, router]);

  if (!authenticated) {
    return null;
  }

  return <>{children}</>;
}