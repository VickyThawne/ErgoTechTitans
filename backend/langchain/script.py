from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import json

# Define the response schemas
response_schemas = [
    ResponseSchema(name="worker_present", description="Is there a worker visible in the image?"),
    ResponseSchema(name="worker_count", description="How many workers are visible in the image?"),
    ResponseSchema(name="ppe_present", description="Is the worker wearing visible PPE (hard hat, safety vest)?"),
    ResponseSchema(name="tool_visible", description="Are any tools visible in the worker's hands or nearby?"),
    ResponseSchema(name="work_environment", description="What type of construction environment is shown (e.g., building interior, exterior, scaffolding)?")
]

# Create the output parser
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Create the prompt template
template = """
You are an AI assistant tasked with analyzing an image of a construction site. Please answer the following questions about the image:

1. Is there a worker visible in the image?
2. How many workers are visible in the image?
3. Is the worker wearing visible PPE (hard hat, safety vest)?
4. Are any tools visible in the worker's hands or nearby?
5. What type of construction environment is shown (e.g., building interior, exterior, scaffolding)?

{format_instructions}
"""

message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "{What'}?",
        },  # You can optionally provide text parts
        {"type": "image_url", "image_url": image_url},
    ]
)
llm.invoke([message])

image_analyzer_chain = LLMChain(llm=llm, prompt=prompt)

# Function to run the chain and parse the output
def run_image_analyzer(image_description):
    result = image_analyzer_chain.run(image_description=image_description)
    parsed_result = output_parser.parse(result)
    return json.dumps(parsed_result, indent=2)

# Example usage
image_description = "The image shows a construction worker on a building site. The worker is wearing a yellow hard hat and an orange safety vest. They are standing on scaffolding and holding a power drill."
print(run_image_analyzer(image_description))