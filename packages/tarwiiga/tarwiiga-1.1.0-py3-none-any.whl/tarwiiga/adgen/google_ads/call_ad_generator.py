from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from ...llm import get_model


def get_response_schemas():
    path1_schema = ResponseSchema(
        name="path1",
        description="This is a url path 1 that come after domain, one word or two only, max 15 characters"
    )
    path2_schema = ResponseSchema(
        name="path2",
        description="This is a url path 2 that come after path 1, one word or two only, max 15 characters"
    )
    headline1_schema = ResponseSchema(
        name="headline1",
        description="Ad headline 1, max 30 characters"
    )
    headline2_schema = ResponseSchema(
        name="headline2",
        description="Ad headline 2, max 30 characters"
    )
    business_name_schema = ResponseSchema(
        name="business_name",
        description="Ad business name, max 25 characters"
    )
    description1_schema = ResponseSchema(
        name="description1",
        description="Ad description 1, max 90 characters, always end it with ."
    )
    description2_schema = ResponseSchema(
        name="description2",
        description="Ad description 2, max 90 characters always end it with ."
    )

    schemas = [
        path1_schema,
        path2_schema,
        headline1_schema,
        headline2_schema,
        business_name_schema,
        description1_schema,
        description2_schema,
    ]

    return schemas


def get_output_parser():
    response_schemas = get_response_schemas()
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    return output_parser


def get_prompt_message(user_input, format_instructions):
    template = """
    You are a google ads spicilaist, you write ad copies for call-only ads.
    Your ads should be attractive, and make clients click to ask for the services.
    You will be given a short input about and ad idea and your job is to generate the ad.
    For the following input, give the following information:

    path1: This is a url path 1 that come after domain, one word or two only, max 15 characters
    path2: This is a url path 2 that come after path 1, one word or two only, max 15 characters
    headline1: Ad headline 1, max 30 characters
    headline2: Ad headline 2, max 30 characters
    business_name: Ad business name, max 25 characters
    description1: Ad description 1, max 90 characters, always end it with .
    description2: Ad description 2, max 90 characters always end it with .
    
    only give the JSON object in the language of input

    input: {user_input}

    {format_instructions}
    """

    prompt = ChatPromptTemplate.from_template(template=template)

    messages = prompt.format_messages(
        user_input=user_input,
        format_instructions=format_instructions,
    )

    return messages[0]


def generate_call_ad(user_input, llm):
    model = get_model(llm)
    output_parser = get_output_parser()
    format_instructions = output_parser.get_format_instructions()
    prompt = get_prompt_message(
        user_input=user_input,
        format_instructions=format_instructions,
    ).content
    response = model.invoke(prompt)
    call_ad = output_parser.parse(response.content)
    return call_ad, prompt
