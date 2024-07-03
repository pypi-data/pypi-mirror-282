from typing import List
from pydantic import BaseModel, Field
from therix.core.data_sources import PDFDataSource
from therix.core.embedding_models import (
    AzureOpenAIEmbedding3LargeEmbeddingModel,
    BedrockTitanEmbedding,
    OpenAITextAdaEmbeddingModel,
)
from therix.core.inference_models import (
    AzureOpenAIGPT4InferenceModel,
    AzureOpenAIGPT4OInferenceModel,
    OpenAIGPT4TurboPreviewInferenceModel,
)
from therix.core.inference_models import (
    OpenAIGPT4TurboPreviewInferenceModel,GroqLlama370b
)
from therix.core.embedding_models import (
    OpenAITextAdaEmbeddingModel,
)
from therix.core.inference_models import (
    OpenAIGPT4TurboPreviewInferenceModel,
)
from therix.core.output_parser import OutputParserWrapper
from therix.core.pipeline import Pipeline
import sys

from therix.core.system_prompt_config import SystemPromptConfig
from therix.core.trace import Trace

GROQ_API_KEY=''

# TODO: Init therix with DB details, and license key

## Usage:
# python main.py ad11128d-d2ec-4f7c-8d87-15c1a5dfe1a9 "how does it help in reasoning?"

# if args has pipeline_id, then load the pipeline
## else create new pipeline
sys_prompt = """Answer the question based only on the following context and reply with your capabilities if something is out of context.
        Context: 
        {context}

        Question: {question}
        The output should be a valid json: {format_instructions}
        """


if len(sys.argv) > 1:
    pipeline = Pipeline.from_id(sys.argv[1])
    question = sys.argv[2]
    session_id = None

    if len(sys.argv) < 4:
        pass
    else:
        session_id = sys.argv[3]

    ans = pipeline.invoke(question, session_id)
    print(ans)
else:
    pipeline = Pipeline(name="My New Published Pipeline")
    (
        pipeline.add(PDFDataSource(config={"files": ["../../test-data/rat.pdf"]}))
        .add(BedrockTitanEmbedding(config={"bedrock_aws_access_key_id" : "",
                                "bedrock_aws_secret_access_key" : "",
                                "bedrock_aws_session_token" : "",
                                "bedrock_region_name" : "us-east-1"}))
        .add(GroqLlama370b(config={"groq_api_key": GROQ_API_KEY}))
        # .add(AzureOpenAIGPT4OInferenceModel(config={"azure_api_key" : "" , "openai_api_version" :  "", "azure_endpoint" : "" , "azure_deployment" : "" }))
        # .add(SystemPromptConfig(config={"system_prompt" : sys_prompt}))
        
        .add(
            Trace(
                config={
                    "secret_key": "sk-lf-3607c024-ad18-4d88-abca-8db3cf97f854",
                    "public_key": "pk-lf-c6ee86c5-9e2e-4f41-a459-b60012b0305d",
                    "identifier": "my own pipeline",
                }
            )
        )
        .save()
    )

    pipeline.publish()
    pipeline.preprocess_data()
    print(pipeline.id)


# ASYNCHRONOUS CALL - EXAMPLE
    # async def call_pipeline():
    #     ans = await pipeline.async_invoke("What are some usecases of RAT?")
    #     print(ans)
    #     return ans
    
    # asyncio.run(call_pipeline())
    # print(ans)


    # OUTPUT_PARSER FOR RAG -->
    class TestDetails(BaseModel):
        name: str = Field(description="Name of the Topic")
        description: str = Field(description="Short description of the Topic")
        citations: str = Field(description="provide the exact file path")
        page: str = Field(description="page number of the topic")


    class OutputParserJSON(BaseModel):
        tests: List[TestDetails] = Field(description="Topic")    

    ans = pipeline.invoke(question="What is ablation study?")
    print(ans)
