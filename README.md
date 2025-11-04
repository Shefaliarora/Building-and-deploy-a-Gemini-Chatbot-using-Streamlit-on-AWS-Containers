# Building-and-deploy-a-Gemini-Chatbot-using-Streamlit-on-AWS-Containers


# 💬 Gemini AI Chatbot on AWS Containers using Streamlit

### 🧠 Overview

This project demonstrates how to **build and deploy an AI-powered chatbot** using **Google’s Gemini API**, **Streamlit** for the front-end, and **Docker containers** hosted on **AWS EC2**.

The chatbot takes user input through a simple Streamlit interface, sends it to the **Gemini Generative AI model**, and displays intelligent, contextual responses in real time.

---

## 🎯 Objectives

* Understand how to integrate **Gemini API** in a Python app.
* Build an interactive web app using **Streamlit**.
* Containerize the app using **Docker**.
* Deploy the containerized app on **AWS EC2**.

---

## 🏗️ Architecture Diagram

```
User → Streamlit App (Frontend) → Gemini API (AI Model)
           ↓
        Docker Container → AWS EC2 Instance
```

---

## ⚙️ Tech Stack

| Component            | Technology                                    |
| -------------------- | --------------------------------------------- |
| Frontend             | Streamlit                                     |
| AI Model             | Google Gemini API (`google-generativeai` SDK) |
| Containerization     | Docker                                        |
| Cloud Platform       | AWS EC2                                       |
| Programming Language | Python 3.10+                                  |

---

## 📦 Folder Structure

```
gemini_chatbot_container/
│
├── main.py                 # Streamlit app code
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build configuration
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/<your-username>/gemini-chatbot-aws.git
cd gemini-chatbot-aws
```

---

### **2️⃣ Set Up Environment Variables**

Create a `.env` file or export the Gemini API key directly:

```bash
export GOOGLE_API_KEY="your_gemini_api_key"
```

You can generate the key from [Google AI Studio](https://makersuite.google.com/app/apikey).

---

### **3️⃣ Install Dependencies (Local Run)**

```bash
pip install -r requirements.txt
```

Run the app locally:

```bash
streamlit run main.py
```

Then open in browser:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🐳 Containerization with Docker

### **4️⃣ Build Docker Image**

```bash
docker build -t gemini-chatbot .
```

### **5️⃣ Run Docker Container**

```bash
docker run -d -p 8501:8501 -e GOOGLE_API_KEY="your_gemini_api_key" gemini-chatbot
```

Access the app at:
👉 `http://localhost:8501`

---

## ☁️ Deployment on AWS EC2

### **6️⃣ Launch EC2 Instance**

* OS: Ubuntu 22.04
* Type: t2.micro (Free Tier)
* Open **Inbound Ports** in Security Group:

  * 22 → SSH
  * 80 → HTTP
  * 8501 → Streamlit

### **7️⃣ Install Docker on EC2**

```bash
sudo apt update -y
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
exit  # log out and log back in
```

### **8️⃣ Pull or Build Image**

Option 1 — Pull from Docker Hub:

```bash
docker pull <your-dockerhub-username>/gemini-chatbot:latest
```

Option 2 — Build on EC2:

```bash
docker build -t gemini-chatbot .
```

### **9️⃣ Run Container on EC2**

```bash
docker run -d -p 8501:8501 -e GOOGLE_API_KEY="your_gemini_api_key" gemini-chatbot
```

Now open in browser:

```
http://<ec2-public-ip>:8501
```

✅ Your Gemini Chatbot is now live on AWS!

---

## 🧠 Example Streamlit Code (main.py)

```python
import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Gemini AI Chatbot", page_icon="💬")
st.title("🤖 Gemini AI Chatbot")

prompt = st.text_input("Ask Gemini something:")
if prompt:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    st.write("**Gemini:**", response.text)
```

---

## 🧩 requirements.txt

```
streamlit
google-generativeai
```

---

## 🔒 Security Best Practices

* Never hardcode API keys — use environment variables.
* Restrict API key usage from specific IPs or environments.
* Always use updated Python libraries inside Docker containers.
* Regularly rebuild your Docker image to apply security patches.

---

## 📚 References

* [Google Generative AI SDK Documentation](https://ai.google.dev/docs)
* [Streamlit Official Docs](https://docs.streamlit.io/)
* [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
* [Docker Documentation](https://docs.docker.com/)

---

## ❤️ Acknowledgment

Special thanks to **Abhilasha** for the opportunity to present this project on YouTube and share it with the cloud and AI learning community.



