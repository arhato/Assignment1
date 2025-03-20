docker network create network
docker volume create servervol
docker build -t server .
docker run -it --name server-con --network network -p 8080:8080 -v servervol:/serverdata server
echo "Server is running. Waiting for client connection..."