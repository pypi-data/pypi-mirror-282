from rich import print
from .utils import manage_cache_file
from get_gitlab_issues import get_gitlab_issues, get_gitlab_issue

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS


def generate_embeddings(
        api_base,
        access_token,
        labels,
        group_id,
        iteration_id,
        cache_file,
        chunk_size,
        chunk_overlap,
        embedding_model,
        sprint_goals
):
    print("[green]Recieveing issues from GitLab...[/green]")
    issues = get_gitlab_issues(access_token, api_base, group_id, labels, iteration_id)
    board = []
    for issue in issues:
        issue = issue.attributes
        board.append(issue)

    print("[green]✅ Issues received[/green]")
    manage_cache_file(create=True, content=sprint_goals+"\n "+str(board))

    print("[green]Generate embeddings...[/green]")
    loader = TextLoader(cache_file)
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = splitter.split_documents(documents)

    embedding = embedding_model
    vector_store = FAISS.from_documents(texts, embedding)
    retriever = vector_store.as_retriever()
    manage_cache_file(content="")
    print("[green]✅ Embeddings generated[/green]")
    return retriever