# ServiceFlow

<details>
<summary><h2>¿Qué es ServiceFlow?</h2></summary>

ServiceFlow es una plataforma para gestionar y centralizar solicitudes internas de una organización.

Permite registrar, categorizar, asignar, priorizar, atender y cerrar solicitudes, manteniendo un seguimiento de todo el proceso.

</details>

<details>
<summary><h2>¿Quiénes forman parte de ServiceFlow?</h2></summary>

El equipo está formado por:

- Matias Bertuccio
- Alexis Albarenga
- Linder Rodríguez
- Andrés Uzeda

NOTA: Más adelante los roles serán detallados.

</details>

<details>
<summary><h2>Tecnologías</h2></summary>

**Back-End:** Python · FastAPI · SQLAlchemy · Alembic

**Front-End:** React · TypeScript · Vite · Tailwind CSS

**Bases de Datos:** SQL · PostgreSQL

**Testing:** `pytest` · `vitest`

**Infraestructura:** Docker · Docker Compose

**Herramientas:** Git · GitHub · Swagger · Mermaid

</details>

<details>
<summary><h2>Estructura</h2></summary>

```text
                         ┌───────────────────────┐
                         │      ServiceFlow      │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │       Front-End       │
                         ├───────────────────────┤
                         │ React                 │
                         │ TypeScript            │
                         │ Vite                  │
                         │ Tailwind CSS          │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │       Back-End        │
                         ├───────────────────────┤
                         │ Python                │
                         │ FastAPI               │
                         │ SQLAlchemy            │
                         │ Alembic               │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │     Base de Datos     │
                         ├───────────────────────┤
                         │ SQL                   │
                         │ PostgreSQL            │
                         └───────────────────────┘


        ┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
        │      Testing      │  │  Infraestructura  │  │    Herramientas   │
        ├───────────────────┤  ├───────────────────┤  ├───────────────────┤
        │ pytest            │  │ Docker            │  │ Git               │
        │ vitest            │  │ Docker Compose    │  │ GitHub            │
        └───────────────────┘  └───────────────────┘  │ Swagger           │
                                                      │ Mermaid           │
                                                      └───────────────────┘
```
</details>

---

- Creación: 2026-09-02
- Última Actualización: 2026-09-02
