#!/bin/bash

echo Hello User,I am the Instagram bot 
echo I will help you get more Instagram Followers.But you have to tell me your Instagram Username and Password.


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
    wget https://chromedriver.storage.googleapis.com/75.0.3770.90/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    sudo chmod +x chromedriver
    sudo mv chromedriver /usr/bin/
    rm chromedriver_linux64.zip
    # export PATH=$PATH:/path-to-extracted-file/.
}

function check_if_geckodriver_is_present()
{
    current_location=`pwd`
    cd /usr/bin
    geckodriver_variable=$(ls | grep -c "geckodriver")
    if [ "$geckodriver_variable" -eq 1 ]
    then
        echo Chromedriver IS ALREADY PRESENT
        cd $current_location
    else 
        cd $current_location
        download_drivers
    fi
}

function check_if_chromedriver_is_present()
{
    
    current_location=`pwd`
    cd /usr/bin
    chromedriver_variable=$(ls | grep -c "chromedriver")
    if [ "$chromedriver_variable" -eq 1 ]
    then
        echo Chromedriver IS ALREADY PRESENT
        cd $current_location
    else 
        cd $current_location
        download_drivers
    fi
    
}

function download_drivers()
{
    if [ $Webbrowser == 'FIREFOX' ]
then
    install_geckodriver
    echo GeckoDriver Installed
elif [ $Webbrowser == 'CHROME' ]
then 
    install_chromedriver
    echo ChromeDriverInstalled
fi

}

     


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
    python src/liking_all_hashtags_links.py $Webbrowser $instaUsername $instaPassword $instaHashtag
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
    python src/searching_for_all_hashtags.py $Webbrowser $instaUsername $instaPassword $instaHashtag
} 


#Main procedure that will run

if [ $Webbrowser == 'FIREFOX' ]
then
    check_if_geckodriver_is_present
    echo GeckoDriver Installed
elif [ $Webbrowser == 'CHROME' ]
then 
    check_if_chromedriver_is_present
    echo ChromeDriverInstalled
fi
