class PROVIDERS:
    GOOGLE = "Google"
    MICROSOFT_AZURE = "Microsoft Azure"
    OPEN_AI = "OpenAI"
    ANTHROPIC = "Anthropic"
    GROQ = "Groq"
    TOGETHER_AI = "Together AI"


def get_model(llm):
    if llm["provider"] == PROVIDERS.GOOGLE:
        from langchain_google_genai import ChatGoogleGenerativeAI
        model = ChatGoogleGenerativeAI(
            model=llm["selected_model"],
            google_api_key=llm["api_key"]
        )
    elif llm["provider"] == PROVIDERS.MICROSOFT_AZURE:
        from langchain_openai import AzureChatOpenAI
        model = AzureChatOpenAI(
            model=llm["selected_model"],
            api_key=llm["api_key"],
            api_version=llm["azure_api_version"],
            azure_endpoint=llm["azure_endpoint"],
        )
    elif llm["provider"] == PROVIDERS.OPEN_AI:
        from langchain_openai import ChatOpenAI
        model = ChatOpenAI(
            model=llm["selected_model"],
            api_key=llm["api_key"]
        )
    elif llm["provider"] == PROVIDERS.ANTHROPIC:
        from langchain_anthropic import ChatAnthropic
        model = ChatAnthropic(
            model=llm["selected_model"],
            api_key=llm["api_key"]
        )
    elif llm["provider"] == PROVIDERS.GROQ:
        from langchain_groq import ChatGroq
        model = ChatGroq(
            model_name=llm["selected_model"],
            api_key=llm["api_key"]
        )
    elif llm["provider"] == PROVIDERS.TOGETHER_AI:
        from langchain_together import ChatTogether
        model = ChatTogether(
            model=llm["selected_model"],
            api_key=llm["api_key"]
        )

    return model


