# Tech Stack & Packages: Conversion Tools Bank

## Frontend
- **Framework:** SvelteKit
- **Styling:** Tailwind CSS
- **Hosting:** Vercel (for static frontend only)
- **Auth UI:** Custom or use `@auth/sveltekit` with OAuth integration

## Backend
- **Framework:** FastAPI
- **Worker Queue:** Celery (with Redis broker)
- **Caching:** Redis
- **File Storage:** Local + S3 support (or MinIO for self-hosted S3)
- **Deployment:** Dockerized stack on Render, Fly.io, or custom VPS
- **Security:** HTTPS, file size limits, time-based cleanup, CORS config

## Database
- **Primary DB:** PostgreSQL
- **ORM:** SQLAlchemy or Tortoise ORM
- **Migrations:** Alembic

## Authentication
- **Library:** `authlib` or `fastapi-users` for social + email login
- **Social Providers:** Google, Facebook, GitHub
- **JWT Tokens:** for auth sessions

## CRM + Automation
- **Email Gating:** Custom pop-up forms (SvelteKit)
- **Automation:** Make.com Webhooks
- **CRM Platform:** HighLevel (GHL)
- **Email Services:** Mailgun or SendGrid for transactional email

## Monetization + Analytics
- **Analytics:** Google Analytics
- **Ads:** Google AdSense
- **Donations:** BuyMeACoffee embed
- **Optional Future Payments:** Stripe for premium tier

## DevOps
- **Containerization:** Docker
- **CI/CD:** GitHub Actions + Docker build pipeline
- **Monitoring:** UptimeRobot, Sentry (optional)
- **Logging:** FastAPI middleware + PostgreSQL

---

## Recommended Python Packages
- `fastapi`, `uvicorn`, `pydantic`, `httpx`
- `celery`, `redis`
- `boto3` (for S3)
- `python-multipart` (for file upload)
- `sqlalchemy`, `alembic`
- `fastapi-users` or `authlib`

## Recommended Svelte Packages
- `@auth/sveltekit`
- `@tailwindcss/forms`
- `axios` or `fetch` for API
- `zod` or `superstruct` for frontend validation

---

*Last updated: April 8, 2025*

