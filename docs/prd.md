# Product Requirements Document (PRD) for Conversion Tools Bank

## Overview
Conversion Tools Bank is a suite of lightweight web-based utilities that convert various file types (e.g., EML to PDF, STL to STEP) within a centralized app. It offers a freemium model with CRM-integrated email capture, user accounts, usage tracking, and a donation-based upsell strategy.

---

## Core Features

### ✅ File Conversion Tools
- EML to PDF (MVP)
- STL to STEP / OBJ
- EPUB to MOBI
- HEIC to JPG
- DOCX to LaTeX
- MP4 to MP3

### 🧑 User Management
- Email & social login (Google, Facebook, GitHub)
- Anonymous users allowed with limited access
- User dashboard with saved conversions & history

### 📊 Usage Controls (Freemium)
- Anonymous users: max 3 conversions per 24h, file size limits (e.g., 10MB)
- Registered users: higher limits, saved history
- Premium plan (future): larger files, bulk conversion, priority processing

### 💌 CRM + Email Capture
- Email form after conversion for anonymous users (optional)
- Email addresses are pushed to HighLevel CRM via Make.com

### 💸 Monetization
- Google AdSense (display ads on tool pages)
- BuyMeACoffee integration
- Future: upsell premium tiers or offer downloadable desktop tool

### 📈 Analytics & Logs
- Google Analytics for web traffic
- Tool-level usage logging (stored in DB)
- Conversion performance metrics (time, success/failure)

### 🔐 Backend Considerations
- File uploads stored temporarily (auto-deletion after X mins)
- Background tasks for long conversions (e.g., Whisper audio processing)
- Redis queue/caching for heavy processing

---

## Goals by Phase

### Phase 1 (MVP)
- FastAPI backend with EML to PDF tool
- SvelteKit frontend with Tailwind CSS styling
- User login, conversion quota logic
- Anonymous usage with email capture form
- PostgreSQL & Redis setup
- Hosted on Docker (self-deploy or cloud VPS)

### Phase 2
- Add 3D file converters and more tool routes
- Build user dashboard and file history
- Add social login options
- Begin analytics tracking + ad integration

### Phase 3
- Premium tier with billing (Stripe)
- Rate-limited API access
- Desktop version of most popular tools
- Deeper email automation funnels

---

## Success Metrics
- Number of conversions per day
- Daily active users (DAUs)
- Email opt-in rate for anonymous users
- Revenue from ads + donations
- Tool usage distribution (to guide future tool dev)

---

## Risks
- Processing timeouts on shared cloud platforms
- File security and user trust with uploads
- Abuse/spam prevention for conversion quota
- Ad blockers reducing monetization

---

## Next Steps
- Finalize tool prioritization list
- Scaffold FastAPI + SvelteKit project
- Design PostgreSQL schema
- Set up Make integration with HighLevel
- Deploy first MVP tool: EML to PDF

---

*Last updated: April 8, 2025*
