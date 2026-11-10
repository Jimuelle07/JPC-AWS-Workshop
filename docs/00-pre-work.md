# Pre-work: get ready before Thursday

Time needed: about 20 minutes. Do this at home on the laptop you will bring.

You will finish with Python installed, this project downloaded, and your packages installed. The last two steps (the API key and the setup check) are done at the workshop if you do not have your AWS access yet.

## Step 1: Check your AWS access

The facilitator will tell you which of these applies:

- **Event access:** you receive an event code or login for a temporary AWS account. Keep it handy.
- **Your own AWS account:** make sure you can sign in to the AWS Management Console.

Either way, you only need to be able to open the **Amazon Bedrock** page in the console.

## Step 2: Check your Python version

You need **Python 3.10 or newer**.

Windows (PowerShell):

```powershell
py --version
```

macOS or Linux:

```bash
python3 --version
```

If it is older than 3.10 or not found, install the latest Python from https://www.python.org/downloads/ (on Windows, tick "Add Python to PATH" during install). Then check again.

## Step 3: Get this project

Option A, with Git:

```bash
git clone https://github.com/Jimuelle07/JPC-AWS-Workshop.git
cd JPC-AWS-Workshop
```

Option B, without Git: on the GitHub page click **Code**, then **Download ZIP**, extract it, and open a terminal inside the extracted folder.

## Step 4: Create a virtual environment and install packages

A virtual environment keeps this project's packages separate from the rest of your computer.

Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks the activate script, run this once and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

When it works, your terminal prompt starts with `(.venv)`. Every time you open a new terminal, activate the environment again.

## Step 5: Create a Bedrock API key (at the workshop, or at home if you have access)

1. Sign in to the AWS console and open **Amazon Bedrock**.
2. Make sure the Region in the top-right corner matches the Region the facilitator announces (the default in this project is `ap-southeast-1`, Singapore).
3. In the left menu choose **API keys**.
4. Create a **short-term** API key and copy it. Short-term keys expire on their own, which is what we want.
5. Set it as an environment variable in your terminal. Do not paste it into any file.

Windows (PowerShell):

```powershell
$env:AWS_BEARER_TOKEN_BEDROCK = "paste-your-key-here"
$env:AWS_REGION = "ap-southeast-1"
```

macOS or Linux:

```bash
export AWS_BEARER_TOKEN_BEDROCK="paste-your-key-here"
export AWS_REGION="ap-southeast-1"
```

These settings last only for that terminal window. If you open a new one, set them again.

## Step 6: Run the setup check

```bash
python step0_check_setup.py
```

On Windows use `python` too once the virtual environment is active.

You should see a short greeting from the model and the words **Setup OK**. If you do, you are done.

## Troubleshooting

| What you see | What to do |
|---|---|
| `python` is not recognized | On Windows try `py` instead, or reinstall Python with "Add Python to PATH" ticked |
| Python is older than 3.10 | Install a newer Python from python.org |
| `pip install` fails | Check your internet, make sure the `(.venv)` prompt shows, then try again |
| "No AWS credentials found" | Repeat Step 5 in the same terminal window you are using |
| `AccessDeniedException` | Your key may be for a different Region or not allowed for that model. Ask a volunteer |
| `ValidationException` or model not found | The model ID is wrong for your Region. Ask a volunteer, or set `MODEL_ID` (see `campus_buddy/config.py`) |
| `ThrottlingException` | Wait a few seconds and run it again. Many people are calling at once |

Stuck? Do not worry. Bring your laptop early on workshop day and a volunteer will help at the registration table.
