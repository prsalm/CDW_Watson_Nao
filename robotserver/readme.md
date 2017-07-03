## Configuring PyCharm

If you are going to run the server locally from within PyCharm, the new robotserver directory that contains 
the source must be made into a Source Root.  In PyCharm...

1. Right-click on robotserver directory and Mark Directory as... Sources Root.
2. Change the runtime by going to "app" pulldown (upper right of IDE)... Edit Configurations... and set Working Directory to the robotserver directory path.


## Deploying container image to Bluemix

This is a mess... buckle up.

Do not install the IBM Cloud Applications Tools 2 Beta for Mac.  You'll regret it more than the below.

#### Setup the Bluemix CLI

1. Install the Bluemix CLI (bx).  https://console.bluemix.net/docs/cli/index.html#cli
2. Install the Bluemix IBM-Containers, container-registry and container-service plugins.
3. Confirm the CLI is installed properly by doing... `bx info`.
4. Login to Bluemix with the CLI... `bx login`.

#### Build the container image and store it in the Bluemix registry.

5. List the current images in the Bluemix registry... `bx cr images`. Look for the highest
 tag and increment it by one.  This will be the new tag that you'll build.  For
 example, tag=0.10 becomes 0.11.
6. From the robotserver source directory... `bx ic build -t registry.ng.bluemix.net/cdw_dev/robotserver:0.11 .` 
(use the proper tag value).  This may take some time.
7. Make sure the newly created image and tag exists in the registry `bx cr images`.

#### Replace the running container instance.

8. 
