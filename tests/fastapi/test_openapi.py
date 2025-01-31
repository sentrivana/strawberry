import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Query:
    abc: str


def test_enable_graphiql_view_and_allow_queries_via_get():
    app = FastAPI()
    schema = strawberry.Schema(query=Query)
    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")

    assert "get" in app.openapi()["paths"]["/graphql"]
    assert "post" in app.openapi()["paths"]["/graphql"]


def test_disable_graphiql_view_and_allow_queries_via_get():
    app = FastAPI()
    schema = strawberry.Schema(query=Query)
    graphql_app = GraphQLRouter(schema, graphiql=False, allow_queries_via_get=False)
    app.include_router(graphql_app, prefix="/graphql")

    assert "get" not in app.openapi()["paths"]["/graphql"]
    assert "post" in app.openapi()["paths"]["/graphql"]
