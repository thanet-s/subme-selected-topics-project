# Subme

Web Application คล้ายๆยูทูป
จัดทำโดย นายธเนษฐ ศิริบูรณ์


# Tools

SvelteKIT
FastAPI
Tortoise ORM
MinIO (AWS S3 compatible)
PostgreSQL
Envoy Proxy
Docker


# How to run
1.

    git clone https://github.com/thanet-s/subme-selected-topics-project.git

2.

    cd subme-selected-topics-project
3.

    docker-compose -f docker-compose-production.yml up -d
4.
เปิด [localhost:3000](http://localhost:3000/) บน browser


**วิธีปิด

    docker-compose -f docker-compose-production.yml down
# URL
[http://localhost:3000](http://localhost:3000) หน้าเว็บ
[http://localhost:3001](http://localhost:3001) MinIO admin
[http://localhost:3002](http://localhost:3002) Adminer