from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

# Define the Product type using Strawberry
@strawberry.type
class Product:
    id: int
    name: str
    price: float

# Initialize the products list with some default data
products = [
    Product(id=1, name="Laptop", price=1200),
    Product(id=2, name="Smartphone", price=800)
]

# Define the Query type
@strawberry.type
class Query:
    @strawberry.field
    def get_products(self) -> list[Product]:
        return products

# Define the Mutation type
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_product(self, id: int, name: str, price: float) -> Product:
        new_product = Product(id=id, name=name, price=price)
        products.append(new_product)
        return new_product

# Create the schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Create the GraphQL router
graphql_app = GraphQLRouter(schema)

# Include the GraphQL router in the FastAPI app
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)