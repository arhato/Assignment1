# Volume Creation:

  Used the "docker volume create" command to make volume to store the generated file.
  
  Alternately, we can not use the command and the docker will create a volume for us when we mount; "servervol:/serverdata"; the volume on our run command.
  
    docker run -it --name server-con --network network -p 8080:8080 -v servervol:/serverdata server

# Container Communication:

  Used a user-defined network using the "docker network create" command.
  
  The container are connected to the network on the "run" command with "--network" tag.
  
  The server container exposes its port for communication.
  
  We use the script to retrive the IP address of the server with it name and pass it to the client container as an argument.
    
    SERVER_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server-con)

  The client script connect the IP and port/socket and receive the text file

# Build Scripts:

  Both script create a volume for the containers, build an image and run the container with necessary parameters.

  Server script makes the network for communication.
  
  Client script retrives the IP address of the server container.

  To build the containers:

  Navigate to /server directory first, then run:

    sh fileserver.sh
</br>

  Navigate to /client directory, then run:

     sh fileclien.sh

# Dockerfiles:

  Both use "python" image to build the containers.

  Set the working directory on "/app". The app script is copied to the directory.

  Make a directory to store the text file and mount to the volume.

  A shell environment will open after the app script is run, and will have to be manually close.

# File Verification:

  Will the shell environments are open on both container, we can access their files to confirm and verify the text file that is exchange between them.

  To do this, first you need to navigate to the the "/clientdata" and "/serverdata" directory accordingly and run your commands.

    cd /clientdata                                            
    cat receivedtext.txt
    md5sum receivedtext.txt

</br>

    cd /serverdata                                            
    cat randomtext.txt
    md5sum randomtext.txt

# Full build and verification.

  <img width="1100" alt="serverscript" src="https://github.com/user-attachments/assets/ca41a1e1-ec7a-499f-bd49-6f47d66fe033" />

</br>

  <img width="1126" alt="client" src="https://github.com/user-attachments/assets/cc2d0aeb-0b26-4c2c-80ad-f0c8b8679b50" />


</br>
For offline submission:  

https://github.com/arhato/Assignment1 
