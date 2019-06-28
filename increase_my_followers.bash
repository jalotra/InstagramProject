#!/bin/bash

echo Hello User,I am the Instagram bot 
echo I will help you get more Instagram Followers.But you have to tell me your Instagram Username , Password.\n


echo I WILL SUPPORT TWO WEBBROWSERS ONLY FIREFOX AND CHROME. And type in all Capitals only.
read -p 'Your Webbrowser:' Webbrowser

function install_geckodriver()
{
    wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
    sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.24.0-linux64.tar.gz -O > /usr/bin/geckodriver'
    sudo chmod +x /usr/bin/geckodriver
    rm geckodriver-v0.24.0-linux64.tar.gz
    # export PATH=$PATH:/path-to-extracted-file/.
}
function install_chromedriver()
{
    wget https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    sudo chmod +x chromedriver
    sudo mv chromedriver /usr/bin/
    rm chromedriver_linux64.zip
    # export PATH=$PATH:/path-to-extracted-file/.
}
if [ $Webbrowser == 'FIREFOX' ]
then
    install_geckodriver
    echo GeckoDriver Installed
elif [ $Webbrowser == 'CHROME' ]
then 
    install_chromedriver
    echo ChromeDriverInstalled
fi
     


function getUserDetails()
{
    read -p 'Username:' instaUsername
    read -p 'Password:' instaPassword
}


echo the following function you can use 1.loginInInstagram 2.increaseFollowers 3.printHashtags

function increaseFollowers()
{
    #WORKS FINE
    getUserDetails
    read -p 'Hashtag:' instaHashtag
    python src/liking_all_hashtags_links.py $instaUsername $instaPassword $instaHashtag
}


function loginInInstagram()
{   
    # WORKS FINE
    python -V
    getUserDetails
    python src/login_into_instagram.py $Webbrowser $instaUsername $instaPassword

}

function printHashtags()
{
    #WORKS FINE
    getUserDetails
    read -p 'Hashtag:' instaHashtag
    python src/searching_for_all_hashtags.py $instaUsername $instaPassword $instaHashtag
} 

