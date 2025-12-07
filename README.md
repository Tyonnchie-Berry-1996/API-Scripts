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
   python3 Gmail-List.py
   ```

   ```bash
   python3 Extract-Follwers.py
   ```

   ```bash
   python3 Prettify-JSON.py
   ```

   ## Authentication
   
   The following scripts require API credentials or tokens to run:
   
   - <code>Bug_Query.py</code>
   - <code>YT-OAuth.py</code>
   - <code>Youtube-API.py</code>
   - <code>Subscriber-list.py</code>
   
   ### Bug_Query.py (Bugzilla – Red Hat)
   
   <code>Bug_Query.py</code> uses the Bugzilla API and requires an API key.
   
   You can generate an API key here:  
   https://bugzilla.redhat.com/userprefs.cgi?tab=apikey
   
   The script supports auto detection for environment variables and if it doesn't detect a env var you will be asked to copy and paste you API key into the terminal 
   
    **Environment variable (recommended)**  
      Export your key before running the script:
      ```bash
      export BUGZILLA_API_KEY="your_api_key_here"
      ```
   I will add video tutorials for how to authenticate <code>YT-OAuth.py</code>, <code>Youtube-API.py</code>, <code>Subscriber-list.py</code> soon!
