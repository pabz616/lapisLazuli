from playwright.async_api import APIRequestContext

"""GITHUB API CLIENTS"""

async def create_new_repository(api_request_context: APIRequestContext, repo_name: str, is_private: bool,api_token: str):
    return await api_request_context.post(
        "/user/repos",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
        data={"name": repo_name, "private": is_private},
    )
    
async def retrieve_created_repository(api_request_context: APIRequestContext, repo_name: str, is_private: bool,api_token: str):
    return await api_request_context.get(
        "/user/repos",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
        data={"name": repo_name, "private": is_private},
    )

async def update_repository(api_request_context: APIRequestContext, repo_name: str, repo_update_name: str, \
    username: str, description: str, is_private: bool, api_token: str):
    repo_update_name = repo_name+"_updated"
    
    return await api_request_context.patch(
        f"/repos/{username}/{repo_name}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
        data={"name": repo_update_name, "description": description, \
        "private": is_private},
    )

async def remove_repository(api_request_context: APIRequestContext, repo_name: str, username: str, api_token: str):
    return await api_request_context.delete(
        f"/repos/{username}/{repo_name}",
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {api_token}",
        },
    )