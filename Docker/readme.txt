#Please note, I have not included a tar file in here as it will make the gitrepo massive
#You will have to save a local image if you want to scan a tar file
docker save webgoat/webgoat-7.1:latest > webgoat-7.1.tar

# we do not scan docker manifests, we scan docker containers via SUSE and docker images via Sonatype