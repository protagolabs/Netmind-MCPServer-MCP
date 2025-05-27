import json

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp import ClientSession
import asyncio


server = StdioServerParameters(
    command='netmind-mcpserver-mcp',
    env={
        "NETMIND_API_TOKEN": "your netmind api token",
        "API_URL": "https://mcp.protago-dev.com/servers"
    }
)


async def main():
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            response = await session.list_tools()
            tools = [dict(t) for t in response.tools]
            print(json.dumps(tools, indent=4, ensure_ascii=False))

            response = await session.call_tool(
                "query_server",
                {'limit': 2, 'offset': 0}
            )
            print(len(json.loads(response.content[0].text)))

            response = await session.call_tool(
                "query_server",
                {'name': 'parse-pdf'}
            )
            print(len(json.loads(response.content[0].text)))

            response = await session.call_tool(
                "get_server",
                {'server_name': 'parse-pdf'}
            )
            print(response)

            response = await session.call_tool(
                "add_update_rating_review",
                {
                    'server_name': 'p',
                    'rating': 5,
                    'review': "This is a test review",
                }
            )
            print(response)

            response = await session.call_tool(
                "add_update_rating_review",
                {
                    'server_name': 'pdafadfafdafda',
                    'rating': 5,
                    'review': "This is a test review",
                }
            )
            print(response)

            response = await session.call_tool(
                "add_update_rating_review",
                {
                    'server_name': 'pdf',
                    'rating': 5,
                    'review': "This is a test review",
                }
            )
            print(response)

            response = await session.call_tool(
                "list_rating_review",
                {'server_name': 'pdf', 'offset': 0, 'limit': 10}
            )
            print(response)


if __name__ == "__main__":
    asyncio.run(main())
