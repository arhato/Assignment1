SERVER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server-con)
docker create volume clientvol
docker build -t client .
docker run -it --name client-con --network network -v clientvol:/clientdata client "$SERVER_IP" 8080
echo "Client is running. Waiting for file transfer..."
