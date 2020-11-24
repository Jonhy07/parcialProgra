import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id #needed for updating

class ProveedorNode(DjangoObjectType):
    class Meta:
        model = Proveedor
        filter_fields = ['proveedor_nombre']
        interfaces = (graphene.relay.Node,)

class CasaMedicaNode(DjangoObjectType):
    class Meta:
        model = CasaMedica
        filter_fields = ['casa_medica']
        interfaces = (graphene.relay.Node,)

class MedicamentoNode(DjangoObjectType):
    class Meta:
        model = Medicamento
        filter_fields = [
              'medicamento_nombre',
              'medicamento_proveedor__proveedor_nombre',
              'medicamento_casa__casa_medica'
               ]
        interfaces = (graphene.relay.Node,)

class CreateCasa(graphene.relay.ClientIDMutation):
    casa_medica = graphene.Field(CasaMedicaNode)
    class Input:
        casa_medica = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        casa_medica = CasaMedica(
            casa_medica=input.get('casa_medica')
        )
        casa_medica.save()
        return CreateCasa(casa_medica=casa_medica)

class CreateMedicamento(graphene.relay.ClientIDMutation):
    medicamento = graphene.Field(MedicamentoNode)

    class Input:
        medicamento_nombre = graphene.String()
        medicamento_proveedor = graphene.String()
        medicamento_casa = graphene.String()

    def mutate_and_get_payload(root, info, **input):

        medicamento = Medicamento(
            medicamento_nombre=input.get('medicamento_nombre'),
            medicamento_proveedor=Proveedor.objects.get(proveedor_nombre=input.get('medicamento_proveedor')),
            medicamento_casa= CasaMedica.objects.get(casa_medica=input.get('medicamento_casa'))
        )
        medicamento.save()
        return CreateMedicamento(medicamento=medicamento)

"""
class UpdateEmployee(graphene.relay.ClientIDMutation):
    Medicamento = graphene.Field(EmployeeNode)
    class Input:
        id = graphene.String()
        nombre_medicamento = graphene.String()
        employee_city = graphene.String()
        employee_title = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        Medicamento = Medicamento.objects.get(pk=from_global_id(input.get('id'))[1])
        Medicamento.nombre_medicamento = input.get('nombre_medicamento')
        Medicamento.employee_city = City.objects.get(city_name=input.get('employee_city'))
        Medicamento.employee_title = Title.objects.get(title_name=input.get('employee_title'))
        Medicamento.save()
        return UpdateEmployee(Medicamento=Medicamento)

class DeleteEmployee(graphene.relay.ClientIDMutation):
    Medicamento = graphene.Field(EmployeeNode)
    class Input:
        id = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        Medicamento = Medicamento.objects.get(pk=from_global_id(input.get('id'))[1])
        Medicamento.delete()
        return DeleteEmployee(Medicamento=Medicamento)
"""

class Query(object):
    proveedor = graphene.relay.Node.Field(ProveedorNode)
    todos_proveedores = DjangoFilterConnectionField(ProveedorNode)
    casa_medica = graphene.relay.Node.Field(CasaMedicaNode)
    todos_casas = DjangoFilterConnectionField(CasaMedicaNode)
    medicamento = graphene.relay.Node.Field(MedicamentoNode)
    todos_medicamentos = DjangoFilterConnectionField(MedicamentoNode)


class Mutation(graphene.AbstractType):
    create_casa = CreateCasa.Field()
    create_medicamento = CreateMedicamento.Field()
    """
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()
    """