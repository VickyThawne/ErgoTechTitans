from langchain.schema import HumanMessage
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate
from typing import List

from langchain_google_genai import ChatGoogleGenerativeAI
import os

from app.models import ImageInformation

from .response_schema import response_schemas

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)



def image_analysis_chain(image_path):
    # Define the prompt template
    template = """
    You are an AI assistant tasked with analyzing an image of a construction site. Please analyze the image and provide the following information:

    {format_instructions}

    Provide your analysis based solely on what you can observe in the image.
    """

    prompt = PromptTemplate(
        template=template,
        partial_variables={"format_instructions": output_parser.get_format_instructions()}
    )

    # Create the output parser

    analysis_result = analyze_construction_image(image_path, prompt)
    return analysis_result

def analyze_construction_image(image_path: str, prompt):



    googleai_api_key = os.getenv("GOOGLE_GENAI_APIKEY")

    vision_llm = ChatGoogleGenerativeAI(model="gemini-pro-vision", google_api_key=googleai_api_key)
    text_llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=googleai_api_key)
    
    human_message = HumanMessage(
        content=[
            {"type": "text", "text": prompt.format()},
            {"type": "image_url", "image_url": image_path},
        ]
    )
    
    response = vision_llm([human_message])
    parsed_response = output_parser.parse(response.content)
    return parsed_response



