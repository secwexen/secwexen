# Sample CTF Writeup

**Challenge:** Web Exploitation - SQL Injection  
**Date:** 2025-01-01

## Approach
- Recon with Nmap and Dirbuster  
- Identified vulnerable parameter in login form  
- Exploited SQL Injection to bypass authentication

## Solution
1. Constructed payload: `' OR '1'='1`  
2. Gained admin access  
3. Documented steps and learned about input validation weaknesses

**Lessons Learned:** Always validate user input and use parameterized queries.
