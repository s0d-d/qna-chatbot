## Get started with the ChatBot 
> **Prerequisites**
>
> To run the ChatBot in your local dev machine, you will need:
>
> - [Node.js](https://nodejs.org/), supported versions: 16, 18
> - [Teams Toolkit Visual Studio Code Extension](https://aka.ms/teams-toolkit) version 5.0.0 and
higher or [Teams Toolkit CLI](https://aka.ms/teams-toolkit-cli)
> - An account with [OpenAI](https://platform.openai.com/).

1. First, select the Teams Toolkit icon on the left in the VS Code toolbar.
1. In file *env/.env.testtool.user*, fill in your OpenAI key `SECRET_OPENAI_API_KEY=<your-key>`.
1. Press F5 to start debugging which launches your app in Teams App Test Tool using a web browser. Select `Debug in Test Tool (Preview)`.
1. You will receive a welcome message from the bot, or send any message to get a response.


### Use Azure OpenAI
Above steps use OpenAI as AI service, optionally, you can also use Azure OpenAI as AI service.
> **Prerequisites**
>
> - Prepare your own [Azure OpenAI](https://aka.ms/oai/access) resource.

1. In file *env/.env.local.user*, fill in your Azure OpenAI key `SECRET_AZURE_OPENAI_API_KEY=<your-key>` and endpoint `SECRET_AZURE_OPENAI_ENDPOINT=<your-endpoint>`.
1. In `src/app.js`, comment out *"Use OpenAI"* part and uncomment *"use Azure OpenAI"* part, e.g.
    ```javascript
    const model = new OpenAIModel({
      // Use OpenAI
      // apiKey: config.openAIKey,
      // defaultModel: "gpt-3.5-turbo",

      // Uncomment the following lines to use Azure OpenAI
      azureApiKey: config.azureOpenAIKey,
      azureDefaultDeployment: "gpt-35-turbo",
      azureEndpoint: config.azureOpenAIEndpoint,

      useSystemMessages: true,
      logRequests: true,
    });
    ```
1. In `src/app.js`, update `azureDefaultDeployment` to your own model deployment name.

## What's included in the template

| Folder       | Contents                                            |
| - | - |
| `.vscode`    | VSCode files for debugging                          |
| `appPackage` | Templates for the Teams application manifest        |
| `env`        | Environment files                                   |
| `infra`      | Templates for provisioning Azure resources          |
| `src`        | The source code for the application                 |

The following files can be customized.

| File                                 | Contents                                           |
| - | - |
|`src/index.js`| Sets up and configures the AI Chat Bot.|
|`src/app.js`| Handles business logics for the AI Chat Bot.|
|`src/config.js`| Defines the environment variables.|
|`src/prompts/chat/skprompt.txt`| Defines the prompt.|
|`src/prompts/chat/config.json`| Configures the prompt.|

The following are Teams Toolkit specific project files.

| File                                 | Contents                                           |
| - | - |
|`teamsapp.yml`|This is the main Teams Toolkit project file. The project file defines two primary things:  Properties and configuration Stage definitions. |
|`teamsapp.local.yml`|This overrides `teamsapp.yml` with actions that enable local execution and debugging.|
|`teamsapp.testtool.yml`|This overrides `teamsapp.yml` with actions that enable local execution and debugging in Teams App Test Tool.|

"# software-tech" 
"# software-tech" 
"# software-tech" 
