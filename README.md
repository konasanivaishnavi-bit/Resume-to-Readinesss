# Resume to Readiness — submission starter

A responsive, browser-based career-readiness application prototype. It combines a student dashboard, resume-to-role comparison, skill-gap roadmap, practice room, Bixby demo assistant, and a study-first mate community.

## What works in this starter

- Responsive interface for desktop, tablet, and mobile browser sizes.
- Demo account creation/login with username length validation and basic password rule validation.
- Study bio, target role, profile photo, and local profile settings.
- Resume upload for PDF, DOCX, and TXT (5 MB limit). PDF/DOCX text extraction uses browser libraries loaded from CDNs, so internet access is needed for those formats. TXT can be read directly.
- Transparent keyword-based resume/role comparison and evidence explanations.
- A* concept explained in the roadmap; the included demo orders learning tasks by priority, with illustrative costs.
- Local demo posts, likes, mate connections, profile, tasks, and progress.
- Practice prompts, simple quiz, and rule-based Bixby responses.
- Optional FastAPI starter with `/health`, `/analyze`, and `/bixby`.

## Important truth-in-demo notes

This is a **submission prototype**, not a production-ready social network. The browser stores demo data in `localStorage`; it is not secure multi-user authentication or a shared database. Posts, stories, mentor profiles, and leaderboard entries are illustrative/local demo data. Comments, story viewing, and live sharing are placeholders. Bixby uses rule-based demo replies in the frontend. The resume analyzer uses a small skill keyword dictionary, not a trained NLP model or semantic embedding model. The A* function demonstrates the idea but the current roadmap UI is a small illustrative priority planner, not a validated globally optimal plan.

Do not use real passwords or upload sensitive documents into a shared/public demo. Before real public launch, add server-side authentication, password hashing, database persistence, access controls, upload scanning/validation, moderation/reporting, privacy controls, and an actual LLM provider integration. Keep LLM API keys on the backend only.

## Run locally (quickest)

1. Extract the ZIP.
2. Open `index.html` in a modern browser. For best results, use a local static server:
   - If Python is installed, open a terminal in this folder and run `python -m http.server 5500`
   - Open `http://localhost:5500`
3. Create a demo account. Use a made-up password for the prototype.
4. Open Resume Lab, upload a PDF/DOCX/TXT resume, and paste a target role description.
5. Explore Roadmap, Practice Room, Mate Network, Mentors, Competition Board, Bixby, and Profile.

If opening directly from the filesystem causes browser restrictions, use the local server step.

## Run the optional API

1. In a terminal: `cd backend`
2. Create a virtual environment if desired.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `uvicorn main:app --reload --port 8000`
5. Visit `http://localhost:8000/health` and `http://localhost:8000/docs`.

The frontend starter currently runs independently and does not automatically call the API. To connect it, add a backend URL configuration and `fetch()` calls in `app.js`. Configure CORS using `FRONTEND_ORIGIN`. Do not expose secrets in the frontend.

## Deployment options

### Static demo
Deploy the project root (`index.html`, `styles.css`, `app.js`) to a static host such as GitHub Pages or Vercel. PDF/DOCX extraction libraries are loaded from CDNs. A static deployment has no server-side database or real authentication.

### Full-stack version
Deploy the static frontend and FastAPI backend separately, configure CORS, then add a managed database, server-side authentication, resume storage policy, and an LLM provider adapter. Do not describe the full-stack features as live until they are actually connected and tested.

## Suggested presentation architecture

Browser UI → upload validation → text extraction → NLP preprocessing → skill/evidence matching → gap report → dependency graph → A* route planning → Bixby/LLM explanation.

- **NLP:** normalize and extract text; detect role requirements and resume evidence.
- **Semantic matching (future integration):** embeddings can recognize related wording beyond exact keywords.
- **LLM:** explain findings, generate interview prompts, and help users reflect on next steps. Treat model output as advice that needs review.
- **A*:** states represent learning milestones; edge costs represent estimated hours/money; `g(n)` is cost so far and `h(n)` estimates remaining cost.
- **Evaluation:** label sample resume/job-description pairs and measure skill-match precision/recall, review false matches, and ask users to rate recommendation usefulness.

## Browser compatibility

Designed for modern versions of Chrome, Edge, Firefox, and Safari with responsive CSS. Test the actual target PCs and browsers before submission; compatibility cannot be guaranteed for every legacy browser or locked-down campus device.

## Added features in this layout-preserving update

- Keeps the original page layout, grid structure, and purple/navy colour palette; only small additions were made within existing panels and form rows.
- Resume Lab includes optional target salary and a goal period. These are personal planning inputs, not salary forecasts.
- Resume analysis now looks for matching skill terms plus action/project context and flags whether measurable outcomes appear. Its score remains a heuristic evidence estimate, not a hiring prediction.
- Cost Points are awarded only after submitting a project/document link or a detailed activity description. Descriptions earn 15 points, links 25 points, and a link with a substantive explanation can earn up to 30 points.
- Progress levels: Starter (0–99), Pro (100–299), Pro Max (300–599), Master (600+).
- The dashboard includes a seven-day Cost Points graph and recent evidence submissions.

**Evidence limitation:** this browser-only prototype stores evidence text/links locally and does not independently verify that a link or claim is genuine. Production use requires server-side storage, access controls, and a real evidence-review process.
