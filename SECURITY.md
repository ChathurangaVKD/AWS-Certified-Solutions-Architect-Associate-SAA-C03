# Security Policy

## Reporting a Vulnerability

We take the security of this study guide repository seriously. While this is primarily an educational resource, we want to ensure the content is safe and accurate.

### What to Report

Please report:

- **Security vulnerabilities** in any scripts, code examples, or configurations
- **Malicious content** or suspicious links
- **Incorrect security practices** that could mislead learners
- **Outdated security information** that could cause harm if implemented

### How to Report

If you discover a security vulnerability, please do one of the following:

1. **Email** the repository maintainers privately (instead of opening a public issue)
2. Use GitHub's Security Advisory feature: "Security" tab → "Report a vulnerability"
3. Open a private discussion if you're uncertain whether it's a security issue

### What to Include

When reporting, please include:

- **Description** of the vulnerability or issue
- **Location** in the repository (file path, line numbers)
- **Potential impact** on learners or users
- **Suggested fix** if you have one

### Response Timeline

- **Initial response**: Within 48 hours
- **Status update**: Within 7 days
- **Resolution**: Varies based on severity and complexity

## Security Best Practices for Contributors

When contributing to this repository:

1. **Never include** real AWS credentials, API keys, or sensitive data
2. **Review code examples** to ensure they follow AWS security best practices
3. **Use placeholder values** like `YOUR_AWS_ACCOUNT_ID` or `example.com`
4. **Document security considerations** for any architectural patterns
5. **Keep dependencies updated** (if any are added in the future)

## Scope

This security policy covers:

- ✅ Documentation content accuracy (especially security-related topics)
- ✅ Code examples and scripts
- ✅ Links to external resources
- ✅ Configuration examples

This policy does NOT cover:

- ❌ AWS platform security (report to AWS directly)
- ❌ Third-party resources linked from this guide
- ❌ Security of individual user AWS accounts

## Acknowledgments

We appreciate the security research community's efforts to keep educational resources safe and accurate. Contributors who report valid security issues will be acknowledged in our [CONTRIBUTORS.md](./CONTRIBUTORS.md) file (unless they prefer to remain anonymous).

---

**Note**: This is an open-source educational project. Always verify information with [official AWS documentation](https://docs.aws.amazon.com/) before implementing in production environments.
