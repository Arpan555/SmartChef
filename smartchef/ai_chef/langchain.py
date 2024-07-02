from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config

def askRecipe(recipe_msg):
    SECRET_KEY = config("OPENAI_API_KEY")
    
    chat = ChatOpenAI(openai_api_key=SECRET_KEY)
    
    systemMsgPrompt = SystemMessagePromptTemplate.\
    from_template("You can be write any type of food recipe which can be cooked in 5 minutes. you are only allowed to answer food related queries. if you dont know the answer then tell o don't know the answer.")
    
    humanMsgPrompt = HumanMessagePromptTemplate.\
    from_template("{asked_recipe}")

    chatPrompt = ChatPromptTemplate.from_messages([
        systemMsgPrompt,
        humanMsgPrompt
    ])

    formattedChatPrompt = chatPrompt.format_messages(asked_recipe=recipe_msg)
    
    response=chat.invoke(formattedChatPrompt)
    return response.content