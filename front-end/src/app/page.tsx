import AuthGuard from "@/components/AuthGuard";
import LogoutButton from "@/components/LogoutButton";

export default function Home() {
  return (
    <AuthGuard>
      <main className="flex flex-1 flex-col items-center justify-center gap-6 px-6 text-center">
        <h1 className="mx-auto text-balance text-4xl font-bold tracking-tight text-foreground sm:text-5xl">
          Bienvenido a ServiceFlow
        </h1>
        <p className="text-sm text-zinc-500">
          Sesión iniciada correctamente.
        </p>
        <LogoutButton />
      </main>
    </AuthGuard>
  );
}