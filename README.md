<!-- ABOUT THE PROJECT -->
## About The Project
Tweeter is a real-time system that will be hosted on a website that Twitter users will draft tweets on.Drafted tweets will be taken as input by our system and return a list of recommended trending hashtags.Tweeter will implement Twitter API’s to collect data and process keywords to recommend trendinghashtags.

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
1. Download [Visual Studio Code](http://code.visualstudio.com/download)
2. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
3. Install a version of Python 3:
    * (macOS) An installation through [Homebrew](https://brew.sh/) on macOS using `brew install python3` (the system install of Python on macOS is not supported).
    * Download [Anaconda](https://www.anaconda.com/download/) (for data science purposes).
    * Have git installed, run in terminal `brew install git` then follow this guide [Git macOS setup](https://sourabhbajaj.com/mac-setup/Git/)

## Step 1: Install code and dependencies
1. Git clone repo and then cd into project directory
2. Create a virtual enviroment directory "venv"
3. Set your the virtual enviroment as source. The use of source under Unix shells ensures that the virtual environment’s variables are set within the current shell, and not in a subprocess (which then disappears, having no useful effect).  
4. Install a list of requirements specified in a Requirements File. Remeber to update this file if you add new libaries.

Using a virtual environment avoids installing Flask into a global Python environment and gives you exact control over the libraries used in an application.
Run the following commands on your computer
```sh
 git clone https://github.com/twitterteam/TwitterFlaskProject.git 
 cd TwitterFlaskProject
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
```
    

These commands will clone this git repository onto your computer,
create a `virtual environment`_ for this project, activate it, and install
the dependencies listed in ``requirements.txt``.

## Step 2: Run Flask App
```sh
flask run
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Team3_uta- [@team3uta](https://twitter.com/team3uta)

Project Link: [https://github.com/twitterteam/TwitterFlaskProject.git ](https://github.com/twitterteam/TwitterFlaskProject.git )
