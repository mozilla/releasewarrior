# Staging and merging instance

There is an AWS instance to run staging and merging instances so that we are fewer hops away from the hg repos.  

To access it, you can either 
1. Create an new instance with the AMI named ```Mozilla release staging/merge machine```.  I used a M3.large instance with 32 gb space added.
2. Use the existing instance named "Mozilla release staging/merge machine" in use1.
You will need a pem file to access them, the key for it is the usual location.  You can connect as user ```ubuntu```.

There is also a Dockerfile attached to <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1400015">1400015</a> that can be used to install the requirements for this machine, however, there is still some work to be done to address the credentials issue.
