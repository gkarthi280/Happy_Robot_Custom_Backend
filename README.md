# Setup Instructions

## 1. Clone and Set Up the Custom API (Python 3)

```bash
git clone https://github.com/gkarthi280/Happy_Robot_Custom_Backend.git
cd Happy_Robot_Custom_Backend
```

Create and activate a virtual environment:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend server:

```bash
python app.py
```

## 2. Set Up a Public URL Using ngrok

Install ngrok (macOS via Homebrew):

```bash
brew install ngrok
```

Create an ngrok account and retrieve your auth token here:
https://dashboard.ngrok.com/get-started/your-authtoken

Add your auth token:

```bash
ngrok config add-authtoken <YOUR_AUTHTOKEN>
```

Expose your local server (e.g., port 5000):

```bash
ngrok http 5000
```

## 3. Update Endpoint in the Happy Robot Use Case

Copy the generated public ngrok URL and replace the API endpoint used in the Happy Robot use case configuration.
