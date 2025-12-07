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

Let's take it up a notch

---

For the scripts <code>Bug_Query.py</code>, <code>YT-OAuth.py</code>, <code>Youtube-API.py</code>, and <code>Subscriber-list.py</code>
they require a bit of authentication. 

For <code>Bug_Query.py</code> you need and API key which can be found here: https://bugzilla.redhat.com/userprefs.cgi?tab=apikey the script will auto detect if you have the API key expoterd as a varaible using subprocess, echo command, and os. I would recommend setting this up before running your venv and if you still have your venv up make sure you run <code>deactivate</code> before the next steps 

1. ***Quickstart***
     ```bash
     echo echo $BUGZILLA_API_KEY
     ```
