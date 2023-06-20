import os
import asyncio
from playwright.async_api import async_playwright
from playwright.async_api import APIRequestContext, async_playwright
import pytest
from github_api import *

API_TOKEN = os.getenv('API_TOKEN')
USER_NAME = os.getenv('USER_NAME')

@pytest.mark.api
@pytest.fixture()
async def api_request_context():
    async with async_playwright() as p:
        request_context = await p.request.new_context(base_url="https://api.github.com")
        yield request_context
        await request_context.dispose()
        

async def test_full_flow_scenario(api_request_context: APIRequestContext):
    # Create a new repository
    response_create_a_repo = await create_new_repository( api_request_context=api_request_context, repo_name="test-repo", \
        is_private=True, api_token=API_TOKEN)
    assert response_create_a_repo.status == 201

    # Get the latest created repository    
    response_retrieve_a_repo = await retrieve_created_repository( api_request_context=api_request_context, repo_name="test-repo", \
       is_private=True, api_token=API_TOKEN)
    assert response_retrieve_a_repo == 200

    # Update name and description of the repository
    response_update_a_repo = await update_repository(api_request_context=api_request_context, \
                                repo_name="test-pw-repo", repo_update_name="test-pw-repo-updated", \
                                username=USER_NAME, description="This is a repo built with playwright", is_private=False, \
                                api_token=API_TOKEN)
    response_body_update_a_repo = await response_update_a_repo.json()
    assert response_update_a_repo.status == 200
    assert response_body_update_a_repo["name"] == "test-pw-repo-update"
    assert response_body_update_a_repo["description"] == "This is a repo built with playwright"

    # Remove the repository
    response_delete_a_repo = await remove_repository(api_request_context=api_request_context, \
                                repo_name="test-pw-repo-updated", username=USER_NAME, api_token=API_TOKEN)
    assert response_delete_a_repo.status == 204