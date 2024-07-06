from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

from ecommbot.ingest import ingestdata

def generate(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    system_template = """You are an ecommerce bot who is expert in giving product recommendations
    and answer to customer queries. Analyze product titles and
    reviews to provide accurate and helpful responses. Ensure your answers are relevant to the 
    product context and refrain from staying off topic. Your responses should be concise and
    informative.

    CONTEXT: 
    {context}

    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("human", "{question}")
    ])

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


if __name__ == "__main__":
    vstore = ingestdata("done")
    chain = generate(vstore)
    response = chain.invoke("can you tell me the best bluetooth buds?")
    print(response)
