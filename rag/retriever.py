from rag.rag_pipeline import create_vectorstore


def retrieve_context(query):

    vectorstore = create_vectorstore()

    retriever = vectorstore.as_retriever()

    docs = retriever.invoke(query)

    if docs:
        return docs[0].page_content

    return "No relevant document found."