# Machine-Learning-Project



Creating Conda Environment

'''
conda create -p venv python==3.11.5 -y
'''

Activating conda
'''
conda activate venv/ 
'''
or
'''
conda activate venv
'''

Installing requirements.txt
'''
pip install -r requirements.txt
'''


To add files in git

'''
git add file_Name
'''
or 
'''
git add .
'''

To check the Git Status

'''
git status
'''

To check all version maintained by git 

'''
git log
'''


To create version/commit all the changes by git 

'''
git commit -m "Any Commit Message"
'''

To send versions or changes to github

'''
git push origin main
'''

To check remote url

'''
git remote -v
'''


Build Docker Image

'''
docker build -t <image_name>:<tag_name> .
'''
Note : image_name should always lower case 

To list docker images 
'''
docker images
'''

Run Docker Image

'''
docker run -p 5000:5000 -e PORT=5000 <image ID>
'''
To check running containers in Docker
'''
docker ps
'''

To stop docker container

'''
docer stop <container_ID>