# ShopCloud - Cloud-Based Secure Web Application
## Capstone Project Report (DevSecOps)
**Student:** aswinkrishnam555  
**Live URL:** http://15.206.94.233  
**GitHub:** https://github.com/aswinkrishnam555/cloud-ecommerce-app

## 1. Architecture
- AWS EC2 (Ubuntu 24.04) — Web Server
- Nginx — Reverse Proxy
- Flask (Python) — Backend
- SQLite — Database
- GitHub Actions — CI/CD
- CloudWatch — Monitoring

## 2. Security
- bcrypt password hashing
- JWT authentication
- UFW Firewall (ports 22, 80, 443)
- Fail2ban brute-force protection
- SSH root login disabled
- Role-based access control

## 3. Deployment Guide
1. Clone repo from GitHub
2. Install requirements: pip install -r requirements.txt
3. Run locally: python run.py
4. AWS: EC2 + Nginx + nohup
5. CI/CD: auto-deploy on git push

## 4. Monitoring
- CloudWatch agent installed
- CPU, Memory, Disk metrics
- App logs: /ecommerce/app
- Nginx logs: /var/log/nginx/

## 5. Application Features
- User registration and login
- Product listing with cart
- Admin dashboard
- CRUD operations