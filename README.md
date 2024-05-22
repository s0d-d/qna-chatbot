# About

ELTE Student Chatbot 🚀

This project builds a chatbot to empower ELTE students with self-service information access. Trained on official documents (rules, scholarships etc.), the chatbot leverages GPT technology to answer frequently asked questions, alleviating pressure on the student coordinator and improving student experience.

## Getting Started

Before you dive in, ensure you have these tools installed:
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Teams Toolkit](https://learn.microsoft.com/en-us/microsoftteams/platform/sbs-gs-notificationbot?tabs=cli&tutorial-step=1#install-teams-toolkit)
- [Node.js](https://nodejs.org/en/download/)
- [Microsoft Teams](https://www.microsoft.com/microsoft-teams/download-app)
- Web browser (Microsoft Edge or Google Chrome)

## Running the Teams App

1.  **Clone the Project:** Clone the project repository using Git.
2.  **Open the Teams Chatbot Folder:** Within VS Code, open **only** the `teams_chatbot` folder. Not the full project.
3.  **Sign in to Teams Toolkit:** Locate the Teams Toolkit extension in the VS Code left sidebar and sign in to your Microsoft 365 account (no developer sandbox required).
4.  **Install Dependencies:** Open the integrated terminal in VS Code, navigate to the project directory using `cd /path/to/project` (replace with your actual path) and run `npm i` to install dependencies.
5.  **Run Locally:** Go to "Development" in Teams Toolkit and select "Preview Your Teams App" to launch the app for testing in a browser or testing tool.
6.  **Deploy to Teams (Optional):** For direct use in Teams, create a deployable package. Navigate to "Utility" in Teams Toolkit and select "Zip Teams App Package." Choose the `manifest.json` file and ensure "local environment" is selected. This creates a zip file.  Within Teams desktop app, access the left-side app bar. Click on "Apps" followed by "Manage your apps." Select "Upload an app" and then "Upload a custom app." Finally, choose the downloaded zip package (located at `/path/to/project/teams_chatbot/appPackage/build/appPackage.local.zip`) to deploy the chatbot to your Teams environment.

## Running the backend (Coming Soon!):
> The description is not complete yet. Detailed instructions for running the backend are forthcoming. In the meantime, explore the Teams app functionality!
- install requirements
- download model from hugging face
- move to models folder
- setup chroma db

## Useful links

- [langchain](https://python.langchain.com/v0.1/docs/expression_language/streaming/)
- [langchain: document retriever](https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/parent_document_retriever/)
- [langchain: chroma db](https://python.langchain.com/v0.1/docs/integrations/vectorstores/chroma/)
- [chromadb](https://docs.trychroma.com/troubleshooting#sqlite)
