## Start up your own Balrog instance

A note on Balrog. Historically, we've had issues with plugging the staging instance to
the staging release pipeline, so we used another workaround:
- From aws console, create a new ubuntu AWS instance
  - Select the datacenter "us-east-1"
  - Pick the latest Ubuntu provided by AWS
  - Instance Type: Choose m3.medium. You can't choose a t2 because of the network (see next point).
  - Network: Pick "Launch into EC2-Classic". If you run it under a VPC, you won't be able to reach the machine outside of the internal VPN. Moreover, it won't allocate a DNS entry. t2 instances only allow VPC networks.
  - Security group: Choose an existing security group named "balrog-dev". It will open the ports needed for you and release promotion to access Balrog
- login to it and clone Balrog [codebase](https://github.com/mozilla/balrog)
- before starting the balrog process, we need to set `STAGING=1` to make balrog accept `http://ftp.stage.mozaws.net` in the blobs, something like
```diff
diff --git a/docker-compose.yml b/docker-compose.yml
index a0dee5a1..9c712750 100644
--- a/docker-compose.yml
+++ b/docker-compose.yml
@@ -29,17 +29,17 @@ services:
       # Grab mail information from the local environment
       - SMTP_HOST
       - SMTP_PORT
       - SMTP_USERNAME
       - SMTP_PASSWORD
       - SMTP_TLS
       - NOTIFY_TO_ADDR
       - NOTIFY_FROM_ADDR
-      - STAGING
+      - STAGING=1
     healthcheck:
         test: nc -z -v balrogadmin 7070
         interval: 5s
         timeout: 30s
         retries: 10


   balrogpub:
```
- Installer the latest versions of docker and docker-compose. During July 2017, the docker version present in the repo weren't compatible with docker-compose.yml in balrog.
  - [Docker installation](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/). Don't forget the [post installation steps](https://docs.docker.com/engine/installation/linux/linux-postinstall/) which require you to log out and log back in.
  - [Docker-compose installation](https://docs.docker.com/compose/install/).
- follow the [installation](https://github.com/mozilla/balrog#installation) process.
