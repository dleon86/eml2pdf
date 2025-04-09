# App Flow: Conversion Tools Bank

## 1. Anonymous User Journey
1. Visit homepage
2. Select a tool (e.g., EML to PDF)
3. Upload file → Submit form
4. Conversion starts → Loading screen (status polling or progress bar)
5. Conversion success → Download file
6. Prompt: "Want more conversions? Enter your email to unlock more daily limits"
7. If submitted → Added to CRM via Make → Shown thank you message

## 2. Registered User Journey
1. Sign up with email or social login (Google, Facebook, GitHub)
2. Dashboard shows usage stats and past conversions
3. Navigate to tool page
4. Upload & convert file
5. File is saved in user history (with optional delete/download options)
6. If limits are reached → Notification shown + upsell offer ("Go Premium")

## 3. Conversion Backend Flow (FastAPI)
1. POST request hits `/convert/{tool}` endpoint
2. Backend validates request, checks auth/quota, stores uploaded file
3. Adds conversion job to Redis queue
4. Worker picks up job, runs processing function (e.g., eml2pdf)
5. Result stored temporarily (e.g., in S3 or local temp dir)
6. Return link to download or auto-trigger download on frontend
7. Log event to database (user, time, tool, result, duration)

## 4. Email Automation Flow (CRM)
1. Anonymous user submits email in popup after conversion
2. Frontend sends email data to webhook endpoint
3. Make.com triggers automation
   - Adds to HighLevel contact list
   - Tags with tool used + source
   - Optional: sends follow-up email with tips or a thank-you

## 5. Admin Flow (Future)
1. Admin login panel (not in MVP)
2. View conversion logs
3. Manage premium users, quotas, banned IPs, etc.

---

*Last updated: April 8, 2025*

