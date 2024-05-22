# About

ELTE Student Chatbot 🚀

This project builds a chatbot to empower ELTE students with self-service information access. Trained on official documents (rules, scholarships etc.), the chatbot leverages GPT technology to answer frequently asked questions, alleviating pressure on the student coordinator and improving student experience.

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/download)
- [Teams Toolkit](https://learn.microsoft.com/en-us/microsoftteams/platform/sbs-gs-notificationbot?tabs=cli&tutorial-step=1#install-teams-toolkit)
- [Node.js](https://nodejs.org/en/download/)
- [Microsoft Teams](https://www.microsoft.com/microsoft-teams/download-app)
- Web browser (Microsoft Edge or Google Chrome)

## How to run Teams App:

- Clone the project
- Then, open only the teams_chatbot folder in VS Code. Not the full project.
- Then, go to Teams Toolkit Extension in the left bar.
- Sign in to your account in the _Accounts > Sign in to Microsoft 365_
  > Note: You can just sign in without the developer sandbox.
- To install dependencies, run the following command:

```shell
$  cd  /path/to/project
/path/to/project $ npm  i
```

- To run your app locally, you can choose one of the options in _Development > Preview Your Teams App_. It will open the app in the testing tool or browser.

- (Optional) if you want to use Teams App, you can download the app as zip package in _Utility > Zip Teams App Package_ section. Choose _manifest.json_ file and then _local_ environment. After downloading, you can go to Teams app. In the left menu bar, select in the following order _Apps > Manage your apps > Upload an app > Upload a custom app_ and choose your zip package. The zip package is in the _/path/to/project/teams_chatbot/appPackage/build/appPackage.local.zip_

## How to run backend:
> The description is not complete yet.
- install requirements
- download model from hugging face
- move to models folder
- setup chroma db

## Useful links

- [langchain](https://python.langchain.com/v0.1/docs/expression_language/streaming/)
- [langchain: document retriever](https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/parent_document_retriever/)
- [langchain: chroma db](https://python.langchain.com/v0.1/docs/integrations/vectorstores/chroma/)
- [chromadb](https://docs.trychroma.com/troubleshooting#sqlite)
