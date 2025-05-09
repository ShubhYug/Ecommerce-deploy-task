# Ecommerce-deploy-task
test and deploy 



create coverage.html in local:
    inside docker:
        pytest --cov=. --cov-report=html:coverage_html
    outeside docke:
        developer@developer:~$ docker cp 315b984f26ad:/app/coverage_html ./coverage_html
