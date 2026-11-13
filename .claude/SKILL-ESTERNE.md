# Skill esterne di design (solo parte tecnica)

Skill di terze parti copiate in `.claude/skills/` (e 4 agenti in `.claude/agents/`) per il
redesign del blog e della landing. Servono a Mirko: **non vanno usate per scrivere articoli**
e non cambiano le regole di `CLAUDE.md` e `PUBBLICARE.md`.

Installate il 2026-11-02 dopo uno studio comparativo (stelle GitHub, roundup di blogger) e una
lettura degli script: nessuna chiamata di rete nascosta, nessun hook installato da sé.

| Cartella | Origine (commit) | Licenza | Note |
|---|---|---|---|
| `skills/impeccable` + `agents/impeccable-*.md` | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) `e89e3ad` | Apache-2.0 | Lo script `scripts/impeccable` scarica il proprio motore dalle release GitHub del progetto, verificato con sha256 (`engine-checksums.txt`). Hook del plugin non installati. |
| `skills/design-taste-frontend` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) `12af471` | MIT | Gli script aprono un Chrome locale per gli screenshot. Le immagini da musei/NASA/Openverse si scaricano solo su richiesta. |
| `skills/ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) `3a13158` | MIT | Script Python solo locali. Tolti i test; percorso `${CLAUDE_PLUGIN_ROOT}` sostituito con `.claude/skills/…`. |
| `skills/hallmark` | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) `4f6a46c` | MIT | Tolti test e fixture. Generazione immagini solo con `TOGETHER_API_KEY` (non impostata). Hook `install-hook.mjs` **non** installato. |
| `skills/accessibility`, `best-practices`, `core-web-vitals`, `performance`, `seo`, `web-quality-audit` | [addyosmani/web-quality-skills](https://github.com/addyosmani/web-quality-skills) `afa8da9` | MIT | `analyze.sh` è di sola lettura. |
| `skills/web-design-guidelines` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) `1a2c79d` + [web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | MIT | L'originale scarica le regole da internet a ogni uso: qui sono in copia fissa (`guidelines.md`). |

Aggiornare una skill: riscaricare il repository, rileggere gli script cambiati, sostituire la
cartella e aggiornare il commit in questa tabella.
