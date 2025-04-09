# Database Schema Design: Conversion Tools Bank

## Users
```sql
users (
    id UUID PRIMARY KEY,
    email TEXT UNIQUE,
    password_hash TEXT,  -- for email/password login
    provider TEXT,       -- e.g., 'google', 'github', 'facebook'
    provider_id TEXT,    -- social login identifier
    created_at TIMESTAMP,
    is_premium BOOLEAN DEFAULT FALSE
)
```

## Conversions
```sql
conversions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    tool_name TEXT,                  -- e.g., 'eml-to-pdf'
    input_filename TEXT,
    output_filename TEXT,
    file_size INTEGER,
    status TEXT,                    -- 'pending', 'completed', 'failed'
    duration_seconds INTEGER,
    created_at TIMESTAMP,
    download_url TEXT,              -- S3/local link
    deleted_at TIMESTAMP           -- for file cleanup tracking
)
```

## Anonymous Emails (CRM Opt-ins)
```sql
leads (
    id UUID PRIMARY KEY,
    email TEXT,
    tool_used TEXT,
    created_at TIMESTAMP,
    source TEXT                     -- e.g., 'conversion-popup', 'landing-page'
)
```

## Rate Limiting (Daily Usage Quotas)
```sql
usage_logs (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    ip_address TEXT,                -- for anonymous rate limiting
    tool_name TEXT,
    conversion_date DATE,
    count INTEGER
)
```

## Premium Subscriptions (Future)
```sql
subscriptions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    plan TEXT,
    status TEXT,                    -- 'active', 'cancelled', 'expired'
    started_at TIMESTAMP,
    ends_at TIMESTAMP
)
```

---

*Last updated: April 8, 2025*

