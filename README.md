# API-Scripts
Each script is a bare-bones starting point that shows how to authenticate, hit endpoints, and parse responses—easy to extend for real projects, view this repo as a barebones API demo.  

1. ***Clone the repo***

   ```bash
   cd $HOME/src
   git clone https://github.com/Tyonnchie-Berry-1996/API-Scripts.git
   cd API-Scripts
   ```

2. ***Auto-generate a requirements file***

   ```bash
   pip install pipreqs
   pipreqs .
   ```
   >Or try this
   
   ```bash
   python3 -m pip install pipreqs
   pipreqs .
   ```
   >Check what deps you need

   ```bash
   cat requirements.txt
   ```      

3. ***Create a venv and install deps***

   ```bash
   python3 -m venv API
   source API/bin/activate
   ```

4. ***Upgrade pip and install the requirements file***

   ```bash
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    python3 -m pip install lxml
   ```
   >Or try this

   ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install lxml
   ```
5. ***Try some easy to use API scripts***
   ```bash
   
   ```   
