# Resume to Readiness — design & architecture notes

## Product promise
Help learners understand how their resume demonstrates a specific target role's requirements, choose a productive learning route, practice skills, and connect with peers. The platform prepares users; it does not offer jobs or guarantee hiring outcomes.

## Main modules
1. Authentication: sign-up, log-in, username length validation (max 70), password policy. Production: server-side password hashing, sessions, rate limits, reset flow, email verification, CSRF protection where applicable.
2. Study profile: academic bio, target role, interests, profile image, privacy settings.
3. Mate network: posts, stories, reactions, comments, connections, groups. Production: database, feed permissions, moderation, reporting, consent, anti-spam.
4. Mentors & solution maintainers: opt-in profiles, topic/availability matching, safe messaging, reporting.
5. Resume lab: allow PDF/DOCX/TXT initially, enforce extension + MIME + size limits, parse in a controlled service, avoid retaining documents by default, compare to a pasted role description.
6. Readiness roadmap: skills, evidence, prerequisites, task milestones, effort/cost estimates.
7. Practice room: mock interview, quiz, project pitch, feedback and history.
8. Bixby: platform help, next-step guidance, study planning, mock-interview conversation; LLM provider connected server-side.
9. Competition board: transparent point rules, progress, weekly challenges, abuse-resistant scoring.

## Data flow
User uploads resume and enters role description → validate file → extract text → normalize → detect requirements → detect resume evidence → classify match/partial/not demonstrated → explain each result → create skill-gap tasks → order tasks with graph search → show progress and let Bixby explain.

## NLP / LLM / A*
- Keyword baseline provides a transparent first demo and is easy to evaluate.
- Semantic matching should use embeddings or a tested NLP pipeline to detect meaning beyond exact words.
- LLMs can write clear explanations and interview prompts; they should not invent evidence or overstate readiness.
- A* searches a skill-dependency graph. Each edge can encode learning hours and money. Use a non-negative edge cost and an admissible heuristic if claiming optimality. For multiple objectives, define and justify a weighted cost function.
- “Low cost” should mean the least estimated total effort/cost under an explicit model, not simply the fewest steps.

## Design system
- Dark navy shell with violet accent, pale canvas, white cards, high-contrast text.
- Persistent left navigation on desktop; collapsible navigation on smaller screens.
- Reusable cards, status labels, progress tracks, task rows, and clear evidence explanations.
- Accessible form labels, visible focus states, responsive breakpoints, and plain-language limitations.

## Production readiness checklist
- [ ] Real database and schema migrations.
- [ ] Secure authentication; never store raw passwords.
- [ ] Authorization checks for every private resource.
- [ ] File type/content validation, size limits, malware scanning, retention/deletion policy.
- [ ] LLM provider adapter with secret stored only server-side.
- [ ] Rate limits, error handling, monitoring, backup and recovery.
- [ ] Community moderation, report/block tools, mentor consent and safe messaging.
- [ ] Privacy notice, terms, user data export/deletion.
- [ ] Unit/integration tests, accessibility review, cross-browser test matrix.
- [ ] Evaluation set for skill extraction and resume/job matching; document false positives/negatives.
