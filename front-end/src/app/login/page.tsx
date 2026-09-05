"use client";

import { useState, type FormEvent } from "react";
import Image from "next/image";
import { useRouter } from "next/navigation";
import { Eye, EyeOff, Loader2 } from "lucide-react";

import { login } from "@/lib/api";
import { setToken } from "@/lib/auth";
import ServiceFlowLogo from "../../../public/serviceflow_logo.svg";

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);

    if (password.length < 8) {
      setError("La contraseña debe tener al menos 8 caracteres");
      return;
    }

    setLoading(true);
    try {
      const data = await login(email, password);
      setToken(data.access_token);
      router.push("/");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error al iniciar sesión");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="flex items-center justify-center min-h-screen flex-col bg-zinc-950 px-6">
      <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-8 w-full max-w-sm shadow-xl">
        <div className="flex flex-col items-center">
          <div className="mb-4 flex justify-center">
            <Image
              src={ServiceFlowLogo}
              alt="ServiceFlow"
              width={40}
              height={40}
              className="w-10 h-10"
            />
          </div>
          <h1 className="text-white text-lg font-bold tracking-widest text-center mb-1">
            ServiceFlow
          </h1>
          <p className="text-gray-400 text-xs text-center mb-8">Acceso Corporativo</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="usuario" className="block text-xs text-gray-400 mb-1.5">
              Correo Corporativo
            </label>
            <input
              id="usuario"
              name="usuario"
              type="email"
              required
              autoComplete="email"
              placeholder="usuario@serviceflow.com"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              className="w-full bg-zinc-950 border border-zinc-800 text-white rounded-md px-3 py-2 text-sm placeholder-zinc-700 focus:outline-none focus:ring-1 focus:ring-zinc-600 focus:border-zinc-600 transition-colors"
            />
          </div>

          <div>
            <label htmlFor="contrasena" className="block text-xs text-gray-400 mb-1.5">
              Contraseña
            </label>
            <div className="relative w-full">
              <input
                id="contrasena"
                name="contrasena"
                type={showPassword ? "text" : "password"}
                required
                autoComplete="current-password"
                placeholder="••••••••••"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                className="w-full bg-zinc-950 border border-zinc-800 text-white rounded-md px-3 py-2 text-sm placeholder-zinc-700 focus:outline-none focus:ring-1 focus:ring-zinc-600 focus:border-zinc-600 transition-colors pr-10"
              />
              <button
                type="button"
                onClick={() => setShowPassword((value) => !value)}
                aria-label={showPassword ? "Ocultar contraseña" : "Mostrar contraseña"}
                className="absolute right-3 top-2.5 text-zinc-500 w-4 h-4 cursor-pointer hover:text-zinc-300"
              >
                {showPassword ? (
                  <EyeOff className="w-4 h-4" />
                ) : (
                  <Eye className="w-4 h-4" />
                )}
              </button>
            </div>
          </div>

          {error && (
            <p className="text-xs text-red-500" role="alert">
              {error}
            </p>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-white text-black font-medium text-sm py-2 rounded-md mt-6 hover:bg-gray-200 transition-colors disabled:opacity-60 flex items-center justify-center gap-2"
          >
            {loading && <Loader2 className="w-4 h-4 animate-spin" />}
            Iniciar Sesión
          </button>
        </form>
      </div>

      <footer className="text-zinc-600 text-[10px] text-center mt-8 tracking-wide">
        ServiceFlow IT Engine © 2025 • Acceso Seguro Encriptado
      </footer>
    </main>
  );
}