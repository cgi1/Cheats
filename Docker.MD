## MySQL
  ### Allow external connections using `-p` argument
  
  ```
  docker run -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mariadb:latest
  
  # Check connection
  mysql -u root -p -h 127.0.0.1 -P3306
  ```
