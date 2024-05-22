const {
  TeamsActivityHandler,
  MemoryStorage,
  ConversationState,
  UserState,
  ActivityHandler,
} = require("botbuilder");
const axios = require("axios");

// Create the conversation state with in-memory storage
const memoryStorage = new MemoryStorage();
const conversationState = new ConversationState(memoryStorage);
const userState = new UserState(memoryStorage);

// Define the handleMessage function
async function handleMessage(userMessage) {
  try {
    const response = await axios.post(
      "https://elte-chatbot-backend.guyem.com:5000/api/endpoint",
      {
        message: userMessage,
      }
    );
    console.log(response.data);
    return response.data || "Sorry, something went wrong.";
  } catch (error) {
    console.error(error);
    return "Error communicating with the backend.";
  }
}

class TeamsBot extends TeamsActivityHandler {
  constructor() {
    super();
    this.conversationState = conversationState;
    this.userState = userState;

    this.onMessage(async (context, next) => {
      const userMessage = context.activity.text;
      const responseMessage = await handleMessage(userMessage);
      await context.sendActivity(responseMessage);
      // By calling next() you ensure that the next BotHandler is run.
      await next();
    });

    // Listen to MembersAdded event, view https://docs.microsoft.com/en-us/microsoftteams/platform/resources/bot-v3/bots-notifications for more events
    this.onMembersAdded(async (context, next) => {
      const membersAdded = context.activity.membersAdded;
      const welcomeText = "Hello and welcome!";
      for (let member of membersAdded) {
        if (member.id !== context.activity.recipient.id) {
          await context.sendActivity(welcomeText);
        }
      }
      await next();
    });
  }
}

module.exports.TeamsBot = TeamsBot;
