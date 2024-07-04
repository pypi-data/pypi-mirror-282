proj_accesso_cliente = {
    'token_spice': 1,
    "token_unauthorized": 1,
    '_id': 1,
    "fecha_vigencia": 1,
    "nivel_de_acceso": 1,
    "status": 1,
    "nombre": 1,
    "apellido": 1,
    "nacimiento": 1,
    "active_plan_id": 1,
    "email": 1,
    "documento": 1,
    "plan_corporativo": 1,
    "plan": 1,
    "sede": 1
}


def create_pipeline_merchant_in_socios(socio_id):
    pipeline = [
        {'$match': {'_id': socio_id}},
        {'$lookup': {
            'from': 'planes',
            'localField': 'active_plan_id',
            'foreignField': '_id',
            'as': 'plan'
        }},
        {'$unwind': {'path': '$plan'}},
        {'$lookup': {
            'from': 'merchants',
            'localField': 'plan.merchant_id',
            'foreignField': '_id',
            'as': 'merchant'
        }},
        {'$unwind': {'path': '$merchant'}}
    ]
    return pipeline
