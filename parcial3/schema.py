import graphene
import farmacia.schema

class Query(farmacia.schema.Query, graphene.ObjectType):
    pass

class Mutation(farmacia.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)