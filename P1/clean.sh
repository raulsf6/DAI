sudo docker rm -v $(docker ps -a -q -f status=exited)
sudo docker rmi $(docker images -f "dangling=true" -q)