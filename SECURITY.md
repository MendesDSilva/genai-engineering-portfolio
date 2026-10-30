# Security policy

## Scope and current state

This hub contains documentation, templates and a local documentation validator. Application security controls are proposed, not implemented. Only the latest main branch of this hub is maintained.

## Credentials and data

Never commit API keys, tokens, passwords, private keys, real `.env` files, database dumps or personal customer data. Use environment injection or a secret manager in future applications; examples must contain obvious placeholders. Git ignore rules are a convenience, not a security boundary. Review staged changes before every commit.

If a credential is exposed, revoke or rotate it immediately, remove it from active configuration, assess access logs and coordinate history cleanup. Deleting a file from the latest commit does not revoke a credential.

Use synthetic or explicitly licensed public data; minimize personal data, define retention and redact logs. Authenticate services, authorize each resource, constrain tools, validate inputs and protect document access. Treat retrieved content as untrusted data rather than instructions.

## Reporting a vulnerability

Do not publish secrets, exploit payloads containing private data or sensitive details in public issues. If GitHub private vulnerability reporting is enabled, use the repository Security tab to report privately. That feature has not been configured or verified by this task. If unavailable, open a public issue requesting a private contact channel without disclosing the vulnerability, then wait for a channel to be agreed with the maintainer.

Provide affected revision, impact and sanitized reproduction steps through the private channel. No response-time SLA is promised. Remote security settings and contact details must be confirmed by the owner before adding them to this policy.
