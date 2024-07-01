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

    # print("found result", analysis_result)
    # assessment = ImageInformation(
    #     worker_details_id = choice(["7234879137", "1290470219", "358093509", "35809813905"])[0],
    #     body_part_name = analysis_result['body_parts'],
    #     image_path = image_path,
    #     timestamp = datetime.utcnow(),
    #     gender = "Male",
    #     worker_present=analysis_result['worker_present'] == 'true',
    #     worker_count=int(analysis_result['worker_count']),
    #     ppe_worn=analysis_result['ppe_worn'],
    #     visible_tools=analysis_result['visible_tools'],
    #     environment_type=analysis_result['environment_type'],
    #     back_position=analysis_result['back_position'],
    #     neck_position=analysis_result['neck_position'],
    #     arm_position=analysis_result['arm_position'],
    #     leg_position=analysis_result['leg_position'],
    #     lifting_status=analysis_result['lifting_status'] == 'true',
    #     repetitive_motion=analysis_result['repetitive_motion'] == 'true',
    #     work_height=analysis_result['work_height'],
    #     balance_status=analysis_result['balance_status'],
    #     work_surface=analysis_result['work_surface'],
    #     ergonomic_risk_level=analysis_result['ergonomic_risk_level'],
    #     fatigue_indicators=analysis_result['fatigue_indicators'] == 'true',
    #     cumulative_risk_score=int(analysis_result['cumulative_risk_score']),
    #     max_strain_in_part=analysis_result['max_strain_in_part']
    #     )
    # print("db has been created")
    # # print(analysis_result)
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



