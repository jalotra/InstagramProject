### What is this Project About??
```bash
		WORKS ON LINUX BASED DISTROS ONLY!
This project is written in python3 builds upon selenium, geckodriver etc.
With this project we exploit a very fundamental instint of a user using 
Instagram. 

I too did this :
Whenever a person likes my photo and also comments on it, I mostly follow him 
back.Thus this increases the followers of that user.
```
### Folder Structure
```bash
./
 1. src --This is a folder that contains all the main python files.
    1. login_into_instagram.py           -- Python automation to login into instagram 
    2. searching_for_all_hashtags.py     -- Python automation to search for all urls for a particular hashtag
    3. liking_all_hashtags_links.py      -- Pyhton automation to like,follow and see the liked instagram accounts     

 2. .gitignore                           -- For python3

 3. README.md                            -- Contains this very file that you are reading right now.

 4. requirements.txt                     -- Python Packages Required

```
### Install
```bash
git clone ${this_repo_https_address}
cd InstagramProject 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
chmod +x increase_my_followers.bash 
source ./increase_my_followers.bash 

```
### HowToRun
```bash
increaseFollowers        --Can be used to like all the urls that a particular hashtag has on instagram and also follow all the accounts whom pictures that you just liked.
loginInInstagram         --Can be used to login into Instagram Automatically
printHashtags            --Can be used to print a list containing all the urls of photos and videos that a particular hashtag has on instagram.
```
